from flask import Flask,render_template,request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def list():
    value = request.args.get('value')  #http://127.0.0.1:5000/?value=2020-09-02 21:50:12
    timeValue = datetime.strptime(value,"%Y-%m-%d %H:%M:%S")
    args = {
        'name':None,
        'createTime': timeValue
    }
    return render_template('index.html',**args)

@app.template_filter('timehandler')
def timeHandler(time):
    '''
    判断时间距离现在的时间：
    1.如果时间间隔小于60秒，显示为刚刚;
    2.如果时间间隔大于1分钟小于60分钟，显示为xx分钟前;
    3.如果时间间隔大于1小时小于24小时，显示为xx小时前;
    4.如果时间间隔大于1天小于30天，显示为xx天前;
    5.如果时间间隔大于1个月小于12个月，显示为xx个月前;
    6.否则就显示具体时间2020-02-02 02:00;
    '''

    if isinstance(time,datetime):
        now = datetime.now()
        timestamp = (now - time).total_seconds()
        if timestamp < 60:
            return '刚刚'
        elif timestamp >= 60 and timestamp < 60*60:
            minutes = timestamp / 60
            return '%s分钟前' %int(minutes)
        elif timestamp >= 60*60 and timestamp < 60*60*24:
            hours = timestamp / (60*60)
            return '%s小时前' %int(hours)
        elif timestamp >= 60*60*24 and timestamp <60*60*24*30:
            days = timestamp / (60*60*24)
            return '%s天前' %int(days)
        elif timestamp >= 60*60*24*30 and timestamp <60*60*24*30*12:
            months = timestamp / (60*60*24*30)
            return '%s月前' %int(months)
        else:
            return time.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return time

if __name__ == '__main__':
    app.run(debug=True)