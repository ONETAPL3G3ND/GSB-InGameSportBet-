import requests
import random

API_KEY = ''
BASE_URL = 'https://api.the-odds-api.com/v4/sports/'


sports = ["soccer", 'basketball', 'boxing']

# Функция для получения текущих матчей и коэффициентов
def get_current_matches_and_odds(api_key, sports):
    results = {}
    for sport in sports:

        response = requests.get(f'{BASE_URL}{sport}/odds', params={
            'apiKey': api_key,
            'regions': 'us',  # или 'uk', 'eu' и т.д.
            'markets': 'h2h',  # 'h2h' - это коэффициенты на победу
            'oddsFormat': 'decimal'
        })

        if response.status_code == 200:
            data = response.json()
            results[sport] = data
        else:
            print(f"Ошибка получения данных для {sport}: {response.status_code}")

    return results

# Получение текущих матчей и коэффициентов
matches_and_odds = get_current_matches_and_odds(API_KEY, sports)
print(matches_and_odds)
print(list(matches_and_odds.keys()))