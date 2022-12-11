import requests
import json

food = input("Enter the product's name: ")

nutrition_type = ['cooking', 'logging']
health = ['alcohol-free', 'celery-free', 'crustacean-free', 'dairy-free', 'egg-free', 'fish-free', 'fodmap-free', 'gluten-free', 'immuno-supportive', 'keto-friendly', 'kidney-friendly', 'kosher', 'low-fat-abs', 'low-potassium', 'low-sugar', 'lupine-free', 'mustard-free', 'no-oil-added', 'paleo', 'peanut-free', 'pescatarian', 'pork-free', 'red-meat-free', 'sesame-free', 'shellfish-free', 'soy-free', 'sugar-conscious', 'tree-nut-free', 'vegan', 'vegeterian', 'wheat-free']
category = ['generic-foods', 'generic-meals', 'packaged-foods', 'fast-foods']

nutrition_type_ = int(input('Enter the nutrition type number: '))
health_ = int(input('Enter the health label numder: '))
category_ = int(input('Enter the category number: '))

with open('id.txt', 'r') as file:
    lines = file.readlines()
    id = lines[0].split('=')[1]
    key = lines[1].split('=')[1]

url = f'https://api.edamam.com/api/food-database/v2/parser?app_id={id[:(len(id)-1)]}&app_key={key}&ingr={food}&nutrition-type={nutrition_type[nutrition_type_ - 1]}&health={health[health_ - 1]}&category={category[category_ - 1]}'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)
j_data = response.json()
j = json.loads(json.dumps(j_data))

with open('The_product_nutritional_value.json', 'w') as f:
    json.dump(j, f, indent=4)

print(f'1g of the product contains {j["parsed"][0]["food"]["nutrients"]["ENERC_KCAL"]} Kcal, {j["parsed"][0]["food"]["nutrients"]["PROCNT"]}g of proteins, {j["parsed"][0]["food"]["nutrients"]["FAT"]}g of lipids, {j["parsed"][0]["food"]["nutrients"]["CHOCDF"]}g of carbohydrates, {j["parsed"][0]["food"]["nutrients"]["FIBTG"]}g of dietary fiber per 10g.')