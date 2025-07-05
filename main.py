import sys
import os
import customtkinter as ctk
import configparser
import datetime

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

def getDate():
   
   today = datetime.date.today()
   return today.strftime("%d")  

def readIni(option):
    keys = {
        1: "total",
        2: "forcast",
        3: "pay",
        4: "tax",
        5: "rent",
        6: "council tax",
        7: "wifi",
        8: "power",
        9: "month"
    }

    config = configparser.ConfigParser()
    config.read("config.ini")

    key = keys.get(option)
    if key and "Settings" in config and key in config["Settings"]:
        return config["Settings"][key]
    else:
        return None

def calcPay(hours):
   
   payPerHour = convertToInt(readIni(3))
   
   pay = hours * payPerHour

   return pay

def addMoney(root):
   
   subWin = ctk.CTkToplevel(root)
   subWin.geometry("400x200")
   subWin.title("Add Money")

   return

def checkPayemntDate(option):

    keys = {
        1: "rent",
        2: "council tax",
        3: "wifi",
        4: "power",
    }

    config = configparser.ConfigParser()

    config.read("config.ini")

    key = keys.get(option)
    if key and "Payment Dates" in config and key in config["Payment Dates"]:
        return config["Payment Dates"][key]
    else:
        return None

def convertToInt(valStr):
   try:
        val = float(valStr)
        return val
        
   except (TypeError, ValueError):
        val = 0.0  # fallback if total is missing or invalid
        return val

def updateForcast(forcast):
   
   print(forcast)
   
   config = configparser.ConfigParser()
   config.read("config.ini")

   if "Settings" not in config:
        config["Settings"] = {}
    
   config["Settings"]["forcast"] = str(forcast)  # configparser stores values as strings
    
   with open("config.ini", "w") as configfile:
    config.write(configfile)
   

def calcForcast(pay, r, ct, w, p):
   
    date = getDate()
    currentForcast = convertToInt(readIni(2))

    rent = convertToInt(readIni(5))
    rentDate = checkPayemntDate(1)

    tax = convertToInt(readIni(4))

    councilTax = convertToInt(readIni(6))
    councilDate = checkPayemntDate(2)

    wifi = convertToInt(readIni(7))
    wifiDate = checkPayemntDate(3)

    power = convertToInt(readIni(8))
    powerDate = checkPayemntDate(4)

    #netPay = pay * (1 - tax / 100)
   
    if r:  # Rent checkbox is selected
        currentForcast -= rent
    if ct:  # Council Tax checkbox is selected
        currentForcast -= councilTax
    if w:  # Wifi checkbox is selected
        currentForcast -= wifi
    if p:  # Power checkbox is selected
        currentForcast -= power
    
    newForcast = currentForcast + pay
    print(newForcast)

    updateForcast(newForcast)

def checkMonth():
   
   currentMonth = readIni(9)

def schedule(root):
    subWin = ctk.CTkToplevel(root)
    subWin.geometry("400x200")
    subWin.title("Add Hours")

    label = ctk.CTkLabel(subWin, text="Please enter your week's schedule")
    label.pack(pady=20)

    hours = ctk.CTkEntry(subWin, placeholder_text="Hours this week?")
    hours.pack(pady=20)

    r = ctk.BooleanVar()
    ct = ctk.BooleanVar()
    w = ctk.BooleanVar()
    p = ctk.BooleanVar()

    rent = ctk.CTkCheckBox(subWin, text = "Rent", variable= r)
    rent.pack(pady=20)

    councilTax = ctk.CTkCheckBox(subWin, text = "Council Tax", variable= ct)
    councilTax.pack(pady=20)

    wifi = ctk.CTkCheckBox(subWin, text = "Wifi", variable= w)
    wifi.pack(pady=20)

    power = ctk.CTkCheckBox(subWin, text = "Power", variable= p)
    power.pack(pady=20)

    def submit():
        val = convertToInt(hours.get())
        pay = calcPay(val)

        rState = r.get()     
        ctState = ct.get()
        wState = w.get()
        pState = p.get()

        calcForcast(pay, rState, ctState, wState, pState)

        subWin.destroy()

    submitBtn = ctk.CTkButton(subWin, text="Submit", command=submit)
    submitBtn.pack(pady=20)

if __name__ == "__main__":
   main()