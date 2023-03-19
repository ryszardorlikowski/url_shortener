# URL Shortener

Features:

- creating a shortened link
- retrieving a shortened link
- redirecting to the target page

## Local project launch

Setting environment variables in the project using a method that copies variables from the **.env.example** file to
the **.env**
file.

```
make setup-project
```

Launching the project using docker-compose.

```
docker-compose up
```

## Running tests

After launching the project using docker-compose, to run tests you need to execute the following command.

```
make run-tests
```