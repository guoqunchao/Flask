from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HelloWorld!'

@app.route('/login/',methods=['Get','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return 'success'

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)