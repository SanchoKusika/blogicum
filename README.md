# Блогикум

## Как запустить:

### 1. Cоздать виртуальное окружение (в корне проекта):

```sh
python -m venv venv
```

### 2. Активировать виртуальное окружение (в корне проекта):

```sh
.\venv\Scripts\activate
```

### 3. Установка зависимостей (в корне проекта):

```sh
pip install -r requirements.txt
```

### 4. Выполнение миграции:

```sh
python manage.py migrate
```

### 5. Запустить проект:

```sh
python manage.py runserver
```

---

### Загрузить данные из файла db.json в базу данных:

```sh
python manage.py loaddata ../db.json
```
