# Авиалинии «Высокое небо»

Платформа Авиалинии «Высокое небо» позволяет узнать сколько раз конкретный самолет приземляется в определенном аэропорту.

## Требования для установки

### ОС

Ubuntu LTS будет достаточно.

### Python

```
sudo apt-get install python3.6
```

### Pip

```
sudo apt-get install python3.6-pip
```

### Git

```
sudo apt-get install git
```

### Postgresql

```
sudo apt-get install postgresql
```

## Установка

### Клонирование репозитория

```
git clone https://github.com/ca5f1071560752cb57c591f7c5b777/site_high_sky.git
cd site_high_sky
```

### Установка зависимостей
```
pip3.6 install -r requirements.txt
```

### Проверочные данные

```

sudo -u postgres createuser site_high_sky
sudo -u postgres createdb site_high_sky
sudo -u postgres psql
psql=# alter user site_high_sky with encrypted password site_high_sky;
psql=# grant all privileges on database site_high_sky to site_high_sky;

python3.6 manage.py migrate
python3.6 manage.py loaddata airliners airports daysofweek routes
python3.6 manage.py loaddata relations
sudo -u postgres psql -f airlines/fixtures/arrival_count.sql
```



