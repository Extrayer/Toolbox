from urllib.request import urlopen, urlretrieve
import progressbar
import os
from tkinter import messagebox
import tkinter as tk


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

root = tk.Tk()
root.overrideredirect(1)
root.withdraw()

def update_toolbox():
    urlretrieve('https://github.com/Extrayer/Toolbox/raw/master/toolbox.exe', "C:\\Toolbox\\toolbox.exe", ProgressBar() )

def update_version():
	if os.path.exists('C:/Toolbox/version.txt'):
   		os.remove('C:/Toolbox/version.txt')
	else:
		pass
	urlretrieve('https://www.toolbox.tk/version.txt', "C:\\Toolbox\\version.txt", ProgressBar() )

def start():

    try:
       os.mkdir('C:\Toolbox\Download')
    except:
        pass

    try:
        os.mkdir('C:\Toolbox\Download\App')
    except:
        pass

    try:
        os.mkdir('C:\Toolbox\Download\Driver')
    except:
        pass

    try:
        os.mkdir('C:\Toolbox\Download\Icon')
    except:
        pass

    try:
        os.mkdir('C:\Toolbox\Download\Regedit')
    except:
        pass

    try:
        os.mkdir('C:\Toolbox\Download\Wallpaper')
    except:
        pass

    os.startfile(r'C:\Toolbox\toolbox.exe')

def install():
    update_version()
    update_toolbox()
    start()

try:
    os.mkdir('C:\Toolbox')
except:
    pass

try: #Si fichier version.txt existe : 
    last_version = urlopen('http://toolbox.tk/version.txt').read().decode('utf8')
    
    fichier = open("C:\\Toolbox\\version.txt", "r")
    currently_version = (fichier.read())
    fichier.close()

    if currently_version == last_version :
        start()
    else:
        answer = None 
        while answer not in ("y", "n"): 
            answer = input("Found new version " + str(last_version) + ", do you want to update now ? (y/n) : ") 
            if answer == "y": 
                print("Mise à jour de l'application :")
                update_version() 
                update_toolbox()
                start()
            elif answer == "n": 
                start()
            else: 
                print("Please enter yes (y) or no (n).") 
   
except: #Si fichier version.txt n'existe pas : 
    install()
