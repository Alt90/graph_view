from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Ок!', 200

@app.errorhandler(404)
def page_not_found(error):
    return 'Вы потерялись:( Но я вам   <a href="/">помогу</a>!', 404


if __name__ == '__main__':
    app.run()