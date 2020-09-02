from flask import Flask,Response,make_response,jsonify,json
# from werkzeug.wrappers import Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    resp = Response(response='HelloWorld!', status=200, content_type='text/html')
    return resp

@app.route('/getJson/')
def getJson():
    dict = {
        "username":"qianxun",
        "password":"123456",
    }
    # 方法1
    return jsonify(dict)

    # 方法2
    # resp = Response(json.dumps(dict),content_type='application/json')
    # return resp

    # 方法3
    # resp = make_response(jsonify(dict),200)
    # return resp
if __name__ == '__main__':
    app.run(debug=True)
