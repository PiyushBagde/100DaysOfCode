from datetime import datetime
import os
import requests

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
TOKEN = os.environ['TOKEN']
GENDER = "male"
WEIGHT_KG = 53
HEIGHT_CM = 167.64
AGE = 22

today_date = datetime.today().strftime("%d/%m/%Y")
today_time = datetime.today().strftime("%H:%M:%S")

text = input("Which exercise you did? ")
exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

sheet_headers = {"Authorization": f"Basic {TOKEN}"}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ['sheet_endpoint']

parameters = {
    "query": text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=exercise_headers)
response.raise_for_status()
data = response.json()

for exercise in data['exercises']:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=sheet_headers)
    print(sheet_response.text)
