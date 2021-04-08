import re
import requests
import urllib.request
import random
import time
import os

sym = "0123456789abcdefghijklmnopqrstuvwxyz"
path = "images/"

random.seed(int(time.time()))

def get(src,code):
    image = requests.get(src)
    with open(path+code+"_im.png",'wb') as f:
        f.write(image.content)

def rnd():
    return random.randint(0,len(sym)-1)

def generate():
    return sym[rnd()]+sym[rnd()]+sym[rnd()]+sym[rnd()]+sym[rnd()]+sym[rnd()]

while True:
    code = generate()

    req = urllib.request.Request("https://prnt.sc/"+generate(), headers={'User-Agent': 'Mozilla/5.0'})
    fp = urllib.request.urlopen(req)
    mybytes = fp.read()

    html = mybytes.decode("utf8")
    img = re.findall(r'<img.*class=".*".*?>',html)
    if img == []:
        fp.close()
        continue
    src = re.findall(r'src=".*?"',img[0])[0][5:-1]
    if src.find("prntscr.com") == -1:
        if not os.path.isfile(code+"_im.png"):
            get(src,code)
    fp.close()