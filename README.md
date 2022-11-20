![workflow](https://github.com/1under-pressure1337/foodgram-project-react/actions/workflows/main.yml/badge.svg)

# О проекте

Cайт Foodgram, «Продуктовый помощник». На этом сервисе пользователи могут:
* публиковать рецепты,
* подписываться на публикации других пользователей,
* добавлять понравившиеся рецепты в список «Избранное»,
* скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд. 

Проект доступен по [адресу](http://51.250.20.80/)
Доступ в административную зону.
E-mail: sasha1337shinko@mail.ru
Password: Vfif1996!

# Технологии

Backend:

* Python
* Django
* Djnago REST framework
* Docker/Docker-compose
* Nginx
* Gunicorn

Frontend:

* JavaScript
* React

# Описание команд для запуска проекта


Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/1under-pressure1337/foodgram-project-react.git
```

```
cd yamdb_final
```
Перейти в директорию 'infra':

```
cd infra
```

Соберать контейнеры:

```
docker-compose up -d
```

Выполнить миграции

```
docker-compose exec web python manage.py migrate
```

Создать суперпользователя:

```
docker-compose exec web python manage.py createsuperuser
```

Собрать статику:

```
docker-compose exec web python manage.py collectstatic --no-input
```


## Автор

[Шинко Александр](https://github.com/1under-pressure1337)
