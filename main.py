from tkinter import Tk,ttk
from tkinter import*
import requests
import json


#Definitions des variables pour les couleurs

col1='#DEEDEE' #green
col2='#ffffff' #white
col3='#ffe599' #yellow
col4='#000000' #black

window = Tk()
window.geometry('400x500')
window.title('Currency Converter')
window.configure(bg=col2)
window.resizable(height=FALSE, width=FALSE)

#Ajout de la Frame "Header"

header = Frame(window, width=400, height=70, bg=col1)
header.grid(row=0, column=0)

body = Frame(window, width=400, height=500, bg=col2)
body.grid(row=1, column=0)


#Style header

convert_app= Label(header, text="Currency converter", height=5, padx=100, pady=30, anchor=N, font=('Arial 16 bold'), bg=col1, fg=col2)
convert_app.place(x=0, y=0)

#Body

def convert():

    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()

    querystring = {"from":currency_1,"to":currency_2,"amount":amount}

    headers = {
	"X-RapidAPI-Key": "eea352303amsh5f404adb07dc2ebp1cdaa1jsn297be566125f",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

    response = requests.request("GET", url, headers=headers, params=querystring)


    database = json.loads(response.text)
    converted_amount = database['result']['convertedAmount']
    formatted = "{:,.2f}".format(converted_amount)
    result['text'] = formatted
    historic.insert(END, (currency_1,"=>", currency_2, "=", converted_amount) )

    print(converted_amount, formatted)


result = Label(body, text="", width=16, height=2, pady=7, relief="solid", anchor=CENTER, font=('Ivy 15 bold'), bg=col2, fg=col4)
result.place(x=80 , y=20)


currency = ['CAD', 'USD' , 'EUR' , 'JPY']

from_selector= Label(body, text="From", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 9'), bg=col2, fg=col4)
from_selector.place(x=78, y=110)
combo1= ttk.Combobox(body,width=5, justify=CENTER, font=('Ivy 12 bold'))
combo1['values'] = (currency)
combo1.place(x=78, y=130)

to_selector = Label(body, text="To", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 9'), bg=col2, fg=col4)
to_selector.place(x=200, y=110)
combo2= ttk.Combobox(body,width=5, justify=CENTER, font=('Ivy 12 bold'))
combo2['values'] = (currency)
combo2.place(x=200, y=130)

value = Entry(body, width=22,justify=CENTER, font=('Ivy 12 bold'), relief="solid")
value.place(x=70, y=180)

button_convert = Button(body,text="Converter", width=19, padx=5, height=1, bg=col3, fg=col2, font=("Ivy 12 bold"),command=convert)
button_convert.place(x=80, y=240)

historic_selector= Label(body, text="Historic", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 9'), bg=col2, fg=col4)
historic_selector.place(x=80,y=300)
historic = Listbox(body, width=20, height=2,  relief="solid", font=('Ivy 10 bold'), bg=col2, fg=col4)
historic.place(x=80, y=320)


window.mainloop()

