import pycountry
import json

country_map = { country.alpha_3: country.name for country in pycountry.countries}

with open('food_crisis/data/country_mapping.json', 'w') as f:
    json.dump(country_map, f, indent=4)