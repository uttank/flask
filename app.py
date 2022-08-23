from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

admin = Admin(app, name='CTP', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))

# Add administrative views here


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'
