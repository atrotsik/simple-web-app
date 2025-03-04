# simple-web-app

## Преднастройка ВМ
* На ВМ в YC настороен докер,
* Пользователь в группе докер,
* Настроен авторизованный сервис Yandex Cloud CLI
* Создан приватный registry YC 

## Клонировать проект в домашнюю директорию пользователя.
```
git clone https://github.com/atrotsik/simple-web-app.git
cd simple-web-app
```

## Запустить скрипт билда имиджа и копирования в приватный registry YC
```
./build_start.sh
```

## Зайти на серсив по http, шаблон http://{public ip address} для запуска скриптов.
http://158.160.151.194

