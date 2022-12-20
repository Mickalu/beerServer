# beerServer
Server use for beer app

## Run project
They are differents config possible with runserver. Indeed we need to separate the dev environnement and the product environnement.

All environnement are present in folder **Beer_server/config/django**.

### local environnement
For running the project in local environnement :

```
python manage.py runserver --settings Beer_server.config.django.local
```
## API

### Beers
Getting all beers, post and get
```
http://127.0.0.1:8000/data/get_all_beers/
```

