from tkinter import Tk,ttk
from tkinter import*
import requests
import json


#Definitions des variables et configuration de la fenêtre.
col1='#a83e32' #red
col2='#ffffff' #white
col3='#ffe599' #yellow
col4='#000000' #black

currency = ['CAD', 'USD' , 'EUR' , 'GBP' , 'AUD' , 'INR' , 'CAD' , 'INR', 'NZF', 'CHF']
currency_rate = { 'EUR':1, 'USD':1.08,'CAD' :1.45, 'GBP':1.13, 'AUD':1.54,'INR':88.80,'NZF':1.79,'CHF':1.0}

gui = Tk()
gui.geometry('400x600')
gui.title('Currency Converter')
gui.configure(bg=col2)
gui.resizable(height=FALSE, width=FALSE)

#Fonction de convertion avec l'historique
def convert():
    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()

    try:
        amount = float(value.get())
        if type(amount) == float:
            error.config(text="")
    except:
        error.config(text="Please enter a number", fg="red")
    try:
        if combo1.get() == "" or combo2.get() == "":
            error.config(text="Please add a currency", fg="red")
    except:
        error.config(text="")
    try:
        if combo1.get() not in currency_rate or combo2.get() not in currency_rate:
            error.config(text="Please add a currency", fg="red")
    except:
        error.config(text="")
    output = float(amount)*(float(currency_rate[combo2.get()])/float(currency_rate[combo1.get()]))  
    result.config(text=output)
    
    historic.insert(END, (currency_1,"=>", currency_2, "=", output) )

 
#Gui

header = Frame(gui, width=400, height=70, bg=col3)
header.grid(row=0, column=0)

body = Frame(gui, width=400, height=500, bg=col2)
body.grid(row=1, column=0)

convert_app= Label(header, text="Currency converter", height=5, padx=70, pady=30, anchor=N, font=('Terminal 16 bold'), bg=col3, fg=col2)
convert_app.place(x=0, y=0)

result = Label(body, text="", width=25, height=2, pady=7, relief="solid", anchor=CENTER, font=('Terminal 15 bold'), bg=col2, fg=col1)
result.place(x=40 , y=20)

error= Label(body, text="", width=23, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Terminal 12 bold'), bg=col2, fg=col1)
error.place(x=90, y=90)

from_selector= Label(body, text="From", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Terminal 9'), bg=col2, fg=col4)
from_selector.place(x=78, y=110)
combo1= ttk.Combobox(body,width=5, justify=CENTER, font=('Terminal 12 bold'))
combo1['values'] = (currency)
combo1.place(x=78, y=130)

to_selector = Label(body, text="To", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Terminal 9'), bg=col2, fg=col4)
to_selector.place(x=200, y=110)
combo2= ttk.Combobox(body,width=5, justify=CENTER, font=('Terminal 12 bold'))
combo2['values'] = (currency)
combo2.place(x=200, y=130)

value = Entry(body, width=22,justify=CENTER, font=('Terminal 12 bold'), relief="solid")
value.place(x=70, y=180)

button_convert = Button(body,text="Converter", width=19, padx=5, height=1, bg=col3, fg=col2, font=("Terminal 12 bold"),command=convert)
button_convert.place(x=80, y=230)

historic_selector= Label(body, text="Historic", width=14, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Terminal 9'), bg=col2, fg=col4)
historic_selector.place(x=80,y=300)
historic = Listbox(body, width=30, height=9,  relief="solid", font=('Terminal 10 bold'), bg=col2, fg=col1,)
historic.place(x=60, y=320)


gui.mainloop()

