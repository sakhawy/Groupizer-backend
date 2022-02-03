# How to setup
- Install `docker-compose` 
- Create the postgres database:
```postgresql
postgres=# CREATE DATABASE groupizer;
CREATE DATABASE
postgres=# CREATE USER groupizer WITH PASSWORD 'groupizer';
CREATE ROLE
postgres=# GRANT ALL PRIVILEGES ON DATABASE groupizer TO groupizer;    
GRANT
postgres=# 
```
- Create a `.env` file
- Populate it
```bash
# ./.env

DATABASE_NAME=groupizer
DATABASE_USER=groupizer
DATABASE_PASSWORD=groupizer
DATABASE_HOST=localhost
DATABASE_PORT=5432
```
- Run `docker-compose up --build`