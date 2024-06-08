import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "knightkingram007@gmail.com"
password = "dladnbtwqagaggkd"

receiver = "knightkingram007@gmail.com"
message = """
Hi this is great.
Good connecting with you.
Hope to work together :)
"""
context = ssl.create_default_context()

with smtplib.SMTP_SSL(host,port,context=context) as server:
    server.login(username,password)
    server.sendmail(username, receiver, message )