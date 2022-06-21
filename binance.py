import json
import urllib.request
from lists import binancelist

def handleBinance(message, resultMessage):
    if (message.text.upper() in binancelist) or (message.text.upper()=="USDT") or (message.text.upper() == "ETHBTC"):
        upperMessage = message.text.upper()
        user_agent = 'Mozilla/5.0'
        url = "https://api.binance.com/api/v3/ticker/24hr?symbol=" + upperMessage + "USDT"
        if upperMessage == "USDT":
            url = "https://api.binance.com/api/v3/ticker/24hr?symbol=" + "USDT" + "TRY"
        headers={'User-Agent':user_agent,}
        if upperMessage == "ETHBTC":
            url = "https://api.binance.com/api/v3/ticker/24hr?symbol=" + "ETH" + "BTC"
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

    if message.text.upper()=="GAINERS" or message.text.upper()=="LOSERS":
        changePercentList = []
        user_agent = 'Mozilla/5.0'
        url = "https://api.binance.com/api/v3/ticker/24hr"
        headers={'User-Agent':user_agent,}
        request=urllib.request.Request(url,None,headers)
        response = urllib.request.urlopen(request)
        data = response.read()
        output = json.loads(data)
        for i in binancelist:
            upperMessage = i + "USDT"
            index = [j for j,_ in enumerate(output) if _['symbol'] == upperMessage][0]
            changePercentList.append([i,float(output[index]['lastPrice']),float(output[index]["priceChangePercent"])])

        if resultMessage != "":
            resultMessage += "\n"
        if message.text.upper()=="GAINERS":
            changePercentList.sort(key= lambda coin: coin[2], reverse=True)
            resultMessage += "Binance Top Gainers:\n"
        if message.text.upper()=="LOSERS":
            changePercentList.sort(key= lambda coin: coin[2])
            resultMessage += "Binance Top Losers:\n"

        resultMessage += changePercentList[0][0] + ': ' + format(changePercentList[0][1]) + "  %{:.2f}".format(float(changePercentList[0][2])) + "\n"
        resultMessage += changePercentList[1][0] + ': ' + format(changePercentList[1][1]) + "  %{:.2f}".format(float(changePercentList[1][2])) + "\n"
        resultMessage += changePercentList[2][0] + ': ' + format(changePercentList[2][1]) + "  %{:.2f}".format(float(changePercentList[2][2])) + "\n"
        resultMessage += changePercentList[3][0] + ': ' + format(changePercentList[3][1]) + "  %{:.2f}".format(float(changePercentList[3][2])) + "\n"
        resultMessage += changePercentList[4][0] + ': ' + format(changePercentList[4][1]) + "  %{:.2f}".format(float(changePercentList[4][2]))
    return resultMessage