# HW.Flask.Docker
1 Вариант: приложение flask в контейнере обращается к БД на localhost

Создаем образ:

docker build --tag my-docker-flask:develop1.1 –f Dockerfile_flask .

Запускаем контейнер:

docker run --env-file ./HW.Docker.Flask2/Env/environment2.env --publish 8000:5000 --detach --name my-docker-flask-db-host my-docker-flask:develop1.1

Важно! Чтобы  контейнер увидел хост, точнее БД PostgresSQL на хосте из контейнера, нужно в приложении, которое запускаем в контейнере, прописывать PostgresSQL адрес так:
host.docker.internal или docker.for.mac.localhost (для OS) (не 127.0.0.1 и не localhost!)

Пример:
SQLALCHEMY_DATABASE_URI=postgresql://Seb:xxxxxx@host.docker.internal:5432/flask_hw


2 Вариант: приложение flask в контейнере обращается к БД на postgres в отдельном контейнере по сети

Использовал pg_dump/pg_restore для копирования в том volume свою БД Postgres, которая на локальном хосте находится.

1.	Запуск контейнера с БД postgresql с привязкой заранее созданного volume:

docker volume create --name postgres-data-volume -d local

Далее контейнер с БД запускаем. Сложил в postgres-data-volume БД c хоста локального: 

docker run --name my-postgres-hw -v postgres-data-volume:/var/lib/postgresql/data -e POSTGRES_PASSWORD=seb_user_postGR67 -e POSTGRES_USER=Seb -e POSTGRES_DB=flask_hw -d -p 5432:5432 postgres

2.	Создаем сеть:

docker network create flask_hw_network


3.	Подключаю к сети контейнер с БД:

docker network connect flask_hw_network my-postgres-hw

4.	Узнаю адрес контйнера через: 

docker network inspect flask_hw_network

5.	Запускаю  контейнер с flask: нужно указать IP-адрес контейнера с БД и вместо пользователя Seb указать postgres. Т.к. при первой устновке образа именно этот пользователь создается. Но пароль берем от Seb)))

docker run --env-file ./HW.Docker.Flask2/Env/environment5.env --publish 8000:5000 --detach --name my-docker-flask-db-cont my-docker-flask:develop1.1

6.	Подключаю к сети

docker network connect flask_hw_network my-docker-flask-db-cont

Все работает!!

