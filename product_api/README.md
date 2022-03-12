# Service: Identity
> ::Resource server::



## Local setup guide
> Tested on Linux and MacOS
### Requirements
- [x] Python: **`v3.8.9`**
- [x] Pip3 package: **`virtualenv`**
- [x] Database: **`SQLite3`**


### Create activate and install dependencies
```shell
user@host[identity]: virtualenv -p /usr/bin/python3 venv
user@host[identity]: source venv/bin/activate
(venv) user@host[identity]: pip install -U pip
(venv) user@host[identity]: pip install -r requirements.txt
```

### Migrate database and run the dev server
```shell
(venv) user@host[identity]: python manage.py migrate
(venv) user@host[identity]: python manage.py runserver 8001
```
