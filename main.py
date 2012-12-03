from flask import Flask, render_template, request
from conf import conf
# from send_email import send_email
# from flask_mail import Mail
# from flask_mail import Message

app = Flask(__name__)
app.config.from_object(conf)
# mailer = Mail(app)

# @app.route('/mail', methods=['POST'])
# def mail():
    # from_address = request.form['field-email']
    # message = "Sender's email:\n{0}\n\nMessage:\n{1}".format(from_address, request.form['field-message'])
    # subject = 'Codeniche contact form email'
    # send_email(conf.EMAIL_USERNAME, conf.EMAIL_PASSWORD, from_address, conf.EMAIL_DESTINATION, message, subject)
    # msg = Message('Subject', recipients=['long.live.vim@gmail.com'])
    # msg.body = 'body of message'
    # mailer.send(msg)
    # return 'success'

@app.route('/')
@app.route('/<subpage>')
def home(subpage='home'):
    data = {'subpage': subpage}
    return render_template('main.html', data=data)

if __name__ == '__main__':
    app.run(host='localhost', debug=True)
