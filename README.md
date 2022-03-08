# Django Docker Sample - Antonio's Assessment

## Antonio's "members" application:

- Added a RESTful API with the Django REST Framework.

- This version follows *Test-Driven Development* process.

- Tests: `pytest`

- Tests runs with coverage (`pytest-cov`)

- Code check for quality issues via linter `flake8`

- Code standard formatting: `black`, `isort`

- DataBase: `postgreSQL`

## Running the application in `Docker`

### 1. Build the image

```bash
docker-compose build
```

### 2. Run the containers

```bash
docker-compose up -d
```


### 3. Create a superuser account:

```bash
docker-compose exec app python manage.py createsuperuser
```

### 4. Check everything is running

- <http://localhost:8000/ping/>
- <http://localhost:8000/hello/>
- <http://localhost:8000/admin/>
- <http://localhost:8000/api/members/>
- <http://localhost:8000/api/members/3/>

### 5. Run the tests with coverage

Run all tests

```bash
docker-compose exec app pytest -p no:warnings --cov=.
```

Selecting Tests (models, serializers, views...)

```bash
docker-compose exec app pytest -k models -p no:warnings
```

### 6. Stop the containers

```bash
docker-compose stop
```

### 7. Bring down the containers

```bash
docker-compose down
```

---
---
