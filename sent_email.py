import smtplib, ssl


def sent_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "kunalrai67890@gmail.com"
    password = "stscldlqmfhcfgkf"

    receiver = "kunalrai67890@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

