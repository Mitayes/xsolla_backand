# Xsolla School 2021. Backend (тестовое задание)
  
# Назначение проекта
Проект подготовлен в рамках реализации задания из вступительного теста для курса **"Xsolla School 2021. Backend"**
  
# Использованные технологии
## Тестовый полигон  
Виртуальная машина на базе Virtualbox  
**Operating System**: Debian GNU/Linux 10 (buster)  
**Kernel**: Linux 4.19.0-13-amd64  
**Architecture**: x86-64  
  
## Разработка  
- Python версии 3.9.6 (3.8 должна подойти)
- PyCharm 2021.1.3 (Community Edition)
- Django==3.2.5
- django-filter==2.4.0
- djangorestframework==3.12.4
- gunicorn==20.1.0

## Эксплуатация
- git version 2.20.1
- Docker version 20.10.2, build 2291f61
- docker-compose version 1.25.3, build d4d1b42b

# Порядок развёртывания
## Развёртывание в Docker
1. Создаём папку, в которую будем клонировать репозиторий git  
`mkdir /home/xsolla_web`
2. Клонируем репозиторий  
`git clone https://github.com/Mitayes/xsolla_backand.git`
3. Собираем контейнер  
`docker-compose build`  
В этот момент может сругаться на версию `docker-compose`, указанную в файле `docker-compose.yml`. Терминал сам подскажет какая версия допустима для вашего docker-compose
>Either specify a supported version (e.g "2.2" or "3.3")
4. Редактируем конфигурационные файлы:  

**/.env.dev**  
  
Задаёт такие параметры как:
  - DEBUG - запуск сервера в режиме отладки (0 - нет, 1 - да)
  - SECRET_KEY - Здесь нужно указать без апосрофов и кавычек секретный ключ Django проекта
  - ALLOWED_HOSTS - Здесь нужно указать через пробел IP-адреса, с которых будет доступен веб-сервер (например: `localhost 192.168.1.2`)  
  
**/docker-compose.yml**  
  - version - версия docker-compose.yml (определяется версией docker-compose)
  - ports - порт, на котором web-сервер будет принимать запросы (слева от двоеточия указывается порт хоста). В моём случае прослушивается http порт 80
