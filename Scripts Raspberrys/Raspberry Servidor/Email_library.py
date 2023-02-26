# -*- coding: utf-8 -*-
import smtplib  # import library to handle smtp protocol
from email.mime.multipart import (
    MIMEMultipart,
)  # importing MIMEMultipart for multiple email parts
from email.mime.text import MIMEText  # importing MIMEText for sending mail body
from email.mime.base import MIMEBase  # importing MIMEBase for sending attachments
from email import encoders  # importing encoders to encode attachments
import configparser  # importing configparser to read configuration ini file
import os  # importing os library

# Creates a ConfigParser object
config_obj = configparser.ConfigParser()

# Reads the configfile.ini file
config_obj.read("./configfile.ini")

# Extracts the "Email" section from the configuration file
Email_config = config_obj["Email"]

# Extracts the "body" value from the "Email" section
body = Email_config["body"]

# Extracts the "sender" value from the "Email" section
sender = Email_config["sender"]

# Extracts the "password" value from the "Email" section
password = Email_config["password"]

# Extracts the "receiver" value from the "Email" section
receiver = Email_config["receiver"]

# Extracts the "subject" value from the "Email" section
Subject = Email_config["subject"]


def setup():
    """
    This function initializes a MIMEMultipart message object and sets the sender, recipient, and subject of the email.
    It also attaches the plain text body of the email.
    """
    # Create a new email message object
    message = MIMEMultipart()
    # Assign the sender email address
    message["From"] = sender
    # Assign the receiver email address
    message["To"] = receiver
    # Assign the subject of the email
    message["Subject"] = Subject
    # Add the plain text body of the email
    message.attach(MIMEText(body, "plain"))
    return message


def attach_PDF(message):
    """
    This function attaches a pdf file to the message object.
    The pdf file is read from the config file with the name specified in the "PDF" key.
    """
    # Load config from the config file
    config_obj = configparser.ConfigParser()
    config_obj.read("./configfile.ini")
    Email_config = config_obj["Email"]
    # Get the PDF file name from the config
    pdfname = Email_config["PDF"]
    # Open the PDF file in binary mode
    binary_pdf = open(pdfname, "rb")
    # Create a MIMEBase object for the PDF file
    payload = MIMEBase("application", "octate-stream", Name=pdfname)
    # Set the payload of the object as the content of the PDF file
    payload.set_payload((binary_pdf).read())
    # Encode the payload in base64
    encoders.encode_base64(payload)
    # Add headers to the payload
    payload.add_header("Content-Decomposition", "attachment", filename=pdfname)
    # Attach the payload to the email message
    message.attach(payload)
    return message


def send_email(message):
    """
    This function attaches a pdf file to the message object.
    The pdf file is read from the config file with the name specified in the "PDF" key.
    """
    # Create a new SMTP session
    session = smtplib.SMTP("smtp.gmail.com", 587)
    # Start the session in Transport Layer Security (TLS) mode
    session.starttls()
    # Print a message to indicate session is being initiated
    print("Iniciant sesió")
    # Login to the email account
    session.login(sender, password)
    # Get the message as a string
    text = message.as_string()
    # Send the email
    session.sendmail(sender, receiver, text)
    # Close the session
    session.quit()
    # Print a message to indicate email was sent successfully
    print("Mail Sent")
