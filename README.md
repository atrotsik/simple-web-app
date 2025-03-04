# simple-web-app

## Преднастройка ВМ
* На VM в облеке настороен докер,
* пользователь в группе докер,
* авторизованные на облаке Яндекс сервис Yandex Cloud CLI
* Создан приватный registry YC 

## Склонировать проект в домашнюю директорию пользователя.
```
git clone https://github.com/atrotsik/simple-web-app.git
cd simple-web-app
```

## Запустить скрипт билда имиджа и копирования в приватны registry YC
```
./build_start.sh
```

## Зайти на серсив по http, шаблон http://{public ip address} для запуска скриптов.
http://158.160.151.194

