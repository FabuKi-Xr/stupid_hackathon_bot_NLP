# from unicodedata import name

from flask import Flask,request,redirect, url_for
from bot import TranslateBot
# from requests import request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
        
    if request.method == 'POST':
        user = request.form['nm']
        
        return redirect(url_for('success'),name=user)
    return "Hello World:3"

@app.route('/test',methods=['POST','GET'])
def test():
    convert = ''
    if request.method == 'POST':
        # print("hi")
        data = request.get_json()
        msg = data.get('msg')
        # print(type(msg))

        # msg = request.form.get("msg")
        # print("Here : ",msg)
        convert = TranslateBot(msg).getMsg()
        return {"msg": convert},201

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)