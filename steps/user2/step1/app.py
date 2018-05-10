from flask import Flask, Blueprint

app = Flask(__name__)
app.config.from_object('config')

bp = Blueprint('profile', __name__,
               template_folder='template',
               static_folder='static')

app.register_blueprint(bp)


@app.route('/')
def main():
    return 'Hello World !'


if __name__ == '__main__':
    app.run()
