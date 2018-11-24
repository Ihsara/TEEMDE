from flask import Flask
from flask import jsonify, request
import requests


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/chat/get_all_messages", methods=["GET", "POST"])
def get_all_messages():
    return jsonify({"data": "get_all_messages"})

@app.route("/chat/send_message/<int:uuid>", methods=["GET", "POST"])
def send_message(uuid):
    print(uuid)
    return jsonify(request.get_json())

@app.route("/chat/")
def chat():
    res = requests.post('http://localhost:5000/chat/send_message/1234', json={"mytext":"lalala"})
    if res.ok:
        return jsonify(res.json())



if __name__ == '__main__':
    app.run(debug=True)
    res = requests.post('http://localhost:8000/chat/send_message/1234', json={"mytext":"lalala"})
    print(res)