import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import configparser 
import os

config_obj = configparser.ConfigParser()
config_obj.read("./configfile.ini")
Email_config = config_obj["Email"]
body = Email_config["body"]
sender = Email_config["sender"]
password = Email_config["password"]
receiver = Email_config["receiver"]

def setup():
    
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'Grafana Report'
     
    message.attach(MIMEText(body, 'plain'))    
    return message
    
   
def attach_PDF(message):
    config_obj = configparser.ConfigParser()
    config_obj.read("./configfile.ini")
    Email_config = config_obj["Email"]
    pdfname = Email_config["PDF"]
    
    current_directory = os.getcwd()
    print(current_directory)
    contents = os.listdir(current_directory)
    print(contents)
    print(pdfname in contents)
    print(pdfname)
    binary_pdf = open(pdfname, 'rb')
    payload = MIMEBase('application', 'octate-stream', Name=pdfname)
    payload.set_payload((binary_pdf).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
    message.attach(payload)
    return message


def send_email(message):
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    print("Iniciant sesió") 
    session.login(sender, password)
     
    text = message.as_string()
    session.sendmail(sender, receiver, text)
    session.quit()
    print('Mail Sent')