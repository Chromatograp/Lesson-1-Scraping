import requests
import json

url = 'https://anapioficeandfire.com/api/characters'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)
j_data = response.json()
j = json.loads(json.dumps(j_data))

with open('Ice_and_Fire_characters.json', 'w') as f:
    json.dump(j, f, indent=4)

print(f'Количество персонажей сериала Ice and Fire = {len(j_data)}')