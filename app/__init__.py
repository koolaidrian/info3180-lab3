from flask import Flask
from flask_mail import Mail



app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '8029b16dfd470a'
app.config['MAIL_PASSWORD'] = '6875c257352f2d'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False


mail = Mail(app)

from app import views

SECRET_KEY = "Sup3r$3cretkey"

app.config['SECRET_KEY'] = SECRET_KEY
