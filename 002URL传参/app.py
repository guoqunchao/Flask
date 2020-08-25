from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/list/<article_id>')
def get_list(article_id):
    return "您请求的文章是：%s" %article_id

if __name__ == '__main__':
    app.run(debug=True)