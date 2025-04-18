import requests
import os
import time
from dotenv import load_dotenv

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

if os.path.exists(".env"):
    load_dotenv()
    api_key = os.getenv("NASA_API_KEY")
else:
    api_key = None

def save_api_key(key):
    with open(".env", "w") as f:
        f.write(f"NASA_API_KEY={key}")

def validate_api_key(key):
    test_url = f"https://api.nasa.gov/planetary/apod?api_key={key}"
    response = requests.get(test_url)
    if response.status_code == 200:
        data = response.json()
        if 'error' in data:
            return False
        return True
    else:
        return False

while not api_key or not validate_api_key(api_key):
    clear()
    print("No valid API key found.")
    time.sleep(2)
    clear()
    api_key = input("Enter your NASA API Key: ").strip()
    clear()
    if validate_api_key(api_key):
        save_api_key(api_key)
        print("API key saved successfully!")
        time.sleep(2)
        clear()
    else:
        print("Invalid API key. Please try again.")
        time.sleep(2)
        clear()
        api_key = None

clear()
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("\n===== NASA API Example Response =====")
    print(f"Title: {data['title']}")
    print(f"Date: {data['date']}")
    print(f"Explanation: {data['explanation']}")
    print(f"Image URL: {data['url']}")
    print("\nThis is an example response. You can modify this script to fetch other NASA APIs.")
    print("Use their official documentation here: https://api.nasa.gov")
    print("=====================================\n")
elif response.status_code == 403:
    print("Access forbidden: Your API key is invalid or expired.")
elif response.status_code == 429:
    print("Too many requests: API limit reached.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
