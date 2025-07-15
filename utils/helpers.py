from datetime import datetime
import requests

def get_current_time():
    return datetime.now().strftime("%I:%M %p")

def get_user_location():
    try:
        response = requests.get("https://ipinfo.io")
        return response.json()["city"]
    except:
        return "Unknown"
