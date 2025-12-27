import psutil
import time
import sys
import subprocess
from pynput.keyboard import Key, Controller

keyboard = Controller()

subprocess.Popen([sys.executable, "listener.py"])

file = open("AI.txt", "r")
restricted = file.read().split("\n")
file.close()

def get_the_pograms():
    list_progs = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            list_progs.append(proc.info["name"])
        except psutil.NoSuchProcess:
            pass
    return list_progs

print(restricted)
while True:
    file = open("IDEs.txt", "r")
    ides = file.read().split("\n")
    file.close()
    time.sleep(0.5)
    flag = False
    progs = get_the_pograms()
    for ide in ides:
        if ide in progs:
            flag = True
            break
    if flag:
        time.sleep(0.5)
        file = open("log.txt", "r")
        data = file.read()
        file.close()
        for r in restricted:
            if r in data:
                file = open("log.txt", "w")
                file.write("")
                file.close()
                subprocess.run([
                    "osascript",
                    "-e",
                    'tell application "System Events" to keystroke "w" using command down'
                ])
                subprocess.run(["osascript", "-e", 'open location "https://medium.com/@Rkrishanthan/you-should-stop-vibe-coding-here-is-why-0a91a3ab037f"'])