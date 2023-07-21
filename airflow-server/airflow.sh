sudo apt update && apt-get update
sudo apt install -y docker
sudo apt install -y docker-compose
sudo docker-compose up -d
sudo docker-compose run -d airflow scheduler

