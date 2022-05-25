import json
import urllib.request
from lists import binancelist

def handleBinance(message, resultMessage):
    if message.text.upper() in binancelist:
        upperMessage = message.text.upper()
        user_agent = 'Mozilla/5.0'
        url = "https://api.binance.com/api/v3/ticker/24hr?symbol=" + upperMessage + "USDT"
        if upperMessage == "USDT":
            url = "https://api.binance.com/api/v3/ticker/24hr?symbol=" + "USDT" + "TRY"
        headers={'User-Agent':user_agent,}
        if upperMessage == "LUNA":
            url = "https://api.binance.com/api/v3/ticker/24hr?symbol=" + "LUNA" + "BUSD"
        if upperMessage == "UST":
            url = "https://api.binance.com/api/v3/ticker/24hr?symbol=" + "UST" + "BUSD"
        headers={'User-Agent':user_agent,} 
        request=urllib.request.Request(url,None,headers)
        response = urllib.request.urlopen(request)
        data = response.read()
        output = json.loads(data)
        
        symbol = ""
        if upperMessage == "USDT":
            symbol = "₺"
        else:
            symbol = "$"

        if resultMessage != "":
            resultMessage += "\n"
        resultMessage += "Binance -> " + upperMessage + ': ' + symbol + format(float(output['lastPrice'])) + "  %{:.2f}".format(float(output['priceChangePercent']))
    return resultMessage