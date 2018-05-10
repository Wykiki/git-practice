from flask import Flask, Blueprint
from flask import render_template

app = Flask(__name__)
app.config.from_object('config')

bp = Blueprint('profile', __name__,
               template_folder='template',
               static_folder='static')

app.register_blueprint(bp)


@app.route('/')
def main():
    return render_template("base.html")


if __name__ == '__main__':
    app.run()
