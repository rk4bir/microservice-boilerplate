FROM node:12.20.0

ENV APP_DIR /app/
WORKDIR /app
ENV PORT 3001


COPY .env /app/.env
COPY . .


RUN yarn install

EXPOSE 3001