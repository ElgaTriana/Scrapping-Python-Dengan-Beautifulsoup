import requests
from bs4 import BeautifulSoup
import time
import mysql.connector
import pandas as pd
import sqlite3
from datetime import datetime

start = time.time()
now = datetime.now()
setDatetime = now.strftime("%Y/%m/%d %H:%M:%S")
dateAmbil = now.strftime("%Y-%m-%d")
timeAmbil = now.strftime("%H:%M:%S")
tanggalPublish = now.strftime("%A, %d %B %Y %H:%M WIB")
updateUser="elga.triana@mncgroup.com"

# Server
# db = mysql.connector.connect(
#     host='172.18.20.42',
#     database='intrasm_dashboard',
#     user='it_sales',
#     password='S4mDBProjectNginx!'
# )

# Local
db=mysql.connector.connect(
    host='localhost',
    database='intrasm_dashboard',
    user='root',
    password=''
)


cursor = db.cursor()

insertketabel = """INSERT INTO scrap_portal_parameter_dummy (tanggal, jam, kanal_id,
                judul_artikel, link_artikel, tanggal_publish, trending_google,
                created_at, updated_at, insert_user,
                update_user)
                values(%s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, %s,
                %s)"""

# IDN NEWS
url1 = requests.get('https://www.idntimes.com/news')
soup = BeautifulSoup(url1.text, 'html.parser')
articles = soup.find(id="latest-article").find_all(class_="box-latest")
link_articles = soup.find(class_="list-latest").find_all(class_="box-latest")

for a in articles:
    tanggal = dateAmbil
    jam = timeAmbil
    kanal_id = "1001"
    timezone = " WIB"
    judul_artikel = a.find('a')['title']
    link_artikel=a.find('a')['href']
    tanggal = a.find('time', class_="date")['datetime']
    tanggal_publish = tanggal + timezone
    splitdate=tanggal.split(' | ')
    tanggal_split=splitdate[0]
    tanggal_split_format = datetime.strptime(tanggal_split, '%d %b %y')
    jam_split = splitdate[1]
    trending_google = "N"
    created_at = setDatetime
    updated_at = setDatetime
    insert_user = "PYTHON ELGA"
    update_user = "PYTHON ELGA"

    values = (tanggal_split_format, jam_split, kanal_id, judul_artikel,
              link_artikel, tanggal_publish, trending_google,
              created_at, updated_at, insert_user,
              update_user)
    cursor.execute(insertketabel, values)
    db.commit()

print("BERHASIL SCRAPPING IDNTIMES NEWS")
# END NEWS IDN

# BUSINESS IDN
url2 = requests.get('https://www.idntimes.com/business')
soup = BeautifulSoup(url2.text, 'html.parser')

for a in articles:
    tanggal = dateAmbil
    jam = timeAmbil
    kanal_id = "1002"
    timezone = " WIB"
    judul_artikel = a.find('a')['title']
    link_artikel=a.find('a')['href']
    tanggal = a.find('time', class_="date")['datetime']
    tanggal_publish = tanggal + timezone
    splitdate=tanggal.split(' | ')
    tanggal_split=splitdate[0]
    tanggal_split_format = datetime.strptime(tanggal_split, '%d %b %y')
    jam_split = splitdate[1]
    trending_google = "N"
    created_at = setDatetime
    updated_at = setDatetime
    insert_user = "PYTHON ELGA"
    update_user = "PYTHON ELGA"

    values = (tanggal_split_format, jam_split, kanal_id, judul_artikel,
              link_artikel, tanggal_publish, trending_google,
              created_at, updated_at, insert_user,
              update_user)
    cursor.execute(insertketabel, values)
    db.commit()

print("BERHASIL SCRAPPING IDNTIMES BUSINESS")
# END BUSINESS IDN

#