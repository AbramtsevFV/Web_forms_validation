# Web_forms_validation #
## Запуск  ##
1) Сохраняем проект на локальный компьютер.
2) Запуск тестов:
```
docker-compose run form_test python manage.py test
```
3) Запуск приложения 
```
docker-compose up
```
Ссылка для проверки (можно отправить просто из браузера):
```
http://127.0.0.1:8000/api/template/?User_name=name&User_email=aq@aq.ru&User_phone=79188962231&User_date=28.07.2021
```
