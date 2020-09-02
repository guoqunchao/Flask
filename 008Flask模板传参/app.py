from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    context = {
        'username':'zhiliao',
        'password':'123456',
        'age':18,
        'children':{
            'name':'xiao a',
            'heigh':180,
        }
    }
    return render_template('index.html',**context)

if __name__ == '__main__':
    app.run(debug=True)