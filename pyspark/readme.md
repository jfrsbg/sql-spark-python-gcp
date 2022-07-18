docker build -t pyspark .
docker-compose run --rm spark

depois de rodar os jobs
sudo chown -R $USER:$USER $PWD