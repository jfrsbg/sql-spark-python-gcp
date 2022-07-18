docker compose up -d

docker exec -i database mysql -u user -ppassword desafio_engenheiro < create_tables.sql

docker exec -i database mysql -u user -ppassword desafio_engenheiro < calculate.sql

docker exec -i database mysql -u user -ppassword desafio_engenheiro < drop.sql

sudo chown -R $USER:$USER $PWD