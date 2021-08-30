import smtplib
from email.mime.text import MIMEText

def send_email(customer,dealer,rating,comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'Add login here'
    password = 'Add password here'
    message = f'<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>'

    sender_mail = 'email1@example.com'    # Add original mails here
    receiver_mail = 'email2@example.com'

    msg = MIMEText(message, 'html')
    msg['Subject'] = "LOGO Feedback"
    msg['From'] = sender_mail
    msg['To'] = receiver_mail

    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login,password)
        server.sendmail(sender_mail,receiver_mail,msg.as_string())