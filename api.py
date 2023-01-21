import requests
import json

url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

currency_1="EUR"
currency_2="USD"
amount="1000"

querystring = {"from":currency_1,"to":currency_2,"amount":amount}

headers = {
	"X-RapidAPI-Key": "eea352303amsh5f404adb07dc2ebp1cdaa1jsn297be566125f",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)


database = json.loads(response.text)
converted_amount = database['result']['convertedAmount']
formatted = "{:,.2f}".format(converted_amount)

print(converted_amount, formatted)