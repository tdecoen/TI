from flask import Flask
from flask_login import LoginManager
from os import urandom

app = Flask(__name__)

app.config['WTF_CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = urandom(24)

lm = LoginManager()
lm.init_app(app)
lm.login_view = "login"

from TI import views

if __name__=='__main__':
        port = int(os.environ.get('PORT', 80))
        app.run(host='10.33.58.15', port=port, debug=True)
