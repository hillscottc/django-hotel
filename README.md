# django-hotel

## The Task
  [TASK_README](TASK_README.md)


## Installation
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
- (Some docker daemons run other than localhost...depends on the docker install.)

- `sudo docker-compose run web python manage.py migrate` to init the db.

- Create an admin account.
    ```bash
    sudo docker-compose run web python manage.py createsuperuser
    ```

    - The db is managed with Django's admin interface at <http://localhost:8000/admin>  

### Functionality
Basic functionality is provided by the [Django REST framework](http://www.django-rest-framework.org/)  
The system utility [httpie](https://github.com/jakubroztocil/httpie#installation) is used for these examples.

We can control the format of the response by adding a format suffix:
```bash
http http://127.0.0.1:8000/hotels.json  # JSON suffix
http http://127.0.0.1:8000/hotels.api   # Browsable API suffix
```

Browse the API in a web browser, by visiting <http://127.0.0.1:8000/hotels/>


## Testing
Run the automated unit tests with `python manage.py test`  
Additional endpoint testing with [httpie](https://github.com/jakubroztocil/httpie#installation):
```bash
http http://localhost:8000/api/hotels/
http http://localhost:8000/api/hotels/1/
http http://localhost:8000/api/hotels/1.json
http --json POST http://127.0.0.1:8000/api/reservations/ hotel=6 client_name='Jackson' res_date='2020-02-05'
http --json PUT http://127.0.0.1:8000/api/hotels/1/ name='Hotel 1' num_rooms=10 res_buffer=2
```
