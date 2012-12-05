from flask import Flask, render_template, request
from conf import conf
from flask_mail import Mail
from flask_mail import Message
import multiprocessing

app = Flask(__name__)
app.config.from_object(conf)
mailer = Mail(app)

def send_email(msg, recips):
    msg = Message(msg, sender=conf.DEFAULT_MAIL_SENDER, recipients=recips)
    mailer.send(msg)

@app.route('/mail', methods=['POST'])
def mail():
    msg = request.form['field-message']
    recips = [request.form['field-email']]
    def send_email_wrapped():
        send_email(msg, recips)
    multiprocessing.Process(target=send_email_wrapped).start()
    return 'success: email sent'

@app.route('/')
@app.route('/<subpage>')
def home(subpage='home'):
    data = {'subpage': subpage}
    return render_template('main.html', data=data)

if __name__ == '__main__':
    app.run(host='localhost', debug=True)
