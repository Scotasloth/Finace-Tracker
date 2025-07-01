import sys
import os
import customtkinter as ctk
import configparser

def main():
   
   existsIni = checkIni()
   if existsIni == True:
      total = readIni(1)
      forcast = readIni(2)
   
   else:
      createIni()
   
   root = ctk.CTk()
   root.geometry("600x400")
   root.title("Finance Tracker")
   #root.set_appearance_mode("Dark")

   totalLbl = ctk.CTkLabel(root, text = f"Total {total}")
   totalLbl.pack(pady = 20)

   forcastLbl = ctk.CTkLabel(root, text = f"Forcast {forcast}")
   forcastLbl.pack(pady = 20)

   addHoursBtn = ctk.CTkButton(root, text = "Add Hours", command=lambda: schedule(root))
   addHoursBtn.pack(pady = 20)

   addMoneyBtn = ctk.CTkButton(root, text = "Add Money", command=lambda: addMoney(root))
   addMoneyBtn.pack(pady = 20)

   root.mainloop()

def createIni():
    
    config = configparser.ConfigParser()

    config["Settings"] = {
       "total": "0",
       "forcast": "0",
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

def readIni(option):
   if option == 1:
      config = configparser.ConfigParser()
      config.read("config.ini")
      total = config["Settings"]["total"]

      return total
   
   if option == 2:
      config = configparser.ConfigParser()
      config.read("config.ini")
      forcast = config["Settings"]["total"]

      return forcast

def calcPay():
   return

def addMoney(root):
   return

def calcForcast():
   return

def schedule(root):
   return

if __name__ == "__main__":
   main()