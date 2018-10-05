docker-compose up db redis elasticsearch consul
curl --request PUT --data-binary @config.local.yml http://consul/v1/kv/kliento
./wait-for-it.sh db:5432 elasticsearch:9200 -- ./code/manage.py runserver 0.0.0.0:8000