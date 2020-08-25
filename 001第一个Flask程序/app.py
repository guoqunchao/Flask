from flask import Flask

'''
配置DEBUG模式的四种方法:
1. 在 "app.run()"中传递一个参数 "debug=True" 就可以自动开启 "DEBUG" 模式；
2. 给 "app.debug=True" 也可以开启 "DEBUG" 模式；
3. 通过配置参数的形式设置DEBUG模式；"app.config.update(DEBUG=True)";
4. 通过配置文件的形式设置DEBUG模式；"app.config.from_object(config)"; 
'''

# 创建一个Flask对象
app = Flask(__name__)

# @app.route是一个装饰器
@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)

