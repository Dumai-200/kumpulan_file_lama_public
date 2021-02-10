import os,sys,requests,json,time

b='\033[1;34m'
i='\033[1;32m'
c='\033[1;36m'
m='\033[1;31m'
u='\033[1;35m'
k='\033[1;33m'
p='\033[1;37m'
h='\033[1;90m'


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

def clear():
    os.system("sleep 1;clear;reset")

def kata(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./50)
def kata2(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./101)
def load():
    for x in range(0,101):
        time.sleep(1./10)
        print(f"\r\033[1;97m[\033[1;96m!\033[1;97m]Loading...(\033[1;92m{x}\033[90m%\033[1;97m)", end="", flush=True)
def Wa():
       os.system("xdg-open https://api.whatsapp.com/send/?phone=%2B6282384332714&text&app_absent=0")
       sys.exit("\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91mExit\033[1;97m")
def baner():
    kata(f"""
                           {c}[ {k}AllTools {c}]
                           {c}[ {k}Version{i} 1.10 {c}]
{c}[{k}•{c}]{i}========================================================={c}[{k}•{c}]{m}
{p}░█████╗░██╗░░░░░██╗░░░░░{h}████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
{p}██╔══██╗██║░░░░░██║░░░░░{h}╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
{p}███████║██║░░░░░██║░░░░░{h}░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
{p}██╔══██║██║░░░░░██║░░░░░{h}░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
{p}██║░░██║███████╗███████╗{h}░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
{p}╚═╝░░╚═╝╚══════╝╚══════╝{h}░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░
{c}[{k}•{c}]{i}========================================================={c}[{k}•{c}]
[{k}•{c}]{h}Script By         : {c}Mr.Risky
[{k}•{c}]{h}Github            : {c}github.com/Dumai-991
[{k}•{c}]{h}WhatSapp          : {c}082384332714
[{k}•{c}]{h}Status            : {c}Work / BerKerja
{c}[{k}•{c}]{i}========================================================={c}[{k}•{c}]{m}
""")

def Add():

	os.system("mkdir Data")

def Hapus():

	os.system("rm -rf Data")

def git():

	os.system("""
clear
git clone https://github.com/Dumai-200/Config
clear
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
{m}[ 21 ]~Segera Hadir....			[  ????   ]
{m}[ 22 ]~Segera Hadir....			[  ????   ]
{m}[ 23 ]~Segera Hadir....			[  ????   ]
{m}[ 24 ]~Segera Hadir....			[  ????   ]
{m}[ 25 ]~Segera Hadir....			[  ????   ]
{h}[ -- ]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[  ----   ]
{p}[ 88 ]~Report Bug Script		[  Admin  ]
{h}[ 99 ]~Update Script			[  Wajib  ]
{p}[ 00 ]~Exit				[  Babi   ]
{h}[ -- ]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[  ----   ]
{k}Script Ini Akan Error Saat Admin Mau MengUpdate..
{b}Atau Menambah Script Atau Tools...
{c}[{k}•{c}]{i}========================================================={c}[{k}•{c}]
""")
def main():
     Add()
     clear()
     baner()
     menu()
     os.system("cd Config/Data;python Config.py")




git()
Hapus()
main()
