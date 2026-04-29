# ✈️ Flight Tracker

A Python app that fetches real-time flight data from the AviationStack API. Search any flight by its IATA code and get live status, departure, and arrival information — with built-in error handling and automatic logging.

---

## Features

- Search any flight by IATA code (e.g. `AA100`)
- Displays live flight status, departure airport, and arrival airport
- Handles API errors, timeouts, and invalid flight numbers gracefully
- Automatically logs errors to `flight_errors.log` for debugging

---

## Tech Stack

- **Python 3.10**
- **Requests** — HTTP library for API calls
- **AviationStack API** — real-time flight data
- **Logging** — Python's built-in logging module for error tracking

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/MaxsCaretaker/flight-tracker.git
cd flight-tracker
```

### 2. Install dependencies

```bash
pip install requests
```

### 3. Add your API key

Sign up for a free API key at [aviationstack.com](https://aviationstack.com), then open `flight_search.py` and replace:

```python
API_KEY = "your_api_key_here"
```

### 4. Run the app

```bash
python flight_search.py
```

---

## Example Output

```
Flight:      AA100
Status:      scheduled
Departure:   John F Kennedy International
Arrival:     Heathrow
```

If an invalid flight number is searched:

```
No flight found for 'XX999'. Check the flight number and try again.
```

The error is also silently written to `flight_errors.log`:

```
2026-04-29 14:23:11,456 - ERROR - No results returned for flight: XX999
```

---

## Error Handling

| Scenario | User Message | Logged |
|---|---|---|
| Flight not found | "No flight found for..." | ✅ |
| Request timeout | "Request timed out..." | ✅ |
| No internet connection | "Connection failed..." | ✅ |
| API HTTP error | "API returned an error..." | ✅ |

---

## What I Learned

- How to authenticate and make requests to a REST API
- How to parse and extract data from JSON responses
- How to handle multiple failure modes without crashing
- How to implement error logging to replicate production system behavior

---

## Planned Features

- Flask web interface so users can search flights in a browser
- Airport search in addition to flight number
- Flight history and departure board view
- Email or SMS alerts for flight status changes

---
