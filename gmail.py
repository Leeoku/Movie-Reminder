import ezgmail, os, smtplib

gmail_user = *
gmail_pass = *
to_address = *
from_address = *

ezgmail.init(tokenFile='/home/admin/Projects/Movie-Recording-Reminder/token.json', credentialsFile='/home/admin/Projects/Movie-Recording-Reminder/credentials.json')
try:
    smtpObj=smtplib.SMTP('smtp.gmail.com',587)
    smtpObj.ehlo()
    smtpObj.starttls()
except:
    print('something went wrong')

smtpObj.login(gmail_user, gmail_pass)