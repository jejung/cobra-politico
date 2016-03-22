#-*- coding: utf8 -*- 
import smtplib
from email.mime.text import MIMEText

if __name__ == '__main__':
    print "Gmail:" 
    from_mail = str(raw_input())
    print "Password (Caution! Password will be shown as typed)"
    password = str(raw_input())
    with open('text.txt', 'rb') as f:
        text = f.read()
    i = 1
    with open('emails.txt', 'rb') as f:
        for line in f.readlines():
            print '#' + str(i) + ': ' + line 
            i = i + 1
            name, email = line.split('=')
            name = name.split('(')[0] 
            full_text = 'Senhor(a) ' + name + ',\n\n' + text
            msg = MIMEText(full_text) 
            msg['Subject'] = u'Cobrança'
            msg['From'] = from_mail
            msg['To'] = email
            print "connecting to smtp.gmail.com:587"
            s = smtplib.SMTP('smtp.gmail.com:587')
            print "starting_tls"
            s.starttls()
            print "successfull"
            print "login"
            s.login(from_mail, password)
            print "OK"
            print "sending"
            print full_text
            s.sendmail(from_mail, [email], msg.as_string())
            print 'sent'
            print "exiting"
            s.quit()
