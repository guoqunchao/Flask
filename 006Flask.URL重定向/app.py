from flask import Flask,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HelloWrold!'

@app.route('/login/',methods=['GET','POST'])
def login():
    return 'login page'

@app.route('/profile/',methods=['GET','POST'])
def profile():
    name = request.args.get('name')

    if not name:
        return redirect(url_for('login'),code=302)
    else:
        return name

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=80)
