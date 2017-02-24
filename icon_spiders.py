#!usr/bin/python3


import requests,time
from bs4 import BeautifulSoup

"""
  http://www.woyaogexing.com/ 网站的头像图片爬取.

"""



def icon_spiders(url,num):
    #主程序
    r=requests.get(url)
    if r.status_code==200:
        r.encoding="utf8"
        soup=BeautifulSoup(r.text,"lxml")
        img=soup.find_all("img",{"class":"lazy"})
        for i in img:
            r=requests.get(i["src"])
            if r.status_code==200:
                print(num)
                with open("img/"+str(num)+".jpg","wb") as f:
                    f.write(r.content)
                    time.sleep(0.5)
                num += 1

        return num



num = 1567
for i in range(118,1000):
    try:
        url="http://www.woyaogexing.com/touxiang/index_%d.html"%i
        print(url,num)
        num=icon_spiders(url,num)
    except:
        num += 1
        continue

