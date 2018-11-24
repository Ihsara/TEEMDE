# TEEMDE

Text sentiment detection

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

#### /chat/send_message/
Linux:
```
curl -X POST -H "Content-Type: application/json" -d "{"author":"customer", "data":{"text": "What an amazingly enjoyable experience!"}}" http://localhost:5000/chat/send_message
```

Windows:
```
curl -X POST -H "Content-Type: application/json" -d "{\"author\":\"customer\", \"data\":{\"text\": \"wonderful!!\"}}" http://localhost:5000/chat/send_message
curl -X POST -H "Content-Type: application/json" -d "{\"author\":\"support\", \"data\":{\"text\": \"As your service!\"}}" http://localhost:5000/chat/send_message
```

#### /chat/user/<int:uuid>

#### /create_user/
```
curl -X POST -H "Content-Type: application/json" -d "{\"username\":\"service\", \"age\":1500, \"gender\": \"apache\"}" http://localhost:5000/user/create
```