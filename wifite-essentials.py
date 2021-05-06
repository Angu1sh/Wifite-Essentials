#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

logo = '''
##   __        ___  __ _ _         _____                    _   _       _
##   \ \      / (_)/ _(_) |_ ___  | ____|___ ___  ___ _ __ | |_(_) __ _| |___
##    \ \ /\ / /| | |_| | __/ _ \ |  _| / __/ __|/ _ \ '_ \| __| |/ _` | / _/
##     \ V  V / | |  _| | ||  __/ | |___\__ \__ \  __/ | | | |_| | (_| | \__ 
##      \_/\_/  |_|_| |_|\__\___| |_____|___/___/\___|_| |_|\__|_|\__,_|_|__|
'''
print('\033[34m' + logo + '\033[0m')
menu = '''
Choose the application you want to install 
(1)  Install Hcxdumptool & Hcxtools
(2)  Install Pyrit

[Fix your date on Kali before install it. Use date --set YYYY-MM-DD and HH:MM:SS]
'''
print('\033[33m' + menu)

def tools():
    os.system('apt-get install libcurl4-openssl-dev libssl-dev pkg-config zlib1g-dev libpcap-dev -y && apt-get update')
    os.system('git clone https://github.com/ZerBea/hcxdumptool.git && cd hcxdumptool && make && make install && cd ..')
    os.system('git clone https://github.com/ZerBea/hcxtools.git && cd hcxtools && make && make install && cd ..')
    print('\033[33m' + "Installing Hcxdumptool & Hcxtools ")


def pyrit():
    os.system("git clone https://github.com/hacker3983/how-to-install-pyrit-on-kali-linux-2020.1a pyrit-installer && cd pyrit-installer && sudo bash install.sh")
    print('\033[33m' + "Installing Pyrit" + '\033[0m')



choose = raw_input('\033[5m' + "Choose some option: " + '\033[0m')


if(choose == "1"):
    tools()
    print("Hcxdumptool and Hcxtools installed successfully! ")
elif(choose == "2"):
    pyrit()
    print("Pyrit installed successfully! ")
else:
    print('Done! Now im quitting...')
    exit()
