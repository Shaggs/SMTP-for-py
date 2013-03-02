# A simple email program to send an email using python from any SMTP server.
# Ideas of use: auto email on program shutdown, SPAM (no dont do it), be creative
# Made by S.Rees 2013

import smtplib
fromaddr = 'Who the email is from'
toaddrs = 'Who the email is for'
msg = 'Place Message here'

#provide gmail user name and password
username = 'username'
password = 'password'

# functions to send an email
server = smtplib.SMTP('SMTP server address:Port number')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
