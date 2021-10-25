from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.turboclass.com.br/").content
soup = BeautifulSoup(html,"html.parser")
#print(soup.prettify)
carros = soup.findAll("a")

i = 1
for carro in soup.find_all("a"):
    print("\n",i ,carro.get("href=anuncio/detalhe"))
    i =i+1