# Workout Tracker

This Python script automates the process of logging workout exercises by interacting with the Nutritionix API to track workouts and the Sheety API to store exercise data into a spreadsheet.

## Features

- Tracks exercises using the Nutritionix API by specifying workout activities in natural language.
- Logs exercise details such as duration and calories burned.
- Stores workout data in a Google Sheet via Sheety API.
- Automatically logs the date and time of the workout session.

## Requirements

1. Python 3.x
2. [Nutritionix API](https://www.nutritionix.com/business/api)
3. [Sheety API](https://sheety.co/)
4. [dotenv](https://pypi.org/project/python-dotenv/) (to manage environment variables)

## Setup

1. **Clone the repository:**

```bash
git clone <repository-url>
cd <repository-folder>
```

2. **Install Dependecies:**

```bash
pip install requests python-dotenv
```

3. **Create a *.env* file in the root directory with the following:**

```makefile
APP_ID=your_nutritionix_app_id
API_KEY=your_nutritionix_api_key
SHEETY_TOKEN=your_sheety_bearer_token
ADD_ROW_URL=your_sheety_api_endpoint
```
- Replace the placeholders with your actual API keys and Sheety API URL.

4. **Run the script:**

```bash
python workout_tracker.py
```

## How it Works
1. Exercise Tracking:
The script uses the Nutritionix API to extract exercise information based on a workout description provided in natural language.

2. Logging Workout Data:
It logs the date, time, type of exercise, duration, and calories burned into a Google Sheet using the Sheety API.

## Environment Variables 
- APP_ID: Your Nutritionix App ID.
- API_KEY: Your Nutritionix API Key.
- SHEETY_TOKEN: Your Sheety API Bearer token for authorization.
- ADD_ROW_URL: The Sheety API endpoint to add new rows to your spreadsheet.
