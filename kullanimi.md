# leagueoftipster
leagueoftipster telegram bot

Nasıl Kurulur? (Termux Kullanınız):
$ pkg install git python -y
$ git clone https://github.com/muhammetbdl/leagueoftipster
$ cd leagueoftipster
$ chmod +x * && python3 setup.py
To Genrate User Data:
$ python3 scraper.py

(members.csv varsayılan olarak adı değiştirdiyseniz kullanın)
Toplanan Verilere Toplu SMS Gönderin
$ python3 smsbot.py members.csv [İsteğe bağlı]

Grubunuza kullanıcı ekleyin;
$ python3 adder.py

veya,
$ python3 add2group.py members.csv

Daha fazla yardıma ihtiyacın olursa : https://t.me/leagueoftipster
