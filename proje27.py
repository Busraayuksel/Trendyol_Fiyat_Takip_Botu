import smtplib
import requests
from bs4 import BeautifulSoup

url = 'https://www.trendyol.com/trendyolmilla/tas-kemerli-toka-detayli-gomlek-twoaw20go0099-p-46044113'

header = {'User Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'}

mail = input("mail adresiniz : ")
password = input("şifreniz : ")
sendToMail = input("gönderilecek mail adresi : ")

class Product:
    def __init__(self, header, url):
        self.header = header
        self.url = url
        
    def informationProduct(self):
        website = requests.get(url,headers=header).content
        soup = BeautifulSoup(website,'html.parser')
        product = soup.find("h1",{"class":"pr-new-br"})
        brand = product.find("a").text
        productName = product.find("span").text
        price = soup.find("div",{"pr-bx-nm with-org-prc"}).text
        print("Ürün Bilgileri".center(50,' '))
        print(f"Adı: {productName}\nMarka : {brand}\nFiyat : {price}")

        if price < '210':
            subject = 'ÜRÜN İNDİRİRİMİ'.center(80,' ')
            msg = f"{subject} \n{productName} fiyatı {price} TL'ye düştü."
            print(msg)
            smt = smtplib.SMTP('smtp.gmail.com',587)
            smt.ehlo()
            smt.starttls()
            smt.login(mail,password)
            smt.sendmail(sendToMail,msg.encode('utf-8'))
            smt.quit()

urun = Product(header,url)
urun.informationProduct()