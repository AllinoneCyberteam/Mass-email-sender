""" Bulk mailer script """

import json
import smtplib
import time

EMAIL_LIST = []

# Read config file
with open("config.txt", "r") as file:
    CONFIG = json.loads(file.read())
file.close()

# Read mailing list and add it to EMAIL_LIST
with open("mailing_list.txt", "r") as file:
    while True:
        LINE = file.readline()
        if not LINE:
            break
        else:
            EMAIL_LIST.append(LINE.strip())
file.close()

# Construct the message to be sent.
MESSAGE = "SUBJECT: {} \n\n{}".format(CONFIG["subject"], CONFIG["message"])

# Open SMTP secure connection.
try:
    EMAIL_SERVER = smtplib.SMTP_SSL("smtp.gmail.com", "465")
except Exception as e:
    print("Error intializing SMTP server")
    print(str(e))


# Login
try:
    EMAIL_SERVER.login(CONFIG["email"], CONFIG["password"])
except SMTPAuthenticationError as e:
    print("Error during authentication")
    print(str(e))

# Send emails to emails in EMAIL_LIST in a loop
for email in EMAIL_LIST:
    try:
        EMAIL_SERVER.sendmail(CONFIG["email"], email, MESSAGE)
    except Exception as e:
        print("Could not send email to " + email)
    time.sleep(0.5)

# Quit SMTP server
EMAIL_SERVER.quit()
