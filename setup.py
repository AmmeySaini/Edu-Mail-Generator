import subprocess
import sys
from __dwnldDrivers.versions import *

######## This script is only for educational purpose ########
######## use it on your own RISK ########
######## I'm not responsible for any loss or damage ########
######## caused to you using this script ########
######## Github Repo - https://git.io/JJisT/ ########

def install(name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])

def main():

    my_packages = ['requests', 'clint', 'faker', 'selenium', 'colorama']

    installed_pr = [] 
    
    for package in my_packages:
        install(package)
        print('\n')

    print('Firefox')
    firefox_ver = get_firefox_version()
    if firefox_ver != None:
        is_firefox_there = 1
        installed_pr.append('Firefox')
        setup_Firefox(firefox_ver)
    else:
        is_firefox_there = 0
        print('Firefox isn\'t installed')
    
    print('\nChrome')
    chrome_ver = get_chrome_version()

    if chrome_ver != None:
        is_chrome_there = 1
        installed_pr.append('Chrome')
        setup_Chrome(chrome_ver)
    else:
        is_chrome_there = 0
        print('Chrome isn\'t installed')
    
    if is_firefox_there == 0 and is_chrome_there == 0:
        print('Error - Setup installation failed \nReason - Please install either Chrome or Firefox browser to complete setup process')
        exit()

    print('\nWich browser do you prefer to run script on')

    for index, pr in enumerate(installed_pr, start=1):
        print('\n[*] ' + str(index) + ' ' + pr)
    
    inpErr = True

    while inpErr != False:
        print('\nEnter id ex - 1 or 2: ', end='')
        userInput = int(input())

        if userInput <= len(installed_pr) and userInput > 0:
            selected = installed_pr[userInput - 1]
            fp = open('prefBrowser.txt', 'w')
            fp.write(selected.lower())
            inpErr = False
        else:
             print('Wrong id, Either input 1 or 2')

    print('Setup Completed')
if __name__ == '__main__':
    main()