import requests
import configuration
import data

#POST‑запрос на регистрацию нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

#POST‑запрос на создание нового набора
def post_new_client_kit(kit_body, auth_token): # создание нового набора (kit_body) для авторизованного пользователя.
    # Формируем заголовки: копируем базовые и добавляем Authorization
    headers_with_token = data.headers.copy() # cоздаёт копию заголовков из data.headers, чтобы не изменять исходный словарь.
    headers_with_token["Authorization"] = f"Bearer {auth_token}"
    url = configuration.URL_SERVICE + configuration.CREATE_KIT_PATH # Формируем полный URL
    # Отправляем запрос
    return requests.post(
        url,
        json=kit_body, # тело в формате JSON
        headers=headers_with_token) # обновлённые заголовки с токеном

#Получение токена
#def get_new_user_token():
    response = post_new_user(data.user_body)
    return response.json().get("authToken")

#Создание набора
#def post_new_client_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,
                         headers={
                               "Authorization": "Bearer " + get_new_user_token()
                         })
