## Cinemax Notifications

[![python](https://img.shields.io/static/v1?label=python&message=3.8%20|%203.9%20|%203.10&color=informational)](https://github.com/temirovazat/cinemax-notifications/actions/workflows/main.yml)
[![dockerfile](https://img.shields.io/static/v1?label=dockerfile&message=published&color=2CB3E8)](https://hub.docker.com/search?q=temirovazat%2Fnotifications)
[![lint](https://img.shields.io/static/v1?label=lint&message=flake8%20|%20mypy&color=brightgreen)](https://github.com/temirovazat/cinemax-notifications/actions/workflows/main.yml)
[![code style](https://img.shields.io/static/v1?label=code%20style&message=WPS&color=orange)](https://wemake-python-styleguide.readthedocs.io/en/latest/)
[![platform](https://img.shields.io/static/v1?label=platform&message=linux%20|%20macos&color=inactive)](https://github.com/temirovazat/cinemax-notifications/actions/workflows/main.yml)

### **Description**

_The aim of this project is to implement a notification service for an online cinema. This has led to the development of a system composed of multiple microservices. The notification source is an API designed for receiving events using the [FastAPI](https://fastapi.tiangolo.com) framework. The process responsible for sending notifications (worker) is implemented using the stream processing library [Faust](https://faust.readthedocs.io). Communication between the API and the worker takes place through the message queue [Kafka](https://kafka.apache.org). To create manual notification dispatch, an admin panel based on the [Django](https://www.djangoproject.com) framework is used in conjunction with [Celery](https://docs.celeryq.dev) for sending periodic notifications (scheduler). The admin panel and scheduler interact with the PostgreSQL database in which notifications, their sending history, and execution frequency are stored._

### **Technologies**

```Python``` ```FastAPI``` ```Django``` ```Celery``` ```Faust``` ```Kafka``` ```PostgreSQL``` ```Redis``` ```NGINX``` ```Docker```

### **How to Run the Project:**

Clone the repository and navigate to the `/infra` directory:
```
git clone https://github.com/temirovazat/cinemax-notifications.git
```
```
cd cinemax-notifications/infra/
```

Create a `.env` file and add project settings:
```
nano .env
```
```
# PostgreSQL
POSTGRES_DB=notifications_database
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

# Kafka
KAFKA_HOST=kafka
KAFKA_PORT=9092

# Redis
REDIS_HOST=redis
REDIS_PORT=6379

# Django
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@mail.ru
DJANGO_SUPERUSER_PASSWORD=1234
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,[::1],django
DJANGO_SECRET_KEY=django-insecure-_o)z83b+i@jfjzbof_jn9#%dw*5q2yy3r6zzq-3azof#(vkf!#

# Microservices
EVENT_SOURCING_URL=fastapi:8000
ADMIN_URL=django:8000
```

Deploy and run the project in containers:
```
docker-compose up
```

Access the admin panel and use the login (admin) and password (1234):
```
http://127.0.0.1/notifications
```

The API documentation will be available at:
```
http://127.0.0.1/openapi
```