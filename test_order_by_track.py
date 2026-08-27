import configuration
import requests
def test_create_order_and_get_by_track():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json={
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
})
    track = response.json()["track"]
    response = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH, params={"t": track})
    assert response.status_code == 200