from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return 'Здесь всё Ок! Но график синуса <a href="/sin/">дальше</a>.', 200

@app.route('/sin/')
def graph_sin():
    return render_template('sin.html')

@app.errorhandler(404)
def page_not_found(error):
    return 'Вы потерялись:( Но я вам   <a href="/">помогу</a>!', 404


if __name__ == '__main__':
    app.run()