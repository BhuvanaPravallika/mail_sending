import smtplib

email = input("sender email")
receiver_email = input("receiver email")

subject = input("subject")
message = input("message")

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login(email,"jqrg pcwk gzdz vsaw")

server.sendmail(email,receiver_email,text)

print("Email has has been sent to" + receiver_email)