# microservice-boilerplate
> Django based microservice architecture with Oauth2


## Overview of the Boilerplate

This is a Django-based microservice architecture that provides OAuth2 authentication and includes a product API. 
The architecture is containerized using Docker for easy deployment and scaling. The front-end uses Nuxt.js, 
allowing for a modular, decoupled system.

### Features:
- **OAuth2 Authentication**: Secure authentication with OAuth2 protocol.
- **Microservice Architecture**: Independent services (Identity Server, Product API).
- **Docker Support**: Easy containerization and deployment.
- **Nuxt.js Frontend**: Seamless front-end integration.

## Contributing
Feel free to open issues or submit PRs to improve the project!


## Demo
- [Authentication Server](./identity/)
- [Resource Server](./product_api/)
- [Client app: authorization-code type](./nuxt-client/)

https://user-images.githubusercontent.com/25036102/158018939-74d5fcd1-4186-4c98-8cfb-0342fef48e32.mp4

## Local setup guide
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

