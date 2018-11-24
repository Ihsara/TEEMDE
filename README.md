"# TEEMDE"


This project uses [pipenv](https://github.com/Ihsara/TEEMDE.git)
### To run this project env
```sh

pipenv install

pipenv shell
```

### Run server:
##### linux:
```sh
FLASK_APP=teemde.py
FLASS_ENV=development
flask run
```
##### windows:
```sh
set FLASK_APP=teemde.py
set FLASK_ENV=development
flask run
```

### Init database:
```
flask db init
flask db migrate
flask db upgrade
```

### API endpoints:

####Message:
