import smtplib
import getpass

# read credentials from the file
def read_credentials(filename):
    """Reads from a file."""
    with open(filename) as file_contents:
        credentials = file_contents.read().split(',')
        return credentials

def send_email():
    # read credentials
    # the credential files need to have one extra item in them to avoid the carriage return
    sender_credentials = read_credentials("credentials")
    recepient_credentials = read_credentials("recepient")

    # assign credentials for logging into gmail
    smtp_object = smtplib.SMTP("smtp.gmail.com",587) # from help with Python-Narrative-Journey from Udemy
    smtp_object.ehlo()
    smtp_object.starttls()
    sender_email = sender_credentials[0]
    sender_passwd = sender_credentials[1] # be sure to use the app password for gmail
    recepient = recepient_credentials
    smtp_object.login(sender_email,sender_passwd)

    # compose email
    from_address = sender_email
    to_address = recepient
    subject = input("Enter the subject: ")
    message = input("Enter the message: ")
    msg = "Subject: "+subject+'\n'+message

    # send email
    smtp_object.sendmail(from_address,to_address,msg)

send_email()