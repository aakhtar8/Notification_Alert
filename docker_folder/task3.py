# this prgram will email notification to the user if the notification is related to him/her
def send_notification(receive_email: str, notification: str, subject = "New Notification\
    from University of Punjab"):
    import smtplib
    my_email = "ahmedsiddique95@outlook.com"
    # setting up smpt server for outlook microsoft account
    server = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    server.starttls()
    server.login(my_email, "aliraja786")
    # setting up email library
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    msg = MIMEMultipart()       # create a message
    # setup parameters of msg
    msg['From'] = my_email
    msg['To'] = receive_email
    msg['Subject'] = subject
    msg.attach(MIMEText(notification, "plain"))
    server.send_message(msg)
    server.quit()


