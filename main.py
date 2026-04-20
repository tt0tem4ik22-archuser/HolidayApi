import os
from dotenv import load_dotenv
import requests
import json


def main():

    load_dotenv()
    api_key = os.getenv("API_KEY")

    link = f"https://calendarific.com/api/v2/holidays?&api_key={api_key}&country=US&year=2025"

    response = requests.get(link)
    response.raise_for_status()
    
    for holiday in response.json()["response"]["holidays"]:
        print(f"""Дата: {holiday['date']['datetime']['day']}.{holiday['date']['datetime']['month']},
Название: {holiday['name']}
Описание: {holiday['description']}\n""")


if __name__ == "__main__":
	main()