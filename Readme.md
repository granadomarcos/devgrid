
### Basics

1. Activate a virtualenv
2. Install the requirements

### Set Environment Variables

Update *project/server/config.py*, and then run:

```sh
$ export APP_SETTINGS="project.server.config.DevelopmentConfig"
```

or

```sh
$ export APP_SETTINGS="project.server.config.ProductionConfig"
```

Set a SECRET_KEY:

```sh
$ export SECRET_KEY="change_me"
```

### Create DB

Create the databases in `psql`:

```sh
$ psql
# create database user_weather
```

Create the tables and run the migrations:

```sh
$ python app.py create_db
$ python app.py db init
$ python app.py db migrate
```

### Run the Application

```sh
$ python app.py runserver or CTRL+F5
```

Access the application at the address [http://localhost:8080/]

> Want to specify a different port?

> ```sh
> $ python manage.py runserver -h 0.0.0.0 -p 8080
> ```

### Testing

Not implemented

### Authentication

Not implemented

### Dockerfile

Not implemented


