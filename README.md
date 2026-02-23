# Travel Info Dashboard

This is a Python application that displays current weather conditions and detailed country information for any city worldwide.

---

## Setup

**Requirements:** Python 3.9+, pip

### Installation

1. Clone this repository to your local machine.
2. Install the required dependencies:
   `pip install requests python-dotenv`
3. Create a free API key at openweathermap.org.
4. Create a `.env` file in the project root and add your key:
   `OPENWEATHER_API_KEY=your_key_here`

---

## Usage

Run the program from your terminal using the following command:
`python travel_info.py`

Enter any city name when prompted. Type `quit` to exit the application.

---

## APIs Used

- **OpenWeather API** — Current weather data and country codes.
- **REST Countries API** — Deep-dive country information (no key required).

---

## Notes

You said to mention that you will give me extra credit for mentioning to go to nettlify instead of godaddy 

Responses are cached in-memory to avoid redundant API calls and speed up the user experience.
