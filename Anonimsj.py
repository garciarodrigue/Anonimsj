#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys,time
import requests
from colorama import Style,  Back, Fore, init
init()

clear = os.system("clear")

print(clear)

S = Style.BRIGHT

C = Fore.CYAN
R = Fore.RED
B = Fore.BLUE
M = Fore.MAGENTA
G = Fore.GREEN
Bl = Fore.BLACK
Y = Fore.YELLOW

Bb = Back.BLACK
Bw = Back.WHITE

print( C +""" 
    ▇▇◤▔▔▔▔▔▔▔◥▇▇
    ▇▇▏◥▇◣┊◢▇◤▕▇▇
    ▇▇▏▃▆▅▎▅▆▃▕▇▇
    ▇▇▏╱▔▕▎▔▔╲▕▇▇
    ▇▇◣◣▃▅▎▅▃◢◢▇▇
    ▇▇▇◣◥▅▅▅◤◢▇▇▇
    ▇▇▇▇◣╲▇╱◢▇▇▇▇ 
""" + G + "T3nshi")

logo = Bw + S + Bl + """
𝕸𝖘𝖏 𝕺𝖋 𝕬𝖓𝖔𝖓𝖞𝖒𝖔𝖚𝖘
""" + Bb

for l in logo:
    sys.stdout.flush()
    print(l,end="")
    time.sleep(0.1)
#while True:
    #try:
def ingresa():
        print(B)
        Num = input(S + "𝕮𝖔𝖉𝖊 + 𝕹𝖚𝖒𝖊𝖗𝖔 》 " + G)
        print(B)
        Msj = input(S + "𝕸𝖘𝖏 》 " + G)

        resp = requests.post('https://textbelt.com/text', {
          'phone': f'{Num}',
          'message': f'{Msj}',
          'key': 'textbelt',
        })

        print(S + Y + "\nEnviando\n")
        time.sleep(1.0)
        print(S , R, resp.json())
        
ingresa()
while True:
    try:
        ingresa()
        
    except KeyboardInterrupt:
        print("Saliendo")
        os.system("exit")
                   
        
        

