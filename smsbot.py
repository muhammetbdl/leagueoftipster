from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
import configparser
import os, sys
import csv
import random
import time

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
yo="\033[1;33m"
SLEEP_TIME = 30

class main():

    def banner():
        
        print(f"""
{re}M{cy}hammet{re}Telegram{cy}Mobil Bot
            """)

    def send_sms():
        try:
            cpass = configparser.RawConfigParser()
            cpass.read('config.data')
            api_id = cpass['cred']['id']
            api_hash = cpass['cred']['hash']
            phone = cpass['cred']['phone']
        except KeyError:
            os.system('clear')
            main.banner()
            print("\033[91m[!] Lütfen başlatin \033[92mpython3 setup.py\033[91m first !!!\033[0m\n")
            sys.exit(1)

        client = TelegramClient(phone, api_id, api_hash)
         
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            os.system('clear')
            main.banner()
            client.sign_in(phone, input(gr+'[+] Gönderilen onay kodunu girin: '+re))
        
        os.system('clear')
        main.banner()
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
        print(gr+"[1] Kullanıcıya göre SMS gönder ID\n[2] Kullanıcı adıyla SMS gönder ")
        mode = int(input(gr+"Seçeneginiz: "+re))
         
        message = input(gr+"[+] Mesajınızı Girin: "+yo)
         
        for user in users:
            if mode == 2:
                if user['username'] == "":
                    continue
                receiver = client.get_input_entity(user['username'])
            elif mode == 1:
                receiver = InputPeerUser(user['id'],user['access_hash'])
            else:
                print(re+"[!] Geçersiz Mod. Çikiliyor ...")
                client.disconnect()
                sys.exit()
            try:
                print(gr+"[+] Mesaj Gönderiliyor:", user['name'])
                client.send_message(receiver, message.format(user['name']))
                print(gr+"[+] Bekleniyor {} saniye...".format(SLEEP_TIME))
                time.sleep(SLEEP_TIME)
            except PeerFloodError:
                print(re+"[!] Telegram flood uyarısı. \n[!] Ekleme botu şimdilik durduruldu. \n[!] Bir süre sonra devam edecek.")
                client.disconnect()
                sys.exit()
            except Exception as e:
                print(re+"[!] Hata:", e)
                print(re+"[!] Devam etmeye çalisiyorum ...")
                continue
        client.disconnect()
        print("Bitti. Tüm kullanıcılara mesaj gönderildi.")



main.send_sms()