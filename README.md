# django-hotel

## The Task
Your friend is asking to help with hotel management. Hotel is at a good location, and a lot of
reservations are made. However, life is not simple, and quite a reasonable percent of booked
reservations gets canceled. As a result, hotel sometimes has too many vacant rooms.
Your friend has a brilliant idea: implement a reservations management system that allows some
overbooking, so even if some room is reserved by someone at a specific date, other people still
can book it. 

Level of overbooking indicates number of reservations that can be booked over the hotel
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

    - `sudo docker-compose run web python manage.py migrate` to init the db.

    - Create an admin account.
    ```bash
    sudo docker-compose run web python manage.py createsuperuser
    ```


### Functionality
Baisc functionality is provided by the [Django REST framework](http://www.django-rest-framework.org/)  
The system utility [httpie](https://github.com/jakubroztocil/httpie#installation) is used for these examples.

We can control the format of the response that we get back, either by using the Accept header:
```bash
http http://127.0.0.1:8000/hotels/ Accept:application/json  # Request JSON
http http://127.0.0.1:8000/hotels/ Accept:text/html         # Request HTML

```

Or by appending a format suffix:
```bash
http http://127.0.0.1:8000/hotels.json  # JSON suffix
http http://127.0.0.1:8000/hotels.api   # Browsable API suffix
```

Control the format of the request using the Content-Type header.  
To POST using JSON:
```bash
http --json POST http://127.0.0.1:8000/api/hotels/ name="Hotel Three" num_rooms=5
```

Browse the API in a web browser, by visiting <http://127.0.0.1:8000/hotels/>


## Testing
Using [httpie](https://github.com/jakubroztocil/httpie#installation).
```bash
http http://localhost:8000/api/hotels/
http http://localhost:8000/api/hotels/1/
http http://localhost:8000/api/hotels/1.json
http --json POST http://127.0.0.1:8000/api/reservations/ hotel=6 client_name='Jackson' res_date='2020-02-05'
```


#### Some random notes
- Run containers in the background: `docker-compose up -d`    
- Are they still running? `docker ps`
- Terminal to running container: `docker-compose exec web bash`
- One liners to stop / remove all Docker containers:
    ```bash
    docker stop $(docker ps -a -q)
    docker rm $(docker ps -a -q)
    ```
