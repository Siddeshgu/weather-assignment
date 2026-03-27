import json
import requests
import os
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor

# Load API key
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Load orders
with open("orders.json", "r") as file:
    orders = json.load(file)

# Function to fetch weather
def get_weather(order):
    city = order["city"]
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print(f"Error for {city}: {data.get('message')}")
            return order

        weather = data["weather"][0]["main"]

        if weather.lower() in ["rain", "snow", "extreme"]:
            order["status"] = "Delayed"
            print(f"Hi {order['customer']}, your order to {city} is delayed due to {weather}")

        return order

    except Exception as e:
        print(f"Exception: {e}")
        return order

# Run in parallel
with ThreadPoolExecutor() as executor:
    updated_orders = list(executor.map(get_weather, orders))

# Save updated file
with open("orders_updated.json", "w") as file:
    json.dump(updated_orders, file, indent=2)

print("Done ✅")