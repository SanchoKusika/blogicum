# Blogikum

## How to Run:

### 1. Create a virtual environment (in the project root):

```sh
python -m venv venv
```

### 2. Activate the virtual environment (in the project root):

```sh
.\venv\Scripts\activate
```

### 3. Install dependencies (in the project root):

```sh
pip install -r requirements.txt
```

### 4. Apply migrations:

```sh
python manage.py migrate
```

### 5. Start the project:

```sh
python manage.py runserver
```

---

### Load data from db.json into the database:

```sh
python manage.py loaddata ../db.json
```
