import sys
import os
import customtkinter as ctk
import configparser

def main():
   
   existsIni = checkIni()
   if existsIni == True:
      return
   
   else:
      createIni()
   
   root = ctk.CTk()
   root.geometry("500x600")
   root.title("Finance Tracker")
   #root.set_appearance_mode("Dark")

   root.mainloop()

def createIni():
    
    config = configparser.ConfigParser()

    config["Settings"] = {
       "total": "0",
       "pay": "12.26",
       "tax": "20",
       "rent": "575",
       "council tax": "164",
       "wifi": "27",
       "power": "57"
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    print("INI file created with default settings.")

def checkIni():
   
   return os.path.exists('config.ini')

def readIni():
   return

def updateTotal(newTotal):
   return

def calcPay():
   return

def schedule():
   return

if __name__ == "__main__":
   main().run()