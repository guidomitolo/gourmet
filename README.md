## GOURMET

Django web-based app developped for the food business management.


### Features

- Users moderation
- Online store
- Online menu
- Clients comment management
- REST API menu

### Deploy

#### 1-  [Heroku](https://shelter-tigre.herokuapp.com/)

#### 2- Docker

Set environment variables or create .env in root, then compose up + build.

- PSQL_PASS = somePassword<br>
- PSQL_USER = postgresUser
- PSQL_HOST = localORanyHost
- PSQL_DB = DatabaseName

```
docker-compose up -d --build
```