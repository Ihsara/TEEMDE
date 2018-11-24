import requests
from flask import jsonify, request

from app import app, db
from textblob import TextBlob
from app.models import User, Message, Video

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/chat/get_all_messages", methods=["GET", "POST"])
def get_all_messages():
    m = []
    m_info={}
    messages  = Message.query.all()
    for message in messages:
        m_info['data'] = message.info()
        m_info['author'] = User.query.filter_by(id = message.client_id).first_or_404().username
        m_info['suggestions'] = ''
        m.append(m_info)
        m_info = {}
    return jsonify(m)

@app.route("/user/create", methods=["POST"])
def create_user():
    data = request.get_json()
    u = User(username = data["username"])
    db.session.add(u)
    db.session.commit()

    return jsonify({'status': 'User created!'})

@app.route("/chat/send_message", methods=["POST"])
def send_message():
    response = request.get_json()
    status = {"status": "something is wrong!"}

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

@app.route("/chat/", methods=["GET"])
def chat():
    '''
    Get all messages from all users. For now, hardcoding lalala
    '''
    m = {}
    m_info={}
    messages  = Message.query.all()
    for message in messages:
        u = User.query.filter_by(id= message.client_id).first_or_404()
        m_info['data'] = message.info()
        m_info['author'] = u.username
        m_info['suggestions'] = 'None as of now!!'
        m[str(message.id)] = m_info
        m_info = {}
    return jsonify(m)

@app.route("/chat/user/<int:uuid>", methods=["GET"])
def chat_get_one_user(uuid):
    '''
    Get all messages from one user.
    '''
    m = {}
    m_info = {}
    u = User.query.filter_by(id=uuid).first_or_404()
    messages  = Message.query.filter_by(client_id=u.id).all()
    for message in messages:
        m_info['data'] = message.info()
        m_info['author'] = u.username
        m_info['suggestions'] = 'None as of now!!'
        m[str(message.id)] = m_info
        m_info = {}
    return jsonify(m)

@app.route("/video/send_feelings", methods=["POST"])
def video_add_feelings():
    response = request.get_json()
    status = {"status": "something is wrong!"}

    if response['happiness'] != '' and response['angry'] != '':
        u = User.query.filter_by(username='customer').first_or_404()

        v = Video(client_id=u.id,happiness_level=response['happiness'],
                    angriness_level=response['angry'])

        db.session.add(v)
        db.session.commit()
        status['status'] = "OK"

    return jsonify(status)

@app.route("/video/get_feelings", methods=["GET"])
def video_get_feelings():
    feelings = Video.query.all()
    cooperate_feelings = []
    for each_time in feelings:
        cooperate_feelings.append(each_time.info())

    return jsonify(cooperate_feelings)

