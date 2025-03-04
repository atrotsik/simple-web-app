docker rm webapp
docker build . -t webapp
docker tag webapp cr.yandex/crppkeb0hbjp6i480150/webapp:latest
docker push cr.yandex/crppkeb0hbjp6i480150/webapp:latest
docker pull cr.yandex/crppkeb0hbjp6i480150/webapp:latest
docker run -it -p 80:5005 --name webapp cr.yandex/crppkeb0hbjp6i480150/webapp:latest
