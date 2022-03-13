# Service: Identity
> ::Authentication server::



## Local setup guide
> Tested on Linux and MacOS only!
### Requirements
- [x] Python: **`v3.8.9`**
- [x] Pip3 package: **`virtualenv`**
- [x] Database: **`SQLite3`**



### Setup with `virtualenv`
```bash
# Create activate and install dependencies
$ virtualenv -p /usr/bin/python3 venv
$ source venv/bin/activate
$ pip install -U pip
$ pip install -r requirements.txt

# Migrate database and run the dev server
$ python manage.py migrate
$ python manage.py runserver
```



### Setup with `docker`
```bash
$ docker-compose up --build
```
