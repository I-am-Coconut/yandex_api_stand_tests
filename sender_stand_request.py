import configuration
import requests
import data

#Этот код отправляет HTTP GET-запрос к заданному URL-адресу, который складывается 
#из базового адреса сервиса и пути к его документации, оба определены в модуле 
#конфигурации. Затем он выводит HTTP-статус код ответа от сервера, который указывает 
#на результат выполнения запроса.

# Определяем функцию get_docs, которая не принимает параметров
def get_docs():
    # Выполняем GET-запрос к URL, который складывается из базового URL-адреса сервиса
    # и пути к документации, заданных в модуле конфигурации
    # Функция возвращает объект ответа от сервера
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
# Вызываем функцию get_docs и сохраняем результат в переменную response
response = get_docs()

#logs - получение логов
# Определяем функцию get_logs, которая отправляет GET-запрос к серверу для получения логов
def get_logs():
    # Складываем базовый URL из конфигурационного файла и путь к основным логам,
    # чтобы сформировать полный URL для запроса.
    # Возвращает объект ответа, полученный от сервера после выполнения GET-запроса
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                        params={"count": 20})
# Вызываем функцию get_logs и сохраняем ответ сервера в переменную response
response = get_logs()

#get_users_table - доступ к таблице 
# Функция для получения данных из таблицы пользователей
def get_users_table():
    # Составление полного URL пути к данным таблицы пользователей
    # путем конкатенации базового URL сервиса и конечной точки таблицы пользователей
    # Возвращает объект ответа от сервера
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

# Выполнение функции и сохранение ответа в переменную response
response = get_users_table()

# Определение функции для отправки POST-запроса на поиск наборов по продуктам
def post_products_kits(products_ids):
    # Отправка POST-запроса с использованием URL из конфигурации, данных о продуктах и заголовков
    # Возвращается объект ответа, полученный от сервера
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids)  # Тело запроса содержит ID продуктов в формате JSON
# Вызов функции с передачей списка ID продуктов из файла data.py
response = post_products_kits(data.products_ids)

#post_new_user - создание токена
# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_USER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data
response = post_new_user(data.user_body)

#get_user_body - сохраняет текущее значение имени
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

