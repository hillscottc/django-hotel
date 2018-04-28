
u:admin
p:adminadmin


sudo docker-compose run web python manage.py migrate
sudo docker-compose run web python manage.py createsuperuser

docker-compose up
docker-compose up -d    (for background)

docker ps (list)

docker-compose exec web bash (terminal to container)