# weather-assignment
Weather-Based Order Delay System using Python and OpenWeather API.  This project fetches real-time weather data for order cities and marks orders as delayed  based on weather conditions. It uses parallel API calls and includes error handling  for invalid cities.

## 📌 Overview
This project checks real-time weather conditions for delivery locations and updates order status accordingly.

## 🚀 Features
- Parallel API calls using ThreadPoolExecutor
- Weather-based delay detection
- Error handling for invalid cities
- Dynamic customer notification messages

## 🛠️ Tech Stack
- Python
- OpenWeather API
- JSON

## ⚙️ How It Works
1. Reads order data from JSON file
2. Fetches weather data for each city
3. Marks orders as "Delayed" if weather is bad
4. Handles invalid city errors without stopping execution
5. Saves updated data to a new JSON file

## ▶️ Run Instructions
```bash
pip install -r requirements.txt
python app.py
