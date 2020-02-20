from bs4 import *
import requests as rq
import os

r2 = rq.get("https://unsplash.com/@ultrabrad")
soup2 = BeautifulSoup(r2.text, "html.parser")

links=[]

x=soup2.select('img[src^="https://unsplash.com/photos/u4cXtIbs6Ts"]')

for img in x:
    links.append(img['src'])

for l in links:
    print(l)

os.mkdir('photos')

i=1

for index,img_link in enumerate(links):
    if i<=10:
        img_data = rq.get(img_link).content
        with open("photos/",str(index+1)+'.jpg','wb+') as f:
            f.write(img_data)
        i+= 1
    else:
        f.close()
        break
        
