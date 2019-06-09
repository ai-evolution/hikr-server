### setup
```
virtualenv -p python3.5 .venv
.venv/bin/pip install -r requiremments.txt

createdb digital_br
psql digital_br -c "create extension postgis"
psql digital_br -c "create extension pgrouting"

createdb routing
psql digital_br -c "create extension postgis"
psql digital_br -c "create extension pgrouting"


.venv/bin/python manage.py migrate

# load data from OpenStreetMap
.venv/bin/python manage.py .venv/bin/python manage.py parse_osm map.osm
```

### example get objects near location by tags

```
GET http://127.0.0.1:8000/api/v1/attraction/?y=60.004532&x=30.43344&tag=125
```

### example get tags

```
GET http://127.0.0.1:8000/api/v1/tags/
```
