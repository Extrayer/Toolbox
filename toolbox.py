import os
import platform
import sys
from socket import *
import json
import urllib.request
from datetime import datetime, timezone
import time
import speedtest
import progressbar
import webbrowser
import ctypes



class colors:
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    
class fg:
    black='\033[30m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'
    purple='\033[35m'
    cyan='\033[36m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    lightgreen='\033[92m'
    yellow='\033[33m'
    lightblue='\033[94m'
    pink='\033[95m'
    lightcyan='\033[96m'
    yellow2='\033[93m'
    
class bg:
    black='\033[40m'
    red='\033[41m'
    green='\033[42m'
    orange='\033[43m'
    blue='\033[44m'
    purple='\033[45m'
    cyan='\033[46m'
    lightgrey='\033[47m'

class ProgressBar():
    def __init__(self):
        self.pbar = None

    def __call__(self, block_num, block_size, total_size):
        if not self.pbar:
            self.pbar=progressbar.ProgressBar(maxval=total_size)
            self.pbar.start()

        downloaded = block_num * block_size
        if downloaded < total_size:
            self.pbar.update(downloaded)
        else:
            self.pbar.finish()

#GLOBAL

computer_user = ''
computer_name = ''
public_ip = ''
local_ip = ''
system = ''
release = ''
version = ''
utc_dt = ''

#FONCTION

def clear():
    os.system("cls")

def error():
    clear()
    print(colors.reset + fg.cyan + "This function is no available yet." + colors.reset)
    time.sleep(1)
    clear()
    accueil()

def reset():
    clear()
    accueil()
    
def start():
    
    
    clear()
    
    computer_user()
    computer_name()
    public_ip()
    local_ip()
    system()
    release()
    version()
    datetime1()

    accueil()



#APP

def social_link(): #1
    
    def twitter():
        webbrowser.open("https://twitter.com/Extrayer")
        social_link()

    def twitch():
        webbrowser.open("https://www.twitch.tv/extrayertv")
        social_link()

    def discord():
        webbrowser.open("https://discord.gg/BhxuYfm")
        social_link()

    def website():
        webbrowser.open("https://www.extrayer.tk/")
        social_link()

    def github():
        webbrowser.open("https://github.com/Extrayer")
        social_link()

    clear()
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(" Toolbox>Social Link>                                                                                                ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [1] ┃ Twitter                                                                                                       ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [2] ┃ Twitch                                                                                                        ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [3] ┃ Discord                                                                                                       ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [4] ┃ Website                                                                                                       ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [5] ┃ Github                                                                                                        ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [0] ┃ Back to menu                                                                                                  ")
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(" ")
    print(" ")
    choice=(input(colors.reset + fg.yellow2 + "Type Option : " + colors.reset))
    try:
        choice= int(choice)
        if choice == 0:
            reset()
        elif choice == 1:
            twitter()
        elif choice == 2:
            twitch()
        elif choice == 3:
            discord()
        elif choice == 4:
            website()
        elif choice == 5:
            github()
        else:
            error()
    except:
        error()

def shortcut(): #2
    clear()
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(" Toolbox>Shorcut>                                                                                              ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [1] ┃ Task Manager                                                                                                  ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [2] ┃ System Properties                                                                                             ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [3] ┃ Control Panel                                                                                                 ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [4] ┃ Ressource Monitor                                                                                             ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [5] ┃ System Information                                                                                            ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [6] ┃ Services                                                                                                      ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [7] ┃ About Windows                                                                                                 ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [8] ┃ Regedit                                                                                                       ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [9] ┃ Msconfig                                                                                                      ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [10] ┃ Computer Management                                                                                          ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [0] ┃ Back to menu                                                                                                  ")
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(" ")
    print(" ")
    choice=(input(colors.reset + fg.yellow2 + "Type Option : " + colors.reset))
    try:
        choice= int(choice)
        if choice == 0:
            reset()
        elif choice == 1:
            os.popen('taskmgr')
            shortcut()
        elif choice == 2:
            os.popen('sysdm.cpl')
            shortcut()
        elif choice == 3:
            os.popen('control')
            shortcut()
        elif choice == 4:
            os.popen('resmon')
            shortcut()
        elif choice == 5:
            os.popen('msinfo32')
            shortcut()
        elif choice == 6:
            os.popen('services.msc')
            shortcut()
        elif choice == 7:
            os.popen('winver')
            shortcut()
        elif choice == 8:
            os.popen('regedit')
            shortcut()
        elif choice == 9:
            os.popen('msconfig')
            shortcut()
        elif choice == 10:
            os.popen('compmgmt.msc')
            shortcut()
        else:
            error()
    except:
        error()

def information(): #3

    def back():
        information()

    def join():
        webbrowser.open("https://discord.gg/BhxuYfm")
        information()

    def update():
        clear()
        print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
        print(" Toolbox>Information>Update                                                                                         ")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" The Toolbox updates automatically each time the application is restarted.                                           ")
        print(" An option to disable these automatic updates will be available soon.                                                ")
        print("                                                                                                                     ")
        print(" If the software is not updated, there may be problems with some features.                                           ")
        print("                                                                                                                     ")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" [1] ┃ Return                                                                                                        ")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" [0] ┃ Back to menu                                                                                                  ")
        print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
        print(" ")
        print(" ")
        choice=(input(colors.reset + fg.yellow2 + "Type Option : " + colors.reset))
        try:
            choice= int(choice)
            if choice == 0:
                reset()
            elif choice == 1:
                back()
            else:
                error()
        except:
            error()

    def changelog():
        clear()
        print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
        print(" Toolbox>Information>Changelog>                                                                                      ")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" Last update : 24/06/2020                                                                                            ")
        print("                                                                                                                     ")
        print(" - Added category #Information                                                                                       ")
        print(" - Added category #Social Link                                                                                       ")
        print("                                                                                                                     ")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" [1] ┃ Return                                                                                                        ")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" [0] ┃ Back to menu                                                                                                  ")
        print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
        print(" ")
        print(" ")
        choice=(input(colors.reset + fg.yellow2 + "Type Option : " + colors.reset))
        try:
            choice= int(choice)
            if choice == 0:
                reset()
            elif choice == 1:
                back()
            else:
                error()
        except:
            error()

    clear()
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(" Toolbox>Information>                                                                                              ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" Toolbox v1.0.1 created by Extrayer.                                                                                 ")
    print(" This script can cause many problems.                                                                                ")
    print(" I am in no way responsible for your actions.                                                                        ")
    print(" In cooperation with the ELITY team.                                                                                 ")
    print(" Discord ELITY: discord.gg/BhxuYfm                                                                                   ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [1] ┃ Join ELITY                                                                                                    ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [2] ┃ Update                                                                                                        ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [3] ┃ Changelogs                                                                                                    ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [0] ┃ Back to menu                                                                                                  ")
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(" ")
    print(" ")
    choice=(input(colors.reset + fg.yellow2 + "Type Option : " + colors.reset))
    try:
        choice= int(choice)
        if choice == 0:
            reset()
        elif choice == 1:
            join()
        elif choice == 2:
            update()
        elif choice == 3:
            changelog()
        else:
            error()
    except:
        error()

def leave(): #4
    pass

def speedtest_app(): #5

    def retry():
        clear()
        launch()
    
    def test():
        print("┌───────────────────┐                  ")
        print("│                   │ Connecting...    ")
        print("└───────────────────┘                  ")
        s = speedtest.Speedtest()
        clear()
        print("┌───────────────────┐                  ")
        print("│═══                │ Connecting...    ")
        print("└───────────────────┘                  ")
        s.get_servers()
        clear()
        print("┌───────────────────┐                  ")
        print("│══════             │ Connecting...    ")
        print("└───────────────────┘                  ")
        s.get_best_server()
        clear()
        print("┌───────────────────┐                  ")
        print("│══════════         │ Connecting...    ")
        print("└───────────────────┘                  ")
        s.download()
        clear()
        print("┌───────────────────┐                  ")
        print("│═══════════════    │ Connecting...    ")
        print("└───────────────────┘                  ")
        s.upload()
        clear()
        print("┌───────────────────┐                  ")
        print("│═══════════════════│ Connecting...    ")
        print("└───────────────────┘                  ")
        res = s.results.dict()
        return res["download"], res["upload"], res["ping"]

    def launch():
        clear()
        d, u, p = test()
        clear()
        print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
        print(" Toolbox>Speedtest>Results")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" ")
        print(' Download: {:.2f} Mo/s\n'.format(d / 1000000))
        print(' Upload: {:.2f} Mo/s\n'.format(u / 1000000))
        print(' Ping: {} ms\n'.format(p))
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" [1] ┃ Retry")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" [0] ┃ Back to menu")
        print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
        print(" ")
        print(" ")
        choice=(input(colors.reset + fg.yellow2 + "Type Option : " + colors.reset))
        try:
            choice= int(choice)
            if choice == 0:
                reset()
            elif choice == 1:
                retry()
            else:
                error()
        except:
            error()
        
    clear()
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(" Toolbox>Speedtest>")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [1] ┃ Start")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [0] ┃ Back to menu")
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(" ")
    print(" ")
    
    choice=(input(colors.reset + fg.yellow2 + "Type Option : " + colors.reset))
    try:
        choice= int(choice)
        if choice == 0:
            reset()
        elif choice == 1:
            launch()
        else:
            error()

    except:
        error()

def regedit(): #6
    clear()
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(" Toolbox>Regedit>                                                                                                    ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" By modifying the windows registry you expose your windows to                                                        ")
    print(" bugs and errors.                                                                                                    ")
    print("                                                                                                                     ")
    print(" We advise you to make a backup of windows before use.                                                               ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [1] ┃ Right Click Menu                                                                                              ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [2] ┃ Explorer                                                                                                      ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [3] ┃ Windows Defender                                                                                              ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [4] ┃ Windows Update                                                                                                ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [0] ┃ Back to menu                                                                                                  ")
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(" ")
    print(" ")
    choice=(input(colors.reset + fg.yellow2 + "Type Option : " + colors.reset))
    try:
        choice= int(choice)
        if choice == 0:
            reset()
        elif choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        else:
            error()
    except:
        error()

def activate(): #7
    pass

def optimisation(): #8
    def on_opti():
        os.popen('REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Search" /v AllowCortana /t REG_DWORD /d 00000000 /f')
        os.popen('REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Power" /v HiberbootEnabled /t REG_DWORD /d 00000000 /f')
        os.popen('reg add "HKCU\Keyboard Layout\toggle" /v "Language Hotkey" /t REG_SZ /d 3 /f')
        os.popen('REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v DisallowShaking /t REG_DWORD /d 00000001 /f')
        os.popen('powercfg -h off')
        os.popen('fsutil behavior set DisableDeleteNotify 0')
        os.popen('REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v SystemResponsiveness /t REG_DWORD /d 00000010 /f')

    def off_opti():
        os.popen('REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Search" /v AllowCortana /t REG_DWORD /d 00000001 /f')
        os.popen('REG ADD "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Power" /v HiberbootEnabled /t REG_DWORD /d 00000001 /f')
        os.popen('reg add "HKCU\Keyboard Layout\toggle" /v "Language Hotkey" /t REG_SZ /d 1 /f')
        os.popen('REG ADD "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v DisallowShaking /t REG_DWORD /d 00000000 /f')
        os.popen('powercfg -h on')
        os.popen('fsutil behavior set DisableDeleteNotify 0')
        os.popen('REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v SystemResponsiveness /t REG_DWORD /d 00000020 /f')

    clear()
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(" Toolbox>Optimisation>                                                                                   ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [1] ┃ Enable : Optimisation                                                                                         ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [2] ┃ Disable : Optimisation                                                                                        ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [0] ┃ Back to menu                                                                                                  ")
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(" ")
    print(" ")
    choice=(input(colors.reset + fg.yellow2 + "Type Option : " + colors.reset))
    try:
        choice= int(choice)
        if choice == 0:
            reset()
        elif choice == 1:
            on_opti()
            optimisation()
        elif choice == 2:
            off_opti()
            optimisation()
        else:
            error()
    except:
        error()

def custom(): #9

    def wallpapers():
        
        def minimalist():
            def un():
                clear()
                try:
                    urllib.request.urlretrieve('https://raw.githubusercontent.com/ExToolbox/download/walppaper/Minimalist1.jpg', "C:\\Toolbox\\Download\\Wallpaper\\Minimalist1.jpg", ProgressBar() )
                    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Toolbox\\Download\\Wallpaper\\Minimalist1.jpg" , 0)
                except:
                    pass
                ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Toolbox\\Download\\Wallpaper\\Minimalist1.jpg" , 0)
                minimalist()
            def deux():
                clear()
                try:
                    urllib.request.urlretrieve('https://raw.githubusercontent.com/ExToolbox/download/walppaper/Minimalist2.jpg', "C:\\Toolbox\\Download\\Wallpaper\\Minimalist2.jpg", ProgressBar() )
                    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Toolbox\\Download\\Wallpaper\\Minimalist2.jpg" , 0)
                except:
                    pass
                ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Toolbox\\Download\\Wallpaper\\Minimalist2.jpg" , 0)
                minimalist()
            def trois():
                clear()
                try:
                    urllib.request.urlretrieve('https://raw.githubusercontent.com/ExToolbox/download/walppaper/Minimalist3.jpg', "C:\\Toolbox\\Download\\Wallpaper\\Minimalist3.jpg", ProgressBar() )
                    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Toolbox\\Download\\Wallpaper\\Minimalist3.jpg" , 0)
                except:
                    pass
                ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Toolbox\\Download\\Wallpaper\\Minimalist3.jpg" , 0)
                minimalist()
            clear()
            print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
            print(" Toolbox>Personalize>Wallpaper>Minimalist>                                                                            ")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(" [1] ┃ Space                                                                                                         ")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(" [2] ┃ Island                                                                                                        ")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(" [3] ┃ Mountain                                                                                                      ")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(" [4] ┃ Return                                                                                                        ")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(" [0] ┃ Back to menu                                                                                                  ")
            print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
            print(" ")
            print(" ")
            choice=(input(colors.reset + fg.yellow2 + "Type Option : " + colors.reset))
            try:
                choice= int(choice)
                if choice == 0:
                    reset()
                elif choice == 1:
                    un()
                elif choice == 2:
                    deux()
                elif choice == 3:
                    trois()
                elif choice == 4:
                    wallpapers()
                else:
                    error()
            except:
                error()

        def manga():
            def un():
                pass
            def deux():
                pass
            def trois():
                pass
            clear()
            print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
            print(" Toolbox>Personalize>Wallpaper>Manga>                                                                               ")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(" [1] ┃                                                                                                               ")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(" [2] ┃                                                                                                               ")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(" [3] ┃                                                                                                               ")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(" [4] ┃ Return                                                                                                        ")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(" [0] ┃ Back to menu                                                                                                  ")
            print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
            print(" ")
            print(" ")
            choice=(input(colors.reset + fg.yellow2 + "Type Option : " + colors.reset))
            try:
                choice= int(choice)
                if choice == 0:
                    reset()
                elif choice == 1:
                    un()
                elif choice == 2:
                    deux()
                elif choice == 3:
                    trois()
                elif choice == 4:
                    wallpapers()
                else:
                    error()
            except:
                error()

        def cars():
            def un():
                pass
            def deux():
                pass
            def trois():
                pass
            clear()
            print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
            print(" Toolbox>Personalize>Wallpaper>Cars>                                                                                 ")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(" [1] ┃                                                                                                               ")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(" [2] ┃                                                                                                               ")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(" [3] ┃                                                                                                               ")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(" [4] ┃ Return                                                                                                        ")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(" [0] ┃ Back to menu                                                                                                  ")
            print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
            print(" ")
            print(" ")
            choice=(input(colors.reset + fg.yellow2 + "Type Option : " + colors.reset))
            try:
                choice= int(choice)
                if choice == 0:
                    reset()
                elif choice == 1:
                    un()
                elif choice == 2:
                    deux()
                elif choice == 3:
                    trois()
                elif choice == 4:
                    wallpapers()
                else:
                    error()
            except:
                error()

        def gaming():
            def un():
                clear()
                try:
                    urllib.request.urlretrieve('https://raw.githubusercontent.com/ExToolbox/download/walppaper/Gaming1.jpg', "C:\\Toolbox\\Download\\Wallpaper\\Gaming1.jpg", ProgressBar() )
                    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Toolbox\\Download\\Wallpaper\\Gaming1.jpg" , 0)
                except:
                    pass
                ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Toolbox\\Download\\Wallpaper\\Gaming1.jpg" , 0)
                gaming()
            def deux():
                clear()
                try:
                    urllib.request.urlretrieve('https://raw.githubusercontent.com/ExToolbox/download/walppaper/Gaming2.jpg', "C:\\Toolbox\\Download\\Wallpaper\\Gaming2.jpg", ProgressBar() )
                    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Toolbox\\Download\\Wallpaper\\Gaming2.jpg" , 0)
                except:
                    pass
                ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Toolbox\\Download\\Wallpaper\\Gaming2.jpg" , 0)
                gaming()
            def trois():
                clear()
                try:
                    urllib.request.urlretrieve('https://raw.githubusercontent.com/ExToolbox/download/walppaper/Gaming3.jpg', "C:\\Toolbox\\Download\\Wallpaper\\Gaming3.jpg", ProgressBar() )
                    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Toolbox\\Download\\Wallpaper\\Gaming3.jpg" , 0)
                except:
                    pass
                ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Toolbox\\Download\\Wallpaper\\Gaming3.jpg" , 0)
                gaming()
            clear()
            print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
            print(" Toolbox>Personalize>Wallpaper>Gaming>                                                                               ")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(" [1] ┃ Ak-47                                                                                                         ")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(" [2] ┃ Halo V                                                                                                        ")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(" [3] ┃ Mario                                                                                                         ")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(" [4] ┃ Return                                                                                                        ")
            print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
            print(" [0] ┃ Back to menu                                                                                                  ")
            print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
            print(" ")
            print(" ")
            choice=(input(colors.reset + fg.yellow2 + "Type Option : " + colors.reset))
            try:
                choice= int(choice)
                if choice == 0:
                    reset()
                elif choice == 1:
                    un()
                elif choice == 2:
                    deux()
                elif choice == 3:
                    trois()
                elif choice == 4:
                    wallpapers()
                else:
                    error()
            except:
                error()

        clear()
        print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
        print(" Toolbox>Personalize>Wallpaper>                                                                                       ")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" [1] ┃ Minimalist                                                                                                    ")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" [2] ┃ Manga                                                                                                         ")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" [3] ┃ Cars                                                                                                          ")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" [4] ┃ Gaming                                                                                                        ")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" [5] ┃ Return                                                                                                        ")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" [0] ┃ Back to menu                                                                                                  ")
        print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
        print(" ")
        print(" ")
        choice=(input(colors.reset + fg.yellow2 + "Type Option : " + colors.reset))
        try:
            choice= int(choice)
            if choice == 0:
                reset()
            elif choice == 1:
                minimalist()
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                gaming()
            elif choice == 5:
                custom()
            else:
                error()
        except:
            error()


    def themes():

        def light_theme():
            os.popen('REG ADD "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v SystemUsesLightTheme /t REG_DWORD /d 00000001 /f')

        def dark_theme():
            os.popen('REG ADD "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v SystemUsesLightTheme /t REG_DWORD /d 00000000 /f')

        clear()
        print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
        print(" Toolbox>Personalize>Themes>                                                                                          ")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" [1] ┃ Light theme                                                                                                   ")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" [2] ┃ Dark theme                                                                                                    ")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" [3] ┃ Return                                                                                                        ")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" [0] ┃ Back to menu                                                                                                  ")
        print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
        print(" ")
        print(" ")
        choice=(input(colors.reset + fg.yellow2 + "Type Option : " + colors.reset))
        try:
            choice= int(choice)
            if choice == 0:
                reset()
            elif choice == 1:
                light_theme()
                themes()
            elif choice == 2:
                dark_theme()
                themes()
            elif choice == 3:
                custom()
            else:
                error()
        except:
            error()
        

    def taskbar():

        def on_transparency():
            os.popen('REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v UseOLEDTaskbarTransparency /t REG_DWORD /d 00000001 /f')
        def off_transparency():
            os.popen('REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v UseOLEDTaskbarTransparency /t REG_DWORD /d 00000000 /f')

        clear()
        print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
        print(" Toolbox>Personalize>Taskbar>                                                                                         ")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" [1] ┃ Enable : Transparency                                                                                         ")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" [2] ┃ Disable : Transparency                                                                                        ")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" [3] ┃ Return                                                                                                        ")
        print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
        print(" [0] ┃ Back to menu                                                                                                  ")
        print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
        print(" ")
        print(" ")
        choice=(input(colors.reset + fg.yellow2 + "Type Option : " + colors.reset))
        try:
            choice= int(choice)
            if choice == 0:
                reset()
            elif choice == 1:
                on_transparency()
                taskbar()
            elif choice == 2:
                off_transparency()
                taskbar()
            elif choice == 3:
                custom()
            else:
                error()
        except:
            error()

    clear()
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(" Toolbox>Personalize>                                                                                                 ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" The toolbox offers wallpapers, themes and the possibility to make the taskbar transparent or not.                   ")
    print(" You will be able to add wallpapers in the toolbox by making a request on discord or twitter.                        ")
    print(" Check social link for joins.                                                                                        ")
    print("                                                                                                                     ")
    print(" This script can cause many problems.                                                                                ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [1] ┃ Walppaper                                                                                                     ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [2] ┃ Themes                                                                                                        ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [3] ┃ Taskbar                                                                                                       ")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [0] ┃ Back to menu                                                                                                  ")
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(" ")
    print(" ")
    choice=(input(colors.reset + fg.yellow2 + "Type Option : " + colors.reset))
    try:
        choice= int(choice)
        if choice == 0:
            reset()
        elif choice == 1:
            wallpapers()
        elif choice == 2:
            themes()
        elif choice == 3:
            taskbar()
        else:
            error()
    except:
        error()
    

def google_dl(): #10

    def download_google():

        clear()
        urllib.request.urlretrieve('https://github.com/ExToolbox/download/raw/master/ChromeSetup.exe', "C:\\Toolbox\\Download\\App\\ChromeSetup.exe", ProgressBar())
        os.startfile(r'C:\Toolbox\Download\App\ChromeSetup.exe')
        reset()
        
    clear()
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(" Toolbox>Google Chrome (browser)>")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [1] ┃ Download")
    print(" [0] ┃ Back to menu")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" Servers : Google ")
    print(" Arch    : x86 / x64 ")
    print(" Required Internet for download. ")
    print(" Version : Latest    ")
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(" ")
    print(" ")
    
    choice=(input(colors.reset + fg.yellow2 + "Type Option : " + colors.reset))
    try:  
        choice= int(choice)
        if choice == 0:
            reset()
        elif choice == 1:
            download_google()
        else:
            error()

    except:
        error()

def discord_dl(): #11
    
    def download_discord():

        clear()
        urllib.request.urlretrieve('http://download1869.mediafire.com/1rbufe47lesg/2ue71pf9av69u2d/DiscordSetup.exe', "C:\\Toolbox\\Download\\App\\DiscordSetup.exe", ProgressBar())
        os.startfile(r'C:\Toolbox\Download\App\DiscordSetup.exe')
        reset()
    
    clear()
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(" Toolbox>Discord (Social Network)>")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [1] ┃ Download")
    print(" [0] ┃ Back to menu")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" Servers : DiscordApp ")
    print(" Arch    : x86 / x64 ")
    print(" Required Internet for download. ")
    print(" Version : Latest    ")
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(" ")
    print(" ")
    
    choice=(input(colors.reset + fg.yellow2 + "Type Option : " + colors.reset))

    try:
        choice= int(choice)
        
        if choice == 0:
            reset()
        elif choice == 1:
            download_discord()
        else:
            error()

    except:
        error()

def zip_dl(): #12
    
    def download_zip():

        clear()
        urllib.request.urlretrieve('https://www.7-zip.org/a/7z2000-x64.exe', "C:\\Toolbox\\Download\\App\\7zip.exe", ProgressBar())
        os.startfile(r'C:\Toolbox\Download\App\7zip')
        reset()
    
    clear()
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(" Toolbox>7zip (Decompressor)>")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" [1] ┃ Download")
    print(" [0] ┃ Back to menu")
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    print(" Servers : Zzip ")
    print(" Arch    : x86 / x64 ")
    print(" Required Internet for download. ")
    print(" Version : Latest    ")
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(" ")
    print(" ")
     
    choice=(input(colors.reset + fg.yellow2 + "Type Option : " + colors.reset))

    try:
        choice = int(choice)
        
        if choice == 0:
            reset()
        elif choice == 1:
            download_zip()
        else:
            error()
            
    except:
        error()

def drivers(): #13
    pass


#REQUEST

def computer_user():
    global computer_user
    computer_user = os.getenv("USERNAME")
def computer_name():
    global computer_name
    computer_name = platform.node()
def public_ip():
    global public_ip
    url = urllib.request.urlopen('http://httpbin.org/ip').read()
    public_ip = json.loads(url.decode())['origin']
def local_ip():
    global local_ip
    local_ip = (gethostbyname(gethostname()))
def system():
    global system
    system = platform.system()
def release():
    global release
    release = platform.release()  
def version():
    global version
    version = platform.version()
def datetime1():
    global utc_dt
    utc_dt = datetime.now(timezone.utc)
    utc_dt = utc_dt.astimezone().isoformat()

#MAIN
    
def accueil():
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(" Toolbox>")    
    print("────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
    time.sleep(0.05)
    print(colors.reset + " TOOLBOX" + fg.cyan + " 1.0.1 " + colors.reset + "|" + fg.cyan + " x64" + colors.reset + " | USER : " + fg.yellow + str(computer_user) + colors.reset + "  | COMPUTERNAME : " + fg.yellow + str(computer_name) + colors.reset)
    time.sleep(0.05)
    print(colors.reset + " YOUR CURRENT OS : " + fg.green + str(system) + " " + str(release) + colors.reset + " | " + "BUILD : " + fg.green +  str(version ) + str(release) + colors.reset + " | ARCH : " + fg.green + "(64bit)")
    time.sleep(0.05)
    print(colors.reset + " PUBLIC IP : " + fg.purple + str(public_ip) + colors.reset + " | " + "LOCAL IP : " + fg.purple + str(local_ip) + colors.reset)
    time.sleep(0.05)
    print(colors.reset + " TIME ZONE : " + fg.lightred + str(utc_dt) + colors.reset)
    time.sleep(0.05)
    print(colors.reset + " FOLLOW US ON TWITTER : " + fg.blue + "@Extrayer " + colors.reset)
    time.sleep(0.05)
    print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    time.sleep(0.05)
    print(" ")
    print(" ")
    print(            "════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════" + colors.reset)
    time.sleep(0.05)
    print(            "                                                                                                                        " + colors.reset)
    time.sleep(0.05)
    print(fg.blue +   "  GENERAL :                                                                                                             " + colors.reset)
    time.sleep(0.05)
    print(fg.yellow + "  ─────────                                                                                                             " + colors.reset)
    time.sleep(0.05)
    print(            "  [1] ┃ Social Link                           [3] ┃ Information                                                         " + colors.reset)
    time.sleep(0.05)
    print(            "  [2] ┃ Shortcut                              [4] ┃ Quit                                                                " + colors.reset)
    time.sleep(0.05)
    print(            "                                                                                                                        " + colors.reset)
    time.sleep(0.05)
    print(fg.blue +   "  UTILITIES :                                 INSTALLER :                                                               " + colors.reset)
    time.sleep(0.05)
    print(fg.yellow + "  ───────────                                 ───────────                                                               " + colors.reset)
    time.sleep(0.05)
    print(            "  [5] ┃ SpeedTest                             [10] ┃ Google Chrome (Browser)                                            " + colors.reset)
    time.sleep(0.05)
    print(            "  [6] ┃ Regedit                               [11] ┃ Discord (Social Network)                                           " + colors.reset)
    time.sleep(0.05)
    print(            "  [7] ┃ Windows Activator                     [12] ┃ 7-Zip (Decompressor)                                               " + colors.reset)
    time.sleep(0.05)
    print(            "  [8] ┃ Optimisation                          [13] ┃ Drivers                                                            " + colors.reset)
    time.sleep(0.05)
    print(            "  [9] ┃ Personalize                           [14] ┃ Users request                                                      " + colors.reset)
    time.sleep(0.05)
    print(            "                                                                                                                        " + colors.reset)
    time.sleep(0.05)
    print(            "════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════" + colors.reset)
    print(" ")

    choice =(input(colors.reset + fg.yellow2 + "Type Option : " + colors.reset))


    try:
        choice = int(choice)

        if choice == 1:
            social_link()
        elif choice == 2:
            shortcut()
        elif choice == 3:
            information()
        elif choice == 4:
            leave()
        elif choice == 5:
            speedtest_app()
        elif choice == 6:
            regedit()
        elif choice == 7:
            activate()
        elif choice == 8:
            optimisation()
        elif choice == 9:
            custom()
        elif choice == 10:
            google_dl()
        elif choice == 11:
            discord_dl()
        elif choice == 12:
            zip_dl()
        elif choice == 13:
            error()
        elif choice == 13:
            error()
        else:
            error()

    except:
        error()


os.system("title TOOLBOX")

start()
    
