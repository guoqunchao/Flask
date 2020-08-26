from flask import Flask,request
import uuid

app = Flask(__name__)

print(uuid.uuid4())

'''
接受用户传递的请求:
第一种：使用path的形式（将参数嵌入到路径中）；
第二种：使用查询字符串的方式，就是通过 "?key=value" 的形式传递；
'''

'''
第一种:路径传递

int:id 指定传参数据类型
string: 默认的数据类型，接受没有任何斜杠 "\/" 的文本；
int: 接受整型;
float: 接受浮点类型;
path: 和string类似，但是接受斜杠;
uuid: 只接受uuid字符串;
any: 可以指定多种路径;
'''

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/sstring/<id>')
def type_string(id):
    # http://127.0.0.1:5000/sstring/1asdafqe1qsd
    return "您请求的内容为：%s" %id

@app.route('/iint/<int:id>')
def type_int(id):
    # http://127.0.0.1:5000/iint/1234324
    return "您请求的内容为：%s" %id

@app.route('/ffloat/<float:id>')
def type_float(id):
    # http://127.0.0.1:5000/ffloat/0.1234324
    return "您请求的内容为：%s" %id

@app.route('/ppath/<path:id>')
def type_path(id):
    # http://127.0.0.1:5000/ppath/a12/b34/c56
    return "您请求的内容为：%s" %id

@app.route('/uuuid/<uuid:id>')
def type_uuid(id):
    # http://127.0.0.1:5000/uuuid/e42db6e6-f14b-48eb-bfc9-f9e0aa7f3eeb
    return "您请求的内容为：%s" %id

@app.route('/<any(blog,bbs):url_path>/<id>')
def type_any(url_path,id):

    return "您请求的路径为：%s  id为:%s" %(url_path,id)


'''
第二种：使用查询字符串方式
'''
# 通过?号的形式传递参数
@app.route('/d')
def d():
    wd = request.args.get('wd')
    ie = request.args.get('ie')
    return "您通过查询字符串的方式传递参数为 %s %s" %(wd,ie)



if __name__ == '__main__':
    app.run(debug=True)


