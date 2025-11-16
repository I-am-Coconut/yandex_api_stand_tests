import pytest
import requests
import configuration
import data
import sender_stand_request

#Создания набора с заданным именем
def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

#Создаёт нового пользователя и возвращает токен авторизации
def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    assert response.status_code == 201
    auth_token = response.json()["authToken"]
    assert auth_token != ""
    return auth_token

#Позитивная проверка: ожидаем код 201 и совпадение поля name
def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    response_json = response.json()
    assert response_json["name"] == kit_body["name"]

#Негативная проверка: ожидаем код 400
def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

#Негативная проверка без параметра name ожидаем код 400
def negative_assert_no_name_parameter(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

#Тест 1: Допустимое количество символов (1)
def test_create_kit_1_char():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)

#Тест 2: Допустимое количество символов (511)
def test_create_kit_511_chars():
    name_511_char = "a" * 511
    kit_body = get_kit_body(name_511_char)
    positive_assert(kit_body)

#Тест 3: Количество символов меньше допустимого (0)
def test_create_kit_empty_name():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)


#Тест 4: Количество символов больше допустимого (512)  
def test_create_kit_512_chars():
    name_512_chars = "a" * 512
    kit_body = get_kit_body(name_512_chars)
    negative_assert_code_400(kit_body)

#Тест 5: Разрешены английские буквы
def test_create_kit_english_letters():
    kit_body = get_kit_body("QWErty")
    positive_assert(kit_body)

#Тест 6: Разрешены русские буквы
def test_create_kit_russian_letters():
    kit_body = get_kit_body("Александр")
    positive_assert(kit_body)

#Тест 7: Разрешены спецсимволы
def test_create_kit_special_chars():
    kit_body = get_kit_body("#№%@,")
    positive_assert(kit_body)

#Тест 8: Разрешены пробелы
def test_create_kit_spaces():
    kit_body = get_kit_body(" Человек и КО ")
    positive_assert(kit_body)

#Тест 9: Разрешены цифры
def test_create_kit_numbers():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

#Тест 10: Параметр не передан в запросе
def test_create_kit_no_name_get_error_response():
    current_kit_body_no_name = data.kit_body.copy()
    current_kit_body_no_name.pop("name")  # Удаляем поле name
    negative_assert_no_name_parameter(current_kit_body_no_name)

#Тест 11: Передан другой тип параметра (число)
def test_create_kit_number_as_name():
    kit_body = {"name": 123}
    negative_assert_code_400(kit_body)
