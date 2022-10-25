from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)


if app.debug:
    admin = Admin(app, name='flask login', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db_session))
