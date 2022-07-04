# Author: Tharcisio Leone #
# Dataset: Send a Email #

## Send mail from your Gmail account using Python
# 0. Importing Libraries
# 1. Adding body of email
# 2. Adding subject, and addresses of sender and receiver.
# 3. Including Login Credentials for sending the mail




# 0. Importing Libraries
import smtplib
import email.message

# 1. Adding body of email
def send_email():
    body_email = """
    <p>A test mail sent by Python. It has no attachment.</p>
    <p>Please delete it.</p>
    """

# 2. Adding title, and addresses of sender and receiver.
    msg = email.message.Message()
    msg['Subject'] = "Python Script"
    msg['From'] = 'tharcisioleone@gmail.com'
    msg['To'] = 'tharcisio.leone@giga-hamburg.de'
    password = 'vevyobxeiugitayi' #
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # 3. Including Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email has been sent.')



send_email()

