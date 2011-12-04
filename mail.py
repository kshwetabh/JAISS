import smtplib
import string

subject = "Test mail using Python"
to = "kshwetabh@gmail.com"
frm = "kshwetabh@gmail.com"
text = "hello hello hello"
host = "mail.google.com"
body = string.join((
        "From: %s" % frm,
        "To: %s" % to,
        "Subject: %s" % subject,
        "",
        text
        ), "\r\n")

server = smtplib.SMTP(host)
server.sendmail(frm,to, body)
server.quit()