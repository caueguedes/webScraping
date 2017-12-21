import smtplib
from email.mime.text import MIMEText
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time


def sendMail(user, password, subject, body):
    msg = MIMEText(_text=body)
    msg['Subject'] = subject
    msg['From'] = "Email From"
    msg['To'] = "Email To"

    s = smtplib.SMTP('smtp.live.com', 587)
    s.starttls()
    s.login(user, password)
    s.sendmail(msg["From"], msg["To"], msg.as_string())
    s.quit()


bsObj = BeautifulSoup(urlopen("http://isitchristmas.com/"), 'html.parser')

while bsObj.find("a", {"id": "answer"}).attrs['title'] == 'NO':
    print("It is not Christmas yet.")
    time.sleep(3600)
    bsObj = BeautifulSoup(urlopen("http://isitchristmas.com/"), 'html.parser')

sendMail('UserMail','Password',"It's Christmas!",
         "According to http://itischristmas.com, it is Christmas!")