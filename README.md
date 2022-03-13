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
```shell
user@host[microservice-boilerplate]: cd identity/
user@host[identity]: virtualenv -p /usr/bin/python3 venv
user@host[identity]: source venv/bin/activate
(venv) user@host[identity]: python manage.py migrate
(venv) user@host[identity]: python manage.py runserver 8000
```

Setup and run development server of products api
```shell
user@host[microservice-boilerplate]: cd product_api/
user@host[product_api]: virtualenv -p /usr/bin/python3 venv
user@host[product_api]: source venv/bin/activate
(venv) user@host[product_api]: python manage.py migrate
(venv) user@host[product_api]: python manage.py runserver 8001
```

Setup and run development server of nuxt web client
```shell
user@host[microservice-boilerplate]: cd nuxt-client/
user@host[nuxt-client]: yarn install
user@host[nuxt-client]: yarn dev
```

#### Local setup guide (with docker: separate services)
Setup and run development server of identity server
```shell
user@host[microservice-boilerplate]: cd identity/
user@host[identity]: docker-compose up --build
```

Setup and run development server of products api
```shell
user@host[microservice-boilerplate]: cd product_api/
user@host[product_api]: docker-compose up --build
```

Setup and run development server of nuxt web client
```shell
user@host[microservice-boilerplate]: cd nuxt-client/
user@host[nuxt-client]: docker-compose up --build
```


#### Local setup guide (with docker: all service together)
Run identity, products api and nuxt web client together
```shell
user@host[microservice-boilerplate]: docker-compose up --build
```
