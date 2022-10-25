from flask import Flask
from flask_admin import Admin

app = Flask(__name__)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

# set flask_admin
admin = Admin(app, name='CTP', template_mode='bootstrap3')


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


if __name__ == '__main__':
    app.run()
