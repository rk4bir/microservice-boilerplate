FROM python:3.8.12

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# clean cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# copy project requirements and install dependencies
COPY ./requirements /app/requirements
COPY ./requirements.txt /app/requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt

# copy env file
COPY .env.dev /app/.env.dev

# copy identity/ to docker's app/
COPY . .

# Django starup commands
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput -v3
