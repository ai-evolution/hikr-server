### setup
```
createdb digital_br
psql digital_br -c "create extension postgis"
psql digital_br -c "create extension pgrouting"

createdb routing
psql digital_br -c "create extension postgis"
psql digital_br -c "create extension pgrouting"

pip install -r requiremments.txt
```

### example get objects near location by tags

```
GET http://127.0.0.1:8000/api/v1/attraction/?y=60.004532&x=30.43344&tag=125
```
