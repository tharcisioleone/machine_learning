# Author: Tharcisio Leone #
# Dataset: Send a Email #

## Maschine Learning using Linear Regression
# 0. Importing Libraries
# 1. Reading the data set from Kaggle data.
# 2. Showing the first five rows of the data sets.
# 3. Calculating the Mean Absolute Error
# 4. Putting MAE in relation to a basis prediction
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





enviar_email()

