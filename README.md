# microservice-boilerplate
> Django based microservice architecture with Oauth2


## Demo
- [Authentication Server](./identity/)
- [Resource Server](./product_api/)
- [Client app: authorization-code type](./nuxt-client/)

https://user-images.githubusercontent.com/25036102/158018939-74d5fcd1-4186-4c98-8cfb-0342fef48e32.mp4

### Local setup guide
#### Local setup guide (with virtualenv)
Setup and run development server of identity server
```bash
$ cd identity/
$ virtualenv -p /usr/bin/python3 venv
$ source venv/bin/activate
$ python manage.py migrate
$ python manage.py runserver 8000
```

Setup and run development server of products api
```bash
$ cd product_api/
$ virtualenv -p /usr/bin/python3 venv
$ source venv/bin/activate
$ python manage.py migrate
$ python manage.py runserver 8001
```

Setup and run development server of nuxt web client
```shell
$ cd nuxt-client/
$ yarn install
$ yarn dev
```

#### Local setup guide (with docker: separate services)
Setup and run development server of identity server
```bash
$ cd identity/
$ docker-compose up --build
```

Setup and run development server of products api
```bash
$ cd product_api/
$ docker-compose up --build
```

Setup and run development server of nuxt web client
```bash
$ cd nuxt-client/
$ docker-compose up --build
```


#### Local setup guide (with docker: all service together)
Run identity, products api and nuxt web client together
```bash
$ docker-compose up --build
```
