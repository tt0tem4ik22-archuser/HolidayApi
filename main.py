import os
from dotenv import load_dotenv
import requests


MONTHS = ["Января","Февраля","Марта","Апреля","Мая","Июня","Июля","Августа","Сентября","Октября","Ноября","Декабря",]


def main():

    load_dotenv()
    api_key = os.getenv("API_KEY")
    params = {
    	api_key="{api_key}",
    	country="RU",
    	year=2025
    }
    link = f"https://calendarific.com/api/v2/holidays"

    response = requests.get(link, params=params)
    response.raise_for_status()
    
    for holiday in response.json()["response"]["holidays"]:
        print(f"""Дата: {holiday['date']['datetime']['day']} {MONTHS[holiday['date']['datetime']['month']-1]},
Название: {holiday['name']}
Описание: {holiday['description']}\n""")


if __name__ == "__main__":
	main()