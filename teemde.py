from app import app, db
from app.models import User, Message, Emotion


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Message': Message, 'Emotion': Emotion}
