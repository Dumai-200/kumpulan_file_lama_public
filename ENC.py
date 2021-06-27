############################################
#SC JANGAN DIPERJUAL BELIKAN :)
#SC PUNYA RISKY
#github : DUMAI-991
#facebook: fb.me/llovexnxx
#yt : Dumai+991
# 6283143565470
############################################
import os, base64, codecs, random
from sys import argv
from os import system
from time import ctime
import os, sys, zlib, base64, marshal, binascii, time, py_compile
from time import sleep as waktu
from random import randint
from os import system, name
from random import choice as pilih
from datetime import datetime
saat_ini = datetime.now()
tgl = saat_ini.strftime('%d')
bln = saat_ini.strftime('%m')
thn = saat_ini.strftime('%Y')
waktu_new = (tgl+"-"+bln+"-"+thn)
xnxx="\033[85m"
q="\033[00m"
h2="\033[40m"
b2="\033[44m"
c2="\033[46m"
i2="\033[42m"
u2="\033[45m"
m2="\033[41m"
p2="\033[47m"
k2="\033[43m"
b='\033[1;34m'
i='\033[1;32m'
c='\033[1;36m'
m='\033[1;31m'
u='\033[1;35m'
k='\033[1;33m'
p='\033[1;37m'
h='\033[1;90m'
k3="\033[43m\033[1;37m"
b3="\033[44m\033[1;37m"
m3="\033[41m\033[1;37m"
wa = ([i, q, b, m, xnxx, u, h,])
w = pilih(wa)
ttl = pilih(["#Jangan DiEdit Ngab Nanti Rusak :)","#Script DiEnclah Goblog Nanti LuRecoder :)","#Anak Kontol Biasanya Anak Reocder","#Kang Recoder Mau Lewat"])
os.system('git pull')
expired = ['10', '07', '2021']
buffer_size = 9999999
logo_exp=('Maaf Gan Logo Expired\nHubungi Admin Untuk DiPerbaiki :)\n'+i+'6283143565470')
logo_me = (c+""" _____            _____  _____  _____  _____ 
|   __| ___  ___ |  |  ||  |  ||     ||  _  |
|   __||   ||  _||  |  ||  |  ||-   -||   __|
|_____||_|_||___| \___/  \___/ |_____||__|"""+i+""">>"""+k+"""Version 2.1.1
"""+w+"""
[->FB : https://m.facebook.com/llovexnxx
[->YT : Dumai-991
[->GH : https://github.com/Dumai-991
[->WA : https://wa.me/6283143565470
[->TL : https://t.me/6283143565470""")
def kontol(ngaceng):
    for peli in ngaceng + '\n':
        sys.stdout.write(peli)
        sys.stdout.flush()
        time.sleep(random.random() * 0.01)
         
def login():
    global file, ppk, obf_note
    os.system('clear')
    kontol(logo_me)
    tanggal = thn + bln + tgl
    exp = expired[2] + expired[1] + expired[0]
    if tanggal >= exp:
        print (('\n').join(['' + logo_me + logo_exp]))
        sys.exit()
    else:
	main()

def main():
    global file, obf_note, sex
    file = raw_input(c+"\nMasukan Filenya : "+k)
    time.sleep(1)
    sex = ("ENC")
    note = (ttl)
    flag2 = "#Enc By Mr.Risky\n#Enc By Dumai-991\n"
    flag3 = '# WAKTU DIENC   : ' + waktu_new + '\n'
    flag4 = '# PESAN Owner   : Jangan DiEdit\n'
    flag5 = '# Text Tambahan : \n#\n#\n\n'
    flag0 = '#==========================>>>>> Mr.Risky\n'
    global obf_note
    obf_note = note + flag2  + flag0 + flag3 + flag4 + flag0 + flag5
    try:
        htr1 = open(file).read()
    except IOError:
        os.sys.exit('\033[1;31m Maaf Gan File Tidak DiTemukan :(')

    htr2 = file.replace('.py', '-Hasil.py')
    os.system('rm -rf '+htr2)
    htr2 = file.replace('.py', '-Hasil.py')
    htr3 = base64.b64encode(htr1)
    h1 = []
    h2 = []
    h3 = []
    h4 = ''
    h5 = ''
    for x in htr3:
        h1.append(ord(x))

    z = 0
    while 1:
        h2.append(h1[z])
        if z >= len(h1) / 2:
            break
        z += 1

    v = len(h1) / 2 + 1
    try:
        while 1:
            h3.append(h1[v])
            v += 1

    except IndexError:
        pass

    for s in h3:
        h4 += chr(s)

    htr4 = codecs.encode(h4, 'rot_13')
    h6 = open(htr2, 'w')
    h6.write(obf_note + '\nimport codecs,base64\n' + 'htr = ' + str(h2) + '\t\t\n' + "tahmid = '" + str(htr4) + "'\t\t\n")
    h6.write("pizza = '\\x72\\x6f\\x74\\x5f\\x31\\x33'\t\t\n")
    h6.write("mobile = codecs.decode(eval('\\x74\\x61\\x68\\x6d\\x69\\x64'), eval('\\x70\\x69\\x7a\\x7a\\x61'))\t\t\n")
    h6.write("donat = codecs.decode(eval('\\x74\\x61\\x68\\x6d\\x69\\x64'), eval('\\x70\\x69\\x7a\\x7a\\x61'))\t\t\n")
    h6.write("burger = base64.b64decode(''.join([chr(tech) for tech in htr])+eval('\\x6d\\x6f\\x62\\x69\\x6c\\x65'))\t\t\n")
    h6.write('eval(compile(eval("\\x62\\x75\\x72\\x67\\x65\\x72"),"<arya77>","exec"))\t\t\n')
    h6.write('eval(compile(eval("\x62\x75\x72\x67\x65\x72"),"<arya77>","exec"))')
    h6.close()
    kontol('\n\033[1;32m > File ' +k+file+i+ ' Ini Sudah DiEnc Menjadi ' + c + htr2)
if __name__ == '__main__':
    login()
#    if len(argv) >= 2:
 #       main(argv[1])
  #  else:
   #     os.sys.exit('\n\033[1;33m Caranya : ' + __file__ + ' <script>')
