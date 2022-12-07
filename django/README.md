## DJANGO ONLY APP

### Features

- Users (clients and employees) moderation
- Online store
- Online menu
- Clients comments management
- REST API menu

### Deploy

#### 1. [Heroku](https://shelter-tigre.herokuapp.com/) (deprecated)

#### 2. Docker

Set environment variables or create .env in root, then compose up + build.

- PSQL_PASS = somePassword
- PSQL_USER = postgresUser
- PSQL_DB = DatabaseName
- DEBUG = False

```
docker-compose up -d --build
```