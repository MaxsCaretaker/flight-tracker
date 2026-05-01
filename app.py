from flask import Flask, request, jsonify, render_template
import requests
import logging
import os


app = Flask(__name__)

logging.basicConfig(
    filename="flight_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

API_KEY = os.getenv("AVIATION_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/flight")
def get_flight():
    flight_number = request.args.get("flight")

    if not flight_number:
        return jsonify({"error": "Please provide a flight number."}), 400

    url = "http://api.aviationstack.com/v1/flights"
    params = {
        "access_key": API_KEY,
        "flight_iata": flight_number
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if not data.get("data"):
            logging.error(f"No results for flight: {flight_number}")
            return jsonify({"error": f"No flight found for '{flight_number}'."}), 404

        flight = data["data"][0]
        result = {
            "flight": flight["flight"]["iata"],
            "status": flight["flight_status"],
            "departure": flight["departure"]["airport"],
            "departure_time": flight["departure"].get("scheduled", "N/A"),
            "departure_delay": flight["departure"].get("delay", 0),
            "arrival": flight["arrival"]["airport"],
            "arrival_time": flight["arrival"].get("scheduled", "N/A"),
            "arrival_delay": flight["arrival"].get("delay", 0),
        }
        return jsonify(result)

    except requests.exceptions.Timeout:
        logging.error(f"Timeout for flight: {flight_number}")
        return jsonify({"error": "Request timed out. Try again."}), 504

    except requests.exceptions.ConnectionError:
        logging.error(f"Connection error for flight: {flight_number}")
        return jsonify({"error": "Connection failed. Check your internet."}), 503

    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error for flight {flight_number}: {e}")
        return jsonify({"error": f"API error: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
