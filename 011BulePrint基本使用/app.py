from flask import Flask,Blueprint
from blueprints.user import user_bp
from blueprints.news import news_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(news_bp)

@app.route('/')
def hello_world():
    return 'hello_world!'

if __name__ == '__main__':
    app.run(debug=True)
