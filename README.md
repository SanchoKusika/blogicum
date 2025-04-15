# Блогикум

## Как запустить:

### 1. В корневой директории проекта создать виртуальное окружение:

```sh
python -m venv venv
```

### 2. Активировать виртуальное окружение, находясь в корневой директории:

```sh
source venv/Scripts/activate
```

### 3. Установка зависимостей (в корне проекта)

```sh
pip install -r requirements.txt
```

### 4. Выполнение миграции

```sh
python manage.py migrate
```

### 8. Запустить проект:

```sh
python manage.py runserver
```

---

### Загрузить данные из файла db.json в базу данных:

```sh
python manage.py loaddata ../db.json
```
