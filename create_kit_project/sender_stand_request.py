import requests
import configuration
import data

#POST‑запрос на регистрацию нового пользователя
def post_auth(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers)
response = post_auth(data.user_body)
print(response.status_code)

#POST‑запрос на создание нового набора
def post_new_client_kit(kit_body, auth_token): # создание нового набора (kit_body) для авторизованного пользователя.

    # Формируем заголовки: копируем базовые и добавляем Authorization
    headers_with_token = data.headers.copy() # cоздаёт копию заголовков из data.headers, чтобы не изменять исходный словарь.
    headers_with_token["Authorization"] = "Bearer {auth_token}"
    # Формируем полный URL
    url = configuration.URL_SERVICE + configuration.CREATE_KIT_PATH
    # Отправляем запрос
    return requests.post(
        url,
        json=kit_body, # тело в формате JSON
        headers=headers_with_token) # обновлённые заголовки с токеном