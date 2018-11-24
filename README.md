"# TEEMDE"


This project uses [pipenv](https://github.com/Ihsara/TEEMDE.git)
### To run this project env
```sh

pipenv install

pipenv shell
```

### Run server:
#### Linux:
```shell
FLASK_APP=teemde.py
FLASS_ENV=development
flask run
```
#### Windows:
```shell
set FLASK_APP=teemde.py
set FLASK_ENV=development
flask run
```

### Init database:
```shell
flask db init
flask db migrate
flask db upgrade
```

### API endpoints:

### Message:

#### Test /chat/send_message/
Linux:
```
curl -X POST -H "Content-Type: application/json" -d "{"author":"lalala", "data":{"text": "What an amazingly enjoyable experience!"}}" http://localhost:5000/chat/send_message
```

Windows:
```
curl -X POST -H "Content-Type: application/json" -d "{\"author\":\"lalala\", \"data\":{\"text\": \"What an amazingly enjoyable experience!\"}}" http://localhost:5000/chat/send_message
```
