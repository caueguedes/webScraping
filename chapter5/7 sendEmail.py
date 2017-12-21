import smtplib
from email.mime.text import MIMEText

smtp = smtplib.SMTP('smtp.live.com', 587)
smtp.starttls()

smtp.login('UserMail', 'Password')

msg = MIMEText(_text=
                     "corpo do email aqui"  
)
msg['Subject'] = "Conteudo do email"
msg['From'] = "Email From"
msg['To'] = "Email To"

smtp.sendmail(msg["From"], msg["To"], msg.as_string())
smtp.quit()

#========= Codigo utilizado no livro ============
# import smtplib
# from email.mime.text import MIMEText
#
# msg = MIMEText("The body of the email is here")
#
# msg['Subject'] = "An Email Alert"
# msg['From'] = "ryan@pythonscraping.com"
# msg['To'] = "ryan@pythonscraping.com"

# s = smtplib.SMTP('localhost')
# s.send_message(msg)
# s.quit()