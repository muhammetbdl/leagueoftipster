print ("\033[1;92m")
print ("░█▀█░█▀▄░█▀▄░█▀▀░█▀▄")
print ("░█▀█░█░█░█░█░█▀▀░█▀▄")
print ("░▀░▀░▀▀░░▀▀░░▀▀▀░▀░▀")
print ("")
print ("      by \033[1;95m@leagueoftipster")
print ("\033[1;92m")
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import traceback
import time
import random

api_id = 1655760   #Telegram API ID.
api_hash = '887513e49c5e3004ea92c0104403c4c3'   #API Hash
phone = '+17099076670'   #Telefon No.
client = TelegramClient(phone, api_id, api_hash)
async def main():
    await client.send_message('me', 'Merhaba !!!!!')


SLEEP_TIME_1 = 100
SLEEP_TIME_2 = 100
with client:
    client.loop.run_until_complete(main())
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('40779'))

users = []
with open(r"members.csv", encoding='UTF-8') as f:  #Dosya ismi giriniz.
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
groups = []

result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size,
    hash=0
))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue

print('Üye eklemek için bir grup seçin: ')
i = 0
for group in groups:
    print(str(i) + '- ' + group.title)
    i += 1

g_index = input("Bir Numara Girin: ")
target_group = groups[int(g_index)]

target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)

mode = int(input("Kullanıcı adına göre eklemek için 1 veya kimliğe göre eklemek için 2 girin: "))

n = 0

for user in users:
    n += 1
    if n % 80 == 0:
        time.sleep(60)
    try:
        print("Ekleniyor {}".format(user['id']))
        if mode == 1:
            if user['username'] == "":
                continue
            user_to_add = client.get_input_entity(user['username'])
        elif mode == 2:
            user_to_add = InputPeerUser(user['id'], user['access_hash'])
        else:
            sys.exit("Geçersiz Mod Seçildi. Lütfen Tekrar Deneyin.")
        client(InviteToChannelRequest(target_group_entity, [user_to_add]))
        print("60-180 Saniye arasi bekleniyor...")
        time.sleep(random.randrange(0, 5))
    except PeerFloodError:
        print("Telegram flood uyarısı. \n[!] Ekleme botu şimdilik durduruldu. \n[!] Bir süre sonra devam edecek.")
        print("Waiting {} seconds".format(SLEEP_TIME_2))
        time.sleep(SLEEP_TIME_2)
    except UserPrivacyRestrictedError:
        print("Kullanıcının gizlilik ayarları bunu yapmanıza izin vermiyor. Atlanıyor ...")
        print("Gizlilik İçeren Kullanıcı Atlandı!")
        time.sleep(random.randrange(0, 5))
    except:
        traceback.print_exc()
        print("Beklenmeyen Hata... ")
        continue
