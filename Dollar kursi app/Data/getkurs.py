import requests
from bs4 import BeautifulSoup

def get_kur(kurs):
    dollar = requests.get("https://dollaruz.su/")
    kurs = BeautifulSoup(dollar.content)
    dkurs = kurs.find_all("tr")

# print(dkurs)
    for i in dkurs:
         f = i.find_all("td")
    return 'Malumotlari='+f[0].text.strip()+':@ziraatbank.uz'+'\nTelefon:+998781476767'+'Dollar Kursi='+f[1].text.strip()

    


# # print(dkurs)

