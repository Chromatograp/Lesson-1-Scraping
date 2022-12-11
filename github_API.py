import requests
import json

# Адрес страницы со списком репозиториев пользователя через API:
url = 'https://api.github.com/users/Pectin-eng/repos'
# Указываем заголовки:
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

# Получаем список и переводим в формат json:
response = requests.get(url, headers=headers)
j_data = response.json()
j = json.loads(json.dumps(j_data))

# Записываем список в файл:
with open('Pectin-eng_repos.json', 'w') as f:
    json.dump(j, f, indent=4)

# Выводим информацию для пользователя:
print(f'Количество репозиториев пользователя {j[0].get("owner").get("login")} = {len(j_data)}')