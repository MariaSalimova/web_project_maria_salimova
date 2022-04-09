from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "искусство должно быть свободным"


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')