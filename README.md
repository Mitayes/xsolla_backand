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
- 


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
В этот момент может сругаться на версию `docker-compose`, указанную в файле `docker-compose.yml`
