from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import configparser
import os, sys
import csv
import traceback
import time
import random

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

def banner():
    print(f"""
{re}M{cy}hammet{re}Telegram{cy}Mobil Bot
        """)

cpass = configparser.RawConfigParser()
cpass.read('config.data')

try:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    client = TelegramClient(phone, api_id, api_hash)
except KeyError:
    os.system('clear')
    banner()
    print("\033[91m[!] Please run \033[92mpython3 setup.py\033[91m first !!!\n")
    sys.exit(1)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    os.system('clear')
    banner()
    client.sign_in(phone, input(gr+'[+] Gönderilen kodu girin: '+re))
 
os.system('clear')
banner()
input_file = sys.argv[1]
users = []
with open(input_file, encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)
 
chats = []
last_date = None
chunk_size = 200
groups=[]
 
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)
 
for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue
 
print(gr+'[+] Üye eklemek için bir grup seçin: '+re)
i=0
for group in groups:
    print(str(i) + '- ' + group.title)
    i+=1
 
g_index = input(gr+"Bir Numara Girin: "+re)
target_group=groups[int(g_index)]
 
target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)
 
print(gr+"[1] Kullanıcıya göre üye ekle ID\n[2] Kullanıcı adına göre üye ekle ")
mode = int(input(gr+"Seçenek: "+re)) 
n = 0
 
for user in users:
    n += 1
    if n % 50 == 0:
	    time.sleep(900)
	    try:
	        print ("Ekleniyor {}".format(user['id']))
	        if mode == 1:
	            if user['username'] == "":
	                continue
	            user_to_add = client.get_input_entity(user['username'])
	        elif mode == 2:
	            user_to_add = InputPeerUser(user['id'], user['access_hash'])
	        else:
	            sys.exit(re+"[!] Geçersiz Mod Seçildi. Lütfen tekrar deneyin.")
	        client(InviteToChannelRequest(target_group_entity,[user_to_add]))
	        print(gr+"[+] 60-180 Saniye arasi bekleniyor...")
	        time.sleep(random.randrange(60, 180))
	    except PeerFloodError:
	        print(re+"[!] Telegram flood uyarısı. \n[!] Ekleme botu şimdilik durduruldu. \n[!] Bir süre sonra devam edecek.")
	    except UserPrivacyRestrictedError:
	        print(re+"[!] Kullanıcının gizlilik ayarları bunu yapmanıza izin vermiyor. Atlanıyor ...")
	    except:
	        traceback.print_exc()
	        print(re+"[!] Beklenmeyen Hata...")
	        continue
