# Author: Tharcisio Leone #
# Dataset: Send a Email #

## Send mail from your Gmail account using Python
# 0. Importing Libraries
# 1. Create MIME
# 2. Add sender, receiver address into the MIME
# 3. Add the mail title into the MIME
# 4. Attach the body into the MIME
# 5. Including additional variables necessary for the prediction
# 6. Displaing graphically the bike demand over the day


# 0. Importing Libraries
import smtplib
import email.message

def send_email():
    body_email = """
    <p>Parágrafo1</p>
    <p>Parágrafo2</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Python Script"
    msg['From'] = 'tharcisioleone@gmail.com'
    msg['To'] = 'tharcisio.leone@giga-hamburg.de'
    password = 'vevyobxeiugitayi' #
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email has been sent.')





send_email()

