class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    JUST = '\033[94m' #LIGHT BLUE

print ("                                  ▄▄▄▄                           ")
print ("▀███▀▀▀██▄▀███▀▀▀██▄ ▀███▀▀▀███ ▄█▀ ▀▀                           ")
print ("  ██   ▀██▄ ██    ▀██▄ ██    ▀█ ██▀                              ")
print ("  ██   ▄██  ██     ▀██ ██   █  █████ ▀███  ▀███  █▀▀▀███ █▀▀▀███ ")
print ("  ███████   ██      ██ ██▀▀██   ██     ██    ██  ▀  ███  ▀  ███  ")
print ("  ██        ██     ▄██ ██   █   ██     ██    ██    ███     ███   ")
print ("  ██        ██    ▄██▀ ██       ██     ██    ██   ███  ▄  ███  ▄ ")
print ("▄████▄    ▄████████▀ ▄████▄   ▄████▄   ▀████▀███▄███████ ███████ ")
print ("                                                                 ")
print ("")
print (f"{bcolors.JUST}[GIVE THE STAR ON MY GITHUB PAGE,IF YOU LIKE TOOL.]{bcolors.RESET}")
print (f"{bcolors.JUST}[https://github.com/un9nplayer/PDFfuzz]{bcolors.RESET}")
print (f"{bcolors.JUST}[Creator : Un9nplayer]{bcolors.RESET}")
print (f"{bcolors.JUST}[Working : CyberSecurity, Penetration Tester.]{bcolors.RESET}")
print ("")
# // Change the url of your Target //

#!/usr/bin/python3 

import requests
import os
import itertools
import threading
import time
import sys

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(2)
done = True
print(f"{bcolors.OK}\n          [Fatching URL on Websites!]{bcolors.RESET}")

def fuzz_PDFs():
        with open('days', 'r') as d:
                days = d.readlines()

        with open('months' ,'r') as m:
                months = m.readlines()

        url_file = open('urls', 'w')
        url_file.close()

        for month in months:
                for day in days:
                        r = requests.get(f'http://dc.intelligence.htb/documents/2020-{day.strip()}-{month.strip()}-upload.pdf') # // Change This to your target url //
                        if int(r.status_code) == 200:
                                print(f"{bcolors.WARNING}http://dc.intelligence.htb/documents/2020-{day.strip()}-{month.strip()}-upload.pdf{bcolors.RESET}")   # // Change This to your target url //

                                with open('urls', 'a') as url_file:
                                        url_file.write(f'http://dc.intelligence.htb/documents/2020-{day.strip()}-{month.strip()}-upload.pdf')  # // Change This to your target url //
                                        url_file.write('\n')

def get_PDFs():
        with open('urls', 'r') as u:
                urls = u.readlines()

        for url in urls:
                os.system(f"wget -q {url.strip()} ")
                print(f"{bcolors.OK}[+] Downloading -- {url.strip()} {bcolors.RESET}")


fuzz_PDFs()
print(f"{bcolors.WARNING}\n[Downloading your PDF Files be patience!\n]{bcolors.RESET}")
get_PDFs()
print(f"{bcolors.OK}\n[Done.!!!]\n[Your all PDF Files Downloaded in your Current Directory Folder]{bcolors.RESET}")
