import requests
from flask import jsonify, request

from app import app, db
from textblob import TextBlob
from app.models import User, Message

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/chat/get_all_messages", methods=["GET", "POST"])
def get_all_messages():
    return jsonify({"data": "get_all_messages"})

@app.route("/chat/send_message", methods=["POST"])
def send_message():
    response = request.get_json()
    status = {"status": "something is wrong!"}
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     response.headers['Access-Control-Allow-Headers'] = '*'
    if response['author'] != '':
        u = User.query.filter_by(username=response['author']).first_or_404()
        message = TextBlob(response['data']['text'])
        m = Message(client_id=u.id, text= response['data']['text'],
                    polarity = message.sentiment.polarity,
                    subjectivity = message.sentiment.subjectivity )

        db.session.add(m)
        db.session.commit()
        status['status'] = "OK"

    return jsonify(status)

@app.route("/chat/")
def chat():
    m = {}
    res = requests.post('http://localhost:5000/chat/send_message', json={"author":"lalala", "data":{"text": "Textblob is amazingly simple to use. What great fun!"}})
    res = requests.post('http://localhost:5000/chat/send_message', json={"author":"lalala", "data":{"text": "What an amazingly enjoyable experience!"}})
    u = User.query.filter_by(username='lalala').first_or_404()
    messages  = Message.query.filter_by(client_id=u.id).all()
    for message in messages:
        m[str(message.id)] = message.info()
    return jsonify(m)

# curl -X POST -H "Content-Type: application/json" -d "{"author":"lalala", "data":{"text": "What an amazingly enjoyable experience!"}}" http://localhost:5000/chat/send_message
# curl -X POST -H "Content-Type: application/json" -d "{\"author\":\"lalala\", \"data\":{\"text\": \"What an amazingly enjoyable experience!\"}}" http://localhost:5000/chat/send_message