from inspect import currentframe
import requests

api_key = "f465a3bed06b150c9982d5029c5d3acc"

def get_exchange_rate(currency_from, currency_to):
    url = f"http://api.exchangeratesapi.io/v1/latest?access_key={api_key}"
    request = requests.get(url)
    exchange_rate_json = request.json()

    currency_from = exchange_rate_json['rates'][currency_from]
    currency_to = exchange_rate_json['rates'][currency_to] #PHP at the moment

    conversion = currency_to / currency_from
    
    return float(conversion)
