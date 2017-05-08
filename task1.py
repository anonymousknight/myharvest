
from flask import Flask, redirect, url_for, request
from flask_mail import Mail, Message
app = Flask(__name__)


mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'myharvestindia@gmail.com'
app.config['MAIL_PASSWORD'] = '*******'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/mail/<name>/<email>/<username>")
def success(name,email,username):
   msg = Message('Hello', sender = 'myharvestindia@gmail.com', recipients = ['archustalin@gmail.com'])
   msg.body = "Name:{},Email:{},Username:{}".format(name,email,username)
   mail.send(msg)
   return "Sent"

@app.route('/task1',methods = ['POST', 'GET'])
def login():
        print('in')
        if request.method == 'POST':
                user,email,username = request.form['name'],request.form['email'],request.form['username']
                return redirect(url_for('success',name = user,email = email,username = username))
        else:
                user = request.args.get('name','email','username')
                return redirect(url_for('success',name = user,email = email,username = username))

        

if __name__ == '__main__':
   app.run(debug = True)

