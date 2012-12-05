from flask import Flask, render_template, request
from conf import conf
from flask_mail import Mail
from flask_mail import Message

app = Flask(__name__)
app.config.from_object(conf)
mailer = Mail(app)

@app.route('/mail', methods=['POST'])
def mail():
    field_message = request.form['field-message']
    field_recipients = [request.form['field-email']]
    msg = Message(field_message, sender=conf.DEFAULT_MAIL_SENDER, recipients=field_recipients)
    mailer.send(msg)
    return 'success'

@app.route('/')
@app.route('/<subpage>')
def home(subpage='home'):
    data = {'subpage': subpage}
    return render_template('main.html', data=data)

if __name__ == '__main__':
    app.run(host='localhost', debug=True)
