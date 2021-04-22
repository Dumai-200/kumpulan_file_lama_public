# Decompiled By RandiSr
# Github : https://github.com/RANDIOLOY
#coding: utf-8

import smtplib,getpass,sys,os
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart


h = "\33[0;32m"
hm = "\33[32;1m"
b = "\33[0;36m"
bm = "\33[36;1m"
m = "\33[31;1m"
mg = "\33[0;31m"
p = "\33[37;0m"
hit = "\33[30;1m"
o = "\33[33;1m"
km = "\33[1;33m"
k = "\33[0;33m"


os.system("clear")

fro="santuyaja019@gmail.com"
#fro="santuyaja019@gmail.com"
to=raw_input("Untuk "+ km +": " + p)
sub=raw_input("Judul pesan "+ km +": "+p)
bod=raw_input("Isi pesan "+ km +": " + p)
#pasw=getpass.getpass("Password email anda "+ km +": " + p)
pasw="xxx1233sd1"

msg = MIMEMultipart()
msg["From"] = fro 
msg["To"] = to
msg["Subject"] = sub
body = bod

try:
  msg.attach(MIMEText(body, "plain"))
  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(fro, pasw)
  text = msg.as_string()
  server.sendmail(fro, to, text)
  server.quit()
  print(hm+"Sukses mengirim email")
except:
  print(m+"Gagal mengirim email")
