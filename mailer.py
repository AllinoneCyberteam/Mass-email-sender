""" Bulk mailer script """

import json
import smtplib

EMAIL_LIST = []

with open("./CONFIG", "r") as file:
    CONFIG = json.loads(file.read())
file.close()


with open("./mailing_list.txt", "r") as file:
    while True:
        LINE = file.readline()
        if not LINE:
            break
        else:
            EMAIL_LIST.append(LINE.strip())
file.close()

MESSAGE = "SUBJECT: {} \n\n{}".format(CONFIG["subject"], CONFIG["message"])

EMAIL_SERVER = smtplib.SMTP_SSL("smtp.gmail.com", "465")
EMAIL_SERVER.login(CONFIG["email"], CONFIG["password"])
for email in EMAIL_LIST:
    EMAIL_SERVER.sendmail(CONFIG["email"], email, MESSAGE)


EMAIL_SERVER.quit()
