import json
import urllib.request
from lists import currencylist

def handleCurrency(message, resultMessage):
    if message.text.upper() in currencylist:
        user_agent = 'Mozilla/5.0'
        url = "https://www.bloomberght.com/doviz/dolar"
        headers={'User-Agent':user_agent,} 
        request=urllib.request.Request(url,None,headers)
        response = urllib.request.urlopen(request)
        data = str(response.read())
        index = data.find('"son_fiyat"  data-secid="USDTRY Curncy">')
        if resultMessage != "":
            resultMessage += "\n"
        resultMessage += ('Dolar: ₺' + data[index+40:index+46])
    return resultMessage
