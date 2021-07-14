# Образ на основе которого создаём контейнер
FROM python:3.9.6-alpine

# рабочая директория внутри проекта
WORKDIR /usr/src/xsolla

# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# устанавливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# копируем содержимое текущей папки в контейнер
COPY . .