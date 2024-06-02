import requests
import pprint

# Задание 1: Получение данных
# Импортируйте библиотеку requests.
# Отправьте GET-запрос к открытому API (например, https://api.github.com) с
# параметром для поиска репозиториев с кодом html.
# Распечатайте статус-код ответа.
# Распечатайте содержимое ответа в формате JSON.

params = {
'q' : 'html'
}
response = requests.get('https://api.github.com',params=params)
print(response.status_code)
print(response.ok)

response_json = response.json()
pprint.pprint(response_json)

