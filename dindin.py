#dindin.py helps you pick your dinner!
import os
import random
import subprocess

meats = ['pork','ground','beef','chicken','fish','tuna','turkey','chorizo','shrimp']
carbs = ['potato','rice','pasta','bread','bean']
styles = ['italian','mexican','asian','american','carribean','filipino','french']

chrome32 = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
chrome64 = "C:/Program Files/Google/Chrome/Application/chrome.exe"

act = None
while act != 'q':
    meat = random.choice(meats)
    carb = random.choice(carbs)
    style = random.choice(styles)

    print(meat)
    print(carb)
    print(style)

    if os.path.isfile(chrome32):
        path = chrome32
    elif os.path.isfile(chrome64):
        path = chrome64
    else:
        msg = "Chrome not installed or accessible!"
        print(msg)
        exit()

    url = r'https://www.google.com/search?q=' + meat + "+" + carb + "+" + style
    
    subprocess.Popen([path, url])
    
    act = input('q to quit:').lower()
exit()
