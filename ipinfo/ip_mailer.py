# Thanks to
__author__ = 'Cody Giles' # https://elinux.org/RPi_Email_IP_On_Boot_Debian
__license__ = "Creative Commons Attribution-ShareAlike 3.0 Unported License"

""" This script was tested on ubuntu. It depends on the tool 'hostname'. """

from subprocess import check_output
import smtplib
from email.mime.text import MIMEText
import datetime

# Account Information
to = 'someone@email.de' # Email to send to.
gmail_user = 'youremail@gmail.com' # Email to send from. (MUST BE GMAIL)
gmail_password = 'yourpassword' # Gmail password.
smtpserver = smtplib.SMTP('smtp.gmail.com', 587) # Server to use.

def get_hostname():
    """
    retrieves the current hostname
    """
    ips = check_output(['hostname',])
    return ips.strip()

def get_local_ip():
    """
    retrieves the current local ip and returns it as a string
    """
    ips = check_output(['hostname', '--all-ip-addresses'])
    return ips.split()

def generate_email_text(now, ip_adresses, hostname):
    """ Generates the email's message text """
    txt = 'Current IP of ' + hostname + ' is:\n'
    txt += now.strftime("%d.%m.%Y %H:%M:%S") + '\n'
    for ip in ip_adresses:
        txt += ip + '\n'
    return txt

def send_email(txt):
    """ sends the mail using the globally defined values """
    smtpserver.ehlo()  # Says 'hello' to the server
    smtpserver.starttls()  # Start TLS encryption
    smtpserver.ehlo()
    smtpserver.login(gmail_user, gmail_password)  # Log in to server

    # Creates the text, subject, 'from', and 'to' of the message.
    msg = MIMEText(txt)
    msg['Subject'] = 'Current IP'
    msg['From'] = gmail_user
    msg['To'] = to

    # Sends the message
    smtpserver.sendmail(gmail_user, [to], msg.as_string())
    # Closes the smtp server.
    smtpserver.quit() 

now = datetime.datetime.now()
ip_address = get_local_ip()
hostname = get_hostname()
txt = generate_email_text(now, ip_address, hostname)
send_email(txt)

print("Sent IP Info successfully")
