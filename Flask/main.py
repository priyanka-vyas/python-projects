from flask_mail import Mail, Message
from flask import Flask

app = Flask(__name__)
mail = Mail(app)


@app.route("/mail")
def email():
    msg = Message("hello Message", sender="priyankavyas2601@gmail.com", recipients="vyaspriyanka2601@gmail.com")
    mail.send(msg)
