# django-hotel

## The Task
Your task is to implement the system that allows a configured level of overbooking. Level of overbooking indicates number of reservations that can be booked over the hotel
capacity. Consider a hotel with 100 rooms. If level of overbooking is set to 0%, we cannot make more than 100 reservations for a specific
date. If level of overbooking is set to 10%, we can create up to 110 reservations for a specific date.

Your application has to expose 2 REST API endpoints using Python Django framework:
1. For hotel configuration, where we can set number of rooms and overbooking level.
2. For making reservations supplying
  - Guest name and email
  - Arrival and departure dates  

When max number of reservations is reached, the second endpoint responds with an error.


## Installation and Usage
This app runs in a Docker environment. Docker Compose is used to manage two containers: Django/Web and PostgreSQL instances.

- If necessary, install <a href="https://docs.docker.com/install/">Docker</a> and <a href="https://docs.docker.com/compose/install/#install-compose">Docker Compose</a>.
- Clone the code from this github repository.
    ```bash
    git clone https://github.com/hillscottc/django-hotel
    ``` 
- From inside the django-hotel dir, 
    ```bash
    docker-compose up
    ```
- Once it's running, the website should be available at  
    <http://localhost:8000>  
*Some docker daemons run other than localhost...depends on the docker install.

- The db is managed with Django's admin interface at <http://localhost:8000/admin>  

    - Need `sudo docker-compose run web python manage.py migrate` to init the db?

    - Create an admin account.
    ```bash
    sudo docker-compose run web python manage.py createsuperuser
    ```

#### My random notes
- Run containers in the background: `docker-compose up -d`    
- Are they still running? `docker ps`
- Terminal to running container: `docker-compose exec web bash`
- One liners to stop / remove all Docker containers:
    ```bash
    docker stop $(docker ps -a -q)
    docker rm $(docker ps -a -q)
    ```
