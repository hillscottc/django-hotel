
u:admin
p:adminadmin


sudo docker-compose run web python manage.py migrate
sudo docker-compose run web python manage.py createsuperuser

docker-compose up
docker-compose up -d    (for background)

docker ps (list)

One liner to stop / remove all of Docker containers:
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

docker-compose exec web bash (terminal to container)



python manage.py makemigrations hotelapp
python manage.py migrate