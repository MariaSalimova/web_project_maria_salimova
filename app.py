from flask import Flask
from data.db_session import global_init
app = Flask(__name__)
app.config['SECRET_KEY'] = 'искусство_должно_быть_свободным'
global_init('gallery.db')


@app.route('/')
def index():
    return "искусство должно быть свободным"


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')