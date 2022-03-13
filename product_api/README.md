# Service: Product API
> ::Resource server::



## Local setup guide
> Tested on Linux and MacOS
### Requirements
- [x] Python: **`v3.8.9`**
- [x] Pip3 package: **`virtualenv`**
- [x] Database: **`SQLite3`**

### Setup with virtualenv
Create activate and install dependencies
```shell
user@host[product_api]: virtualenv -p /usr/bin/python3 venv
user@host[product_api]: source venv/bin/activate
(venv) user@host[product_api]: pip install -U pip
(venv) user@host[product_api]: pip install -r requirements.txt
```

Migrate database and run the dev server
```shell
(venv) user@host[product_api]: python manage.py migrate
(venv) user@host[product_api]: python manage.py runserver 8001
```
### Setup with docker
```shell
user@host[product_api]: docker-compose up --build
```
