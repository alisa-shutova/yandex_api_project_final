import requests
import configuration

# Запрос на создание заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=order_body)

# Получение заказа по треку
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH, params={"t": track})