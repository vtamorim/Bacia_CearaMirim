import smtplib

smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.starttls()
smtp.login("vthero89@gmail.com", "quss nbgy esgp zucv")
print("Login OK")
smtp.quit()
