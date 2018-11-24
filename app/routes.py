
from flask import jsonify, request

from app import app

import requests


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/chat/get_all_messages", methods=["GET", "POST"])
def get_all_messages():
    return jsonify({"data": "get_all_messages"})

@app.route("/chat/send_message/", methods=["POST"])
def send_message(uuid):
    print(uuid)
    return jsonify(request.get_json())

@app.route("/chat/")
def chat():
    resp = jsonify({})
    res = requests.post('http://localhost:5000/chat/send_message/1234', json={"author":"lalala", "data":"This is chat_msg_1"})
    if res.ok:
        resp= jsonify(res.json())

    return resp