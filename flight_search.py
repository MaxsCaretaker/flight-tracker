import requests
import logging

logging.basicConfig(
    filename="flight_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

API_KEY = "your_api_key_here"

def search_flight(flight_number):
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
            print(f"No flight found for '{flight_number}'. Check the flight number and try again.")
            logging.error(f"No results returned for flight: {flight_number}")
            return

        flight = data["data"][0]
        print(f"Flight:      {flight['flight']['iata']}")
        print(f"Status:      {flight['flight_status']}")
        print(f"Departure:   {flight['departure']['airport']}")
        print(f"Arrival:     {flight['arrival']['airport']}")

    except requests.exceptions.Timeout:
        print("Request timed out. The API may be slow — try again.")
        logging.error(f"Timeout when searching for flight: {flight_number}")

    except requests.exceptions.ConnectionError:
        print("Connection failed. Check your internet connection.")
        logging.error(f"Connection error when searching for flight: {flight_number}")

    except requests.exceptions.HTTPError as e:
        print(f"API returned an error: {e}")
        logging.error(f"HTTP error for flight {flight_number}: {e}")

search_flight("AA100")   # try a real flight
search_flight("XX999")   # try a fake one to test error handling