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

   totalLbl = ctk.CTkLabel(root, text = f"Total £{total}")
   totalLbl.pack(pady = 20)

   forcastLbl = ctk.CTkLabel(root, text = f"Forcast £{forcast}")
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
       "power": "57",
       "month": "July"
    }

    config["Payment Dates"] = {
       "rent": "1",
       "council tax": "1",
       "power": "15",
       "wifi": "2"
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
      forcast = config["Settings"]["forcast"]

      return forcast
   
   if option == 3:
      config = configparser.ConfigParser()
      config.read("config.ini")
      pay = config["Settings"]["pay"]

      return pay
   
   if option == 4:
      config = configparser.ConfigParser()
      config.read("config.ini")
      tax = config["Settings"]["tax"]

      return tax
   
   if option == 5:
      config = configparser.ConfigParser()
      config.read("config.ini")
      rent = config["Settings"]["rent"]

      return rent
   
   if option == 6:
      config = configparser.ConfigParser()
      config.read("config.ini")
      councilTax = config["Settings"]["council tax"]

      return councilTax
   
   if option == 7:
      config = configparser.ConfigParser()
      config.read("config.ini")
      wifi = config["Settings"]["wifi"]

      return wifi
   
   if option == 8:
      config = configparser.ConfigParser()
      config.read("config.ini")
      power = config["Settings"]["power"]

      return power
   
   if option == 9:
      config = configparser.ConfigParser()
      config.read("config.ini")
      month = config["Settings"]["month"]

      return month

def calcPay(hours):
   
   payPerHour = readIni(3)
   pay = hours * payPerHour

   calcForcast(pay)
   

def addMoney(root):
   
   subWin = ctk.CTkToplevel(root)
   subWin.geometry("400x200")
   subWin.title("Add Money")

   return

def calcForcast(pay):
   
   currentForcast = readIni(2)
   rent = readIni(5)
   tax = readIni(4)
   councilTax = readIni(6)
   wifi = readIni(7)
   power = readIni(8)

   netPay = pay * (1 - tax / 100)
   expenses = rent + councilTax + power + wifi

   newForcast = currentForcast + netPay

def checkMonth():
   
   currentMonth = readIni(9)

def schedule(root):
   
   subWin = ctk.CTkToplevel(root)
   subWin.geometry("400x200")
   subWin.title("Add Hours")

   label = ctk.CTkLabel(subWin, text = "Please enter your weeks schedule")
   label.pack(pady = 20)

   hours = ctk.CTkEntry(subWin, placeholder_text= "Hours this week?")
   hours.pack(pady = 20)

   def submit():
      val = hours.get()
      calcPay(val)
      subWin.destroy()

   submitBtn = ctk.CTkButton(subWin, text = "Submit", command = submit())
   submitBtn.pck(pady = 20)

if __name__ == "__main__":
   main()