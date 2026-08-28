# Алиса Шутова 46-я когорта. Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request

# Проверка, что созданный заказ можно получить по его треку
def test_create_order_and_get_by_track():
    # Создание заказа и сохранение его трека
    response = sender_stand_request.post_new_order(data.order_body)
    track = response.json()["track"]
    # Получение заказа по треку и проверка кода ответа
    response = sender_stand_request.get_order_by_track(track)
    assert response.status_code == 200