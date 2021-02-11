import os,sys,requests,json,time

b='\033[1;34m'
i='\033[1;32m'
c='\033[1;36m'
m='\033[1;31m'
u='\033[1;35m'
k='\033[1;33m'
p='\033[1;37m'
h='\033[1;90m'

def bahan2():

	kata("Ok Lanjut... MengIntall...")
	os.system("""
pkg update -y
pkg upgrade -y
pkg install git -y
npm cache clear
npm audit fix
""")



def bot():

	os.system("clear")
	kata2(f"""
		{c}[{k}VERSION {k}1.12{c}]
{m}[•]======================================[•]
{h}[•]01[•]~BabyBot	[ New ]		 [•]
{p}[•]02[•]~AnKer		[ New ]		 [•]
{h}[•]03[•]~AhfisJunianto  [ New ]		 [•]
{p}[•]04[•]~Segera Hadir.. [ New ] 	 [•]
{h}[•]05[•]~Segera Hadir.. [ New ]		 [•]
{m}[•]======================================[•]

{m}[•]======================================[•]
{c}		|BY MR.RISKY|
{m}[•]======================================[•]
""")

	kata(f"{c}Silahkan Pilih Bot Whatsapp Mau DiInstall.???")
	os.system("sleep 2")
	kon=input(f"{c}[•]{m}==={c}[•]{m}====={k}>>> {m}")
	if kon == "":
		kata(f"{m}Error...??? Anjinh...")
		os.system("sleep 2")
		bot()

	elif kon == "1":
		load()
		bahan2()
		os.system("""
pkg install git
https://github.com/Ramlan666/babybot
cd babybot
bash install.sh
node index.js
""")
	elif kon == "2":
		load()
		bahan2()
		os.system("""
git clone https://github.com/4NK3R-PRODUCT1ON/bot-wea-v2
cd bot-wea-v2
bash install.sh
node index.js
""")
	elif kon == "3":
		load()
		bahan2()
		os.system("""
git clone https://github.com/affisjunianto/botwasapv4
cd botwasapv4
bash install.sh
node index.js
""")

	else:
		kata(f"{m}Filed...Error..!!!")
		os.system("sleep 2")
		bot()


def load():
    for x in range(0,101):
        time.sleep(1./10)
        print(f"\r\033[1;97m[\033[1;96m!\033[1;97m]Loading...(\033[1;92m{x}\033[90m%\033[1;97m)", end="", flush=True)


def bahan():

	load()
	kata("Tunggu Hingga Selesai Anjing...")
	os.system("""
sleep 3
clear
pkg update
clear
pkg upgrade
clear
pkg install git
clear
pkg install python2
clear
pkg install python
clear
pkg install bash
clear
pkg install cowsay
clear
pkg install figlet
clear
pkg install pip
clear
pkg install toilet
clear
pkg install wget
clear
pkg install lolcat
clear
pip2 install requests mechanize tqdm
clear
cd Tool
""")



def kata(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./50)
def kata2(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0./100)

def halo():

	xxx=input(f"{c}[•]{m}====={c}[•]{m}======={c}]>>>> {k}")
	if xxx == "":
		kata(f"Jangan Kosong... Anjing....")
		kata2(f"Lu Mau Gw Santet Ha... Anjing....")
		os.system("sleep 2")


	elif xxx == "1":
		load()
		bahan()
		os.system("""
git clone https://github.com/TheMagizz/DarkPremium
cd DarkPremium
python2 DarkFB.py
""")

	elif xxx == "02":
		load()
		bahan()
		os.system("""
https://github.com/Dumai-991/SpamSms
cd SpamSms
python Halo.py
""")

	elif xxx == "03":
		load()
		bahan()
		os.system("""
https://github.com/Dumai-991/Update
cd Update
python2 Update.py
""")

	elif xxx == "04":
		load()
		bahan()
		os.system("""
https://github.com/Dumai-991/FreeSms
cd FreeSms
python free.py
""")

	elif xxx == "05":
		load()
		bahan()
		os.system("""
git clone https://github.com/BOT-033/Sensei
cd Sensei
chmod +x *
python2 main.py
""")

	elif xxx == "06":
		load()
		bahan()
		os.system("""
git clone https://github.com/Dumai-991/RajaCrack
cd RajaCrack
python2 King.py
""")


	elif xxx == "07":
		load()
		bahan()
		os.system("""
git clone https://github.com/evait-security/weeman.git
cd weeman
python2 weeman.py
""")
	elif xxx == "08":
		load()
		bahan()
		os.system("""
git clone https://github.com/gillang15/RATU_ERROR
cd RATU_ERROR
python2 RATU_ERROR.py
""")
	elif xxx == "09":
		load()
		bahan()
		os.system("""
git clone https://github.com/Dumai-991/Dark-Gold
cd Dark-Gold
python2 Dark.py
""")
	elif xxx == "10":
		load()
		bahan()
		os.system("""
git clone https://github.com/Dumai-991/RajaCrack
cd RajaCrack
python2 King.py
""")
	elif xxx == "11":
		load()
		bahan()
		os.system("""
git clone https://github.com/ROMI-AFRZL/Cfb
cd Cfb
python2 Cfb.pyc
""")
	elif xxx == "12":
		load()
		os.system("""
pkg install unstable-repo
pkg install metasploit
pkg install git
pkg install python
pkg install python2
pkg install wget
pkg install curl
pkg install nmap
pkg install ruby
pkg install bash
curl -LO raw.githubusercontent.com/Hax4us/Metasploit_termux/master/metasploit.sh
chmod 777 metasploit.sh
./metasploit.sh
cd metasploit-framework
bundle update --bundler
nsfconsole
""")
	elif xxx == "13":
		load()
		bahan()
		os.system("""
git clone https://github.com/P4HRUL/CRACKER
cd CRACKER
python2 CrackerPemula.py
""")
	elif xxx == "14":
		load()
		bahan()
		os.system("""
git clone https://github.com/P4HRU/CR4CK
cd CR4CK
python2 CRACK.py
""")
	elif xxx == "15":
		load()
		bahan()
		os.system("""
git clone https://github.com/Tech-abm/Fb-Mafia
cd Fb-Mafia
pip2 install mechanize
pip2 install requests
python2 Dark-Cloning.py
""")
	elif xxx == "16":
		load()
		bahan()
		os.system("""
pip2 install mechanize
pip2 install bs4
pip2 install requests
git clone https://github.com/ROMI-AFRZL/UNIS3X
cd UNIS3X
python2 KIYAY_.py
""")
	elif xxx == "17":
		load()
		bahan()
		os.system("""
pkg install git python2 bash
git clone  https://github.com/LimitQueenProject/empas-limit
cd empas-limit
bash empas
""")
	elif xxx == "18":
		load()
		bahan()
		os.system("""
https://github.com/DarknessCyberTeam/BAJINGANv6
cd BAJINGANv6
BAJINGAN.sh
""")
	elif xxx == "19":
		load()
		bahan()
		os.system("""
git clone https://github.com/dz-id/dmbf
cd dmbf
cythonize -i brute.c && rm brute.c
python run.py
""")
	elif xxx == "20":
		load()
		bahan()
		os.system("""
git clone https://github.com/Ha3MrX/Gemail-Hack
cd Gemail-Hack
chmod +x gemailhack.py
python gemailhack.py
""")
	elif xxx == "21":
		load()
		input(f"{c}Apakan Anda Yakin Mau Menginstall Bot~WhatsApp~ALL SERVER")
		kata("Anda Telah Masuk... KeBot~~~")
		os.system("sleep 2")
		bot()

	elif xxx == "22":
		load()
		bahan()
		os.system("""
git clone https://github.com/anggaxd/cfbid
cd cfbid
python2 crack.py
""")
	elif xxx == "23":
		load()
		bahan()
		os.system("""
git clone https://github.com/anggaxd/cfbid2
cd cfbid2
python2 run.py
""")
	elif xxx == "24":
		load()
		bahan()
		os.system("""
git clone https://github.com/Yayan-XD/MBF
cd MBF
bash setup.sh
""")
	elif xxx == "25":
		load()
		bahan()
		os.system("""
git clone https://github.com/Yayan-XD/Silent 
cd Silent
sh install.sh
python2 Silent.py
""")
	elif xxx == "26":
		load()
		bahan()
		os.system("""
git clone https://github.com/Yayan-XD/B2
cd B2
pip2 install mechanize
pip2 install requests
python2 bb-hacker.py
""")
	elif xxx == "27":
		load()
		bahan()
		os.system("""


""")
	elif xxx == "28":
		load()
		bahan()
		os.system("""


""")
	elif xxx == "29":
		load()
		bahan()
		os.system("""


""")
	elif xxx == "30":
		load()
		bahan()
		os.system("""


""")




	elif xxx == "88":
		os.system("xdg-open https://api.whatsapp.com/send/?phone=082384332714&text&app_absent=0")
		input(f"{m}Back~{p}Kembali")
		halo()

	elif xxx == "99":
		load()
		update()

	elif xxx == "00":
		os.system("xdg-open https://api.whatsapp.com/send/?phone=082384332714&text&app_absent=0")
		os.system("sleep 2")
		os.system("xdg-open https://chat.whatsapp.com/LwR9NQFlHUZ5KvzFdWjbyf")
		sys.exit(f"{k}Bye Bye Bye")

	else:
		kata(f"{c}Pilihan Anda Tidak TerDaftar....")
		os.system("sleep 2")
		input(f"{m}Back~{p}Kembali")
		halo()

def update():

	os.system("""
clear
cd $HOME
clear
rm -rf AllTools
git clone https://github.com/Dumai-991/AllTools
cd AllTools
python Mulai.py
""")






halo()
