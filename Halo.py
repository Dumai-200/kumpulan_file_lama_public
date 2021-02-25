import os,sys,requests,json,time

b='\033[1;34m'
i='\033[1;32m'
c='\033[1;36m'
m='\033[1;31m'
u='\033[1;35m'
k='\033[1;33m'
p='\033[1;37m'
h='\033[1;90m'

def git():

	os.system("""
open-xdg https://m.facebook.com/risky.solihin.18
clear
git clone https://github.com/Dumai-200/Config
clear
""")




def halo():

	clear()
	kata2(f"{h}Sebelum Lanjut Apakah Anda Sudah Install Bahan...?")
	kata2(f"{p}Jika Sudah Jawab {k}Y")
	kata(f"{p}Jika Belum Jawab {k}N")
	asw=input(f"{c}[{k}•{c}]{m}===={c}[{k}•{c}]{m}====={c}]>>>> {c}")

	if asw == "":
		kata(f"{h}Jangan {p}Kosonglah Anjing....")
		os.system("sleep 2")

	elif asw == "y":
		kata(f"{c}Ok... Lanjut....")
		os.system("sleep 2")
		main()

	elif asw == "Y":
		kata(f"{c}Ok... Lanjut....")
		os.system("sleep 2")
		main()

	elif asw == "N":
		kata(f"{h}Bye{p} Bye{h} Bye")
		kata(f"{m}Hacker Pro.... {p}Salam Dari Dumai")
		bahan()
		halo()

	elif asw == "n":
		kata(f"{h}Bye{p} Bye{h} Bye")
		kata(f"{m}Hacker Pro.... {p}Salam Dari Dumai")
		bahan()
		halo()
	else:
		kata(f"{m}Soryy..... {p}Error.....")
		os.system("sleep 2")
		halo()

def enter():

	load()
	kata2(f"{k}Tekan Enter Untuk Lanjut...{m}KONTOL...")
	os.system("sleep 2")
	print("")
	input(f"{c}[{p} Next {k}>><<{p} Lanjut {c}]")

def b():

	os.system("clear")

def load():
        try:
                a = 50
                b = 0
                for c in range(a):
                        a -= 1
                        b += 1
                        sys.stdout.write(f"\r {i}Download {k}[{p}%s{h}%s{k}]{i} %s/%s"%("⋙"*b,"≡"*a,b,a)),;sys.stdout.flush()
                        time.sleep(0.3)
        except KeyboardInterrupt:
                sys.exit()

def load3():

	text = [f"{i}[>>>>             ] 35%","[>>>>>>>>>        ] 46%","[>>>>>>>>>>>>     ] 96%","[>>>>>>>>>>>>>>>>>] 100%"]
	for o in text + "\r":
		print("\r\033[1;91m[●] \033[1;92mLoading \033[1;97m"+o+"\r"),;sys.stdout.flush();time.sleep(1)
#	        print(f"\r\033[1;97m[\033[1;96m!\033[1;97m]Loading...(\033[1;92m"+o+"\033[90m%\033[1;97m)", time.sleep("10") , end="", flush=False)

def bahan():

	clear()
	os.system("""
pkg update -y
clear
pkg upgrade -y
clear
pkg install bash -y
clear
pkg install git -y
clear
pkg install python -y 
clear
pkg install cowsay -y
clear
pkg install figlet -y
clear
pkg install gem -y
clear
pkg install toilet -y
clear
cd $HOME
git clone https://github.com/Dumai-991/Update
clear
cd Update
clear
bash Install.sh
clear
cd $HOME
clear
""")

def welcome():

	kata3(f"""
{p}Assalamulaikum... Buat Kaum Islam...
{p}Salom Buat...  Kaum Kristen...

{c}Selamat Datang DiTools Ini... Tools Ini 100% Work...
Dan Tools Ini.. Akan Bertambah Setiap Kali... Anda MengUpdate...
Admin Sudah Menyiapkan Pilihan Update.. Pada Nomor [ 99 ]...
Jika Ada Masalah Terhadap Tools.. Silahkan Report Bug....

{k}~~~~~~~{i}Mr.Risky
{k}~~~~~~~{i}083143565470
""")
	os.system("sleep 3;clear")


def clear():
    os.system("sleep 1;clear;reset")

def kata(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./80)
def kata2(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./101)
def kata3(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./30)
def load2():
    for x in range(0,101):
        time.sleep(1./10)
        print(f"\r\033[1;97m[\033[1;96m!\033[1;97m]Loading...(\033[1;92m{x}\033[90m%\033[1;97m)", end="", flush=True)
def Wa():
       os.system("xdg-open https://api.whatsapp.com/send/?phone=%2B6283143565470&text&app_absent=0")
       sys.exit("\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91mExit\033[1;97m")
def baner():
    kata(f"""
{c}[ {i}VERSION {c}]{m}~~~{c}[  {i}INFO{c}  ]
{c}[  {k}1.12   {c}]{m}~~~{c}[ {k}Pindah{c} ]
{c}[  {k}20.1   {c}]{m}~~~{c}[ {k}Pindah{c} ]
{c}[  {k}23.9   {c}]{m}~~~{c}[ {k}Pindah{c} ]
{c}[  {k}26.8   {c}]{m}~~~{c}[  {m}End{c}   ]
{c}[  {k}????   {c}]{m}~~~{c}[ {m}??????{c} ]

{c}[{k}•{c}]{i}========================================================={c}[{k}•{c}]{m}
{h}░█████╗░██╗░░░░░██╗░░░░░{p}████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
{h}██╔══██╗██║░░░░░██║░░░░░{p}╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
{h}███████║██║░░░░░██║░░░░░{p}░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
{h}██╔══██║██║░░░░░██║░░░░░{p}░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
{h}██║░░██║███████╗███████╗{p}░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
{h}╚═╝░░╚═╝╚══════╝╚══════╝{p}░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░
{c}[{k}•{c}]{i}========================================================={c}[{k}•{c}]
[{k}•{c}]{h}Script By         : {c}Mr.Risky
[{k}•{c}]{h}Github            : {c}github.com/Dumai-991
[{k}•{c}]{h}WhatSapp          : {c}083143565470
[{k}•{c}]{h}Status            : {c}Work / BerKerja
{c}[{k}•{c}]{i}========================================================={c}[{k}•{c}]{m}
""")

def menu():

	kata2(f"""
{c}[{k}•{c}]{i}========================================================={c}[{k}•{c}]
{m}[ NO ]~~~~~~[ NAME SCRIPT ]~~~~~~~~~~~~~[ VERSION ]~~~~~~~~~
{h}[ 01 ]~Script Dark Fb                   [  12.1   ]
{p}[ 02 ]~Script SpamSms			[  00.0   ]
{h}[ 03 ]~Script Update Termux		[  15.5   ]
{p}[ 04 ]~Script FreeSms                   [  00.0   ]
{h}[ 05 ]~Script Sensai                    [  12.1   ]
{p}[ 06 ]~Script RajaCrack			[  12.1   ]
{h}[ 07 ]~Script Phising                   [  00.0   ]
{p}[ 08 ]~Script Ratu Error		[  10.1   ]
{h}[ 09 ]~Script Dark Gold			[  12.1   ]
{p}[ 10 ]~Script KingCrack			[  12.2   ]
{h}[ 11 ]~Script Crack All Negara          [  19.0   ]
{p}[ 12 ]~Script MetasPloit		[  12.1   ]
{h}[ 13 ]~Script Crack Pemula		[  12.7   ]
{p}[ 14 ]~Script CR4CK			[  12.9   ]
{h}[ 15 ]~Script Fb Mafia			[  17.0   ]
{p}[ 16 ]~Script UNIS3X			[  00.0   ]
{h}[ 17 ]~Script Empas MonToon		[  20.0   ]
{p}[ 18 ]~Script Bajingan			[  00.6   ]
{h}[ 19 ]~Script DmBf			[  12.1   ]
{p}[ 20 ]~Script Hack Gmail		[  12.9   ]
{h}[ 21 ]~Script Bot~WhatsApp~New		[  ????   ]
{p}[ 22 ]~Script CFBID			[  12.0   ]
{h}[ 23 ]~Script CFBID2			[  13.1   ]
{p}[ 24 ]~Script MBF 			[  12.1   ]
{h}[ 25 ]~Script B2			[  19.9   ]
{p}[ 26 ]~Script Silet			[  23.0   ]
{h}[ 27 ]~Script Hack CCTV			[  19.0   ]
{p}[ 28 ]~Script Virus Hp			[  6.12   ]
{h}[ 29 ]~Script Cek Ip Me			[  15.5   ]
{p}[ 30 ]~Script BotChat			[  4.0    ]
{h}[ 31 ]~Script Scan IP Web		[  2.0    ]
{p}[ 32 ]~Script EncPytHon			[  22.0   ]
{h}[ 33 ]~Script Lacak IP			[  12.0   ]
{p}[ 34 ]~Script MrTamfanSpam		[  19.9   ]
{h}[ 35 ]~Script Prem     			[  12.1   ]
{p}[ 36 ]~Script Treker Fb			[  11.1   ]
{h}[ 37 ]~Script Hack IG			[  0.00   ]
{p}[ 38 ]~Script DarkFB New		[  0.00   ]
{h}[ 39 ]~Script BRUTEFERONCEnew		[  0.00   ]
{p}[ 40 ]~Script LiteSpam			[  0.00   ]
{h}[ 41 ]~Script VirusAll			[  34.6   ]
{p}[ 42 ]~Script Mempercatikan Termux	[  20.9   ]
{h}[ 43 ]~Script HxWhatsapp		[  00.0   ]
{p}[ 44 ]~Script Trojans			[  10.1   ]
{h}[ 45 ]~Script Dompile (Enc) 		[  12.1   ]
{p}[ 46 ]~Script Cracker 			[  23.0   ]
{h}[ 47 ]~Script DarkFb			[  00.0   ]
{p}[ 48 ]~Script SpamSMS			[  00.0   ]
{h}[ 49 ]~Script DeathHacker :V		[  10.5   ]
{p}[ 50 ]~Script CLAY (Hasil Recode)	[  19.1   ]
{h}[ -- ]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[  ----   ]
{p}[ 88 ]~Report Bug Script		[  Admin  ]
{h}[ 99 ]~Update Script			[  Wajib  ]
{p}[ 00 ]~Exit				[  Babi   ]
{h}[ -- ]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[  ----   ]
{c}[{k}•{c}]{i}========================================================={c}[{k}•{c}]
"""),;kata3(f"""
{k}Script Ini Akan Error Saat Admin Mau MengUpdate..
{c}Atau Menambah Script Atau Tools...
{k}Wajib Install Bahan Dulu Bro... Kolo Tidak Diakan Rusak...
{c}TOOLS INI 100% WORK... Pilih ,[ 88 ] Untuk Report Bugs Atau..
{k}Terjadi Kesalahan Terhadap Script...
""")
#{}[ 30 ]~Script 			[     ]
#???
#???
#???


def main():
     clear()
     baner()
     menu()
     os.system("cd Config/Data;python Config.py")


b()
load()
git()
main()
