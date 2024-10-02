import datetime  # To handle date and time
import requests  # For making HTTP requests to APIs
import os  # To access environment variables
from dotenv import load_dotenv  # To load environment variables from a .env file

# Load environment variables from the .env file
load_dotenv()

# Access environment variables for Nutritionix and Sheety API authentication
app_id = os.getenv('APP_ID')
api_key = os.getenv('API_KEY')
sheety_token = os.getenv('SHEETY_TOKEN')

# Nutritionix API endpoint for tracking exercise
nutriotionix_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

# Headers required by the Nutritionix API
headers = {
    'x-app-id': app_id,
    'x-app-key': api_key,
}

# Get the workout description from user input
workout_description = input("Describe your workout (e.g., 'ran 5km in 30 minutes'): ")

# Pass the user input as a query parameter
params = {
    "query": workout_description
}

# Send a POST request to the Nutritionix API to get exercise data
request_json = requests.post(nutriotionix_url, headers=headers, json=params).json()['exercises']

# Print the response from the Nutritionix API for debugging
print(request_json)

# Get the current date and time
date_and_time = datetime.datetime.now()
formatted_date = date_and_time.strftime("%d/%m/%Y")  # Format the date as day/month/year
formatted_time = date_and_time.strftime("%H:%M:%S")  # Format the time as hour:minute:second

# Sheety API endpoint to add a new row to the spreadsheet
add_row_url = os.getenv('ADD_ROW_URL')

# Headers for authentication to Sheety API using Bearer token
headersAuth = {
    'Authorization': 'Bearer ' + sheety_token,
}

# Loop through the list of exercises from Nutritionix and log each one to the spreadsheet
for exercise in request_json:
    # Prepare the data to be sent to Sheety
    exercises_params = {
        'workout': {
            'date': formatted_date,
            'time': formatted_time,
            'exercise': exercise['name'].title(),  # Exercise name, formatted with title case
            'duration': str(exercise['duration_min']).title(),  # Duration of the exercise in minutes
            'calories': str(exercise['nf_calories']).title()  # Calories burned during the exercise
        }
    }
    # Send a POST request to Sheety to log the exercise data
    print(requests.post(add_row_url, json=exercises_params, headers=headersAuth))
