import json
from forex_python.converter import CurrencyCodes

def map_currency(codigos_monedas):
    currency_codes = CurrencyCodes()
    currency_info = {}

    for currency in codigos_monedas:
        symbol = currency_codes.get_symbol(currency)  # Obtener el símbolo
        name = currency_codes.get_currency_name(currency)  # Obtener el nombre completo
        currency_info[currency] = f"{name} ({symbol})"

    with open('food_crisis/data/currency_info.json', 'w') as json_file:
        json.dump(currency_info, json_file, indent=4)

    return currency_info