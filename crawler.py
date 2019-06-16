import os 
from datetime import datetime 
from queue import Queue
from threading import Thread
import requests
requests.packages.urllib3.disable_warnings()

from bs4 import BeautifulSoup
import re


# 声明一个队列
Q = Queue()
for i in range(50):
    Q.put(i)

def worker(i):
    while not Q.empty():
        page = Q.get()
        print("[-] 收集第 {} 页".format(str(page)))
        url = "http://simpledesktops.com/browse/"+str(page)+"/"
        try:
            r = requests.get(url,verify=False,timeout=5)
            html = r.text
            soup = BeautifulSoup(html,'html.parser')
            imgs = soup.find_all('img')
            for img in imgs:
                img_url = img['src']
                text = re.search('(http://static.simpledesktops.com/uploads/desktops/\d+/\d+/\d+/(.*?png)).*?png',img_url)
                new_img_url = text.group(1)

                r = requests.get(new_img_url,verify=False,timeout=5)
                path = "source/img/"+text.group(2)
                print("[-] 线程 {} 开始下载 {} 开始时间：{}".format(i,text.group(2),datetime.now()))

                with open(path,'wb') as f:
                    f.write(r.content)

        except Exception as e: 
            print(e)

    Q.all_tasks_done


if __name__ =="__main__":
    # 一定要将数据加入队列，否则是启动不了的，因为队列为空 
    # 线程的声明
    ts = [Thread(target=worker,args=(i,)) for i in range(200)]
    for t in ts:
        t.start()

    for t in ts:
        t.join()