import smtplib
import time, datetime
import os # this Python app is Linux specific


# read credentials from the file
def read_credentials(filename):
    """Reads from a file."""
    with open(filename) as file_contents:
        credentials = file_contents.read().split(",")
        return credentials


def read_ip_addresses():
    lines = [line.rstrip("\n") for line in open("ip_addresses")] # https://stackoverflow.com/questions/3277503/in-python-how-do-i-read-a-file-line-by-line-into-a-list
    sortedlines = []
    for line in lines:
        sortedlines.append(line.split(","))
    return sortedlines


def send_email(name,ip):
    # read credentials
    # the credential files need to have one extra item in them to avoid the carriage return
    sender_credentials = read_credentials("credentials")
    recepient_credentials = read_credentials("recepient")

    # assign credentials for logging into gmail
    smtp_object = smtplib.SMTP("smtp.gmail.com",587) # from help with Python-Narrative-Journey from Udemy
    smtp_object.ehlo()
    smtp_object.starttls()
    sender_email = sender_credentials[0]
    sender_passwd = sender_credentials[1] # be sure to use the app password for gmail, or you will get errors
    recepient = recepient_credentials
    smtp_object.login(sender_email,sender_passwd)
    
    # compose email
    from_address = sender_email
    to_address = recepient
    subject = (name + " is down!")
    message = ("The logical address of the device is " + ip)
    msg = "Subject: "+subject+'\n'+message

    # send email
    smtp_object.sendmail(from_address,to_address,msg)


def ping_bulk(): # https://stackoverflow.com/questions/2953462/pinging-servers-in-python
    address_list = read_ip_addresses()
    for entry in address_list:
        response = os.system("ping -c 1 -w5 " + entry[1] + " > /dev/null 2>&1") # works on linux only
        if response == 0:
            pass
        else:
            send_email(entry[0],entry[1])

ping_bulk()