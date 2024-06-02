import requests
import pprint

print("*"*100)
print("Задание 1: Получение данных")
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

print("*"*100)
print("Задание 2: Параметры запрос")
# Задание 2: Параметры запрос
# 1. Используйте API, который позволяет фильтрацию данных через
# URL-параметры (например, https://jsonplaceholder.typicode.com/posts).
#
# 2. Отправьте GET-запрос с параметром `userId`, равным `1`.
#
# 3. Распечатайте полученные записи.


url = "https://jsonplaceholder.typicode.com/posts"
data = {"userId" : 1}
response = requests.post(url, data=data)
print(response.status_code)
print(f"ответ- {response.json()}")