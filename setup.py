import os, sys
import configparser
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
	os.system('clear')
	print(f"""
	{re}M{cy}hammet{re}Telegram{cy}Mobil Bot
	{re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐
	{re}╚═╗{cy}├┤  │ │ │├─┘
	{re}╚═╝{cy}└─┘ ┴ └─┘┴  
	""")
banner()
print(gr+"[+] Gereksinimler yükleniyor ...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
banner()
os.system("touch config.data")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input(gr+"[+] API ID Girin : "+re)
cpass.set('cred', 'id', xid)
xhash = input(gr+"[+] API Hash Girin : "+re)
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"[+] Telefon Numarasini Girin: "+re)
cpass.set('cred', 'phone', xphone)
setup = open('config.data', 'w')
cpass.write(setup)
setup.close()
print(gr+"[+] Kurulum tamamlandı!")
print(gr+"[+] Artık herhangi bir aracı çalıştırabilirsiniz!")
print("\033[92m[+] @leagueoftipster: \033[96mhttp://t.me/leagueoftipster\033[0m")
