import smtplip
#smtp session
s=smtplib.SMTP("smtp.gmail.com",587)
#security
s.starttls()
s.login("razual53731@gmail.com","ryttyuu13234")#mymail ID
msg=input("enter your message here")
s.sendmail("razual53731@gamil.com","razual786@gmail.com",msg)
s.quit()
