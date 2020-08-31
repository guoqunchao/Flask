from flask import Flask
from werkzeug.routing import BaseConverter

'''
1.实现一个类，继承自 "BaseConveter"。
2.在自定义的类中，重写 "regex",也就是这个变量的正则表达式。
3.将自定义的类，映射到 "app.url_map.converters"
'''

app = Flask(__name__)

class TelephoneConveter(BaseConverter):
    regex = r'1[358]\d{9}'

class ListConveter(BaseConverter):
    def to_python(self, value):
        return value.split('+')
app.url_map.converters['tele'] = TelephoneConveter
app.url_map.converters['list'] = ListConveter

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/tele/<tele:tele>')
def tele(tele):
    return "您输入的手机号码为：%s" %tele

@app.route('/posts/<list:board>')
def posts(board):
    return "您请求的内容为：%s" %board

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)