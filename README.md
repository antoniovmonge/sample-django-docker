# Django Docker Sample - Antonio's Assessment

## Antonio's "members" application:

- Added a RESTful API with the Django REST Framework.

- This version follows *Test-Driven Development* process.

- Tests: `pytest`

- Tests runs with coverage (`pytest-cov`)

- Code check for quality issues via linter. (`flake8`, `black`, `isort`)

- DataBase: `postgreSQL`

## Running the application in `Docker`

### 1. There is one file needed to populate the database (not added to github for security reasons - included in `.gitignore`)

This file should be stored inside the "app" directory.

    - members.json

### 2. Build the image

```bash
docker-compose build
```

### 3. Run the containers

```bash
docker-compose up -d
```

### 4. Seed the Database with the file `members.json` (this file is not included in the repository - I will send it via email)  

```bash
docker-compose exec members python manage.py loaddata members.json 
```

### 5. Create a superuser account:

```bash
docker-compose exec members python manage.py createsuperuser
```

### 6. Check everything is running

- <http://localhost:8009/ping/>
- <http://localhost:8009/hello/>
- <http://localhost:8009/admin/>
- <http://localhost:8009/api/members/>
- <http://localhost:8009/api/members/3/>

### 7. Run the tests with coverage

```bash
docker-compose exec members pytest -p no:warnings --cov=.
```

### 8. Lint

```bash
docker-compose exec members flake8 .
```

### 9. Run `Black` and `isort`

- Check options

```bash
docker-compose exec members black --exclude=migrations --check .
docker-compose exec members isort . --check-only
```

- Make code changes

```bash
docker-compose exec members black --exclude=migrations .
docker-compose exec members isort .
```

### 10. Stop the containers

```bash
docker-compose stop
```

### 11. Stop the containers

```bash
docker-compose down
```

---
---
