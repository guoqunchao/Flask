from flask import Flask,Response
# from werkzeug.wrappers import Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    resp = Response(response='HelloWorld!', status=200, content_type='text/html')
    return resp

if __name__ == '__main__':
    app.run(debug=True)