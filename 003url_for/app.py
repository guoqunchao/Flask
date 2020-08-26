from flask import Flask,url_for

app = Flask(__name__)

'''
"url_for" 第一个参数为视图函数的名字的字符串，后面的参数就是传递给 "url"。
如果传递的参数之前在 "url" 中已经定义，那参数会被当成 "path" 的形式传递。 否则将以查询字符串方式传递。
'''

@app.route('/')
def hello_world():
    return url_for('list',id=1,page=2) # /post/list/1/?page=2

@app.route('/post/list/<id>/')
def list(id):
    return 'list'

@app.route('/detial/<id>/')
def detial(id):
    return 'detial;'

if __name__ == '__main__':
    app.run(debug=True)