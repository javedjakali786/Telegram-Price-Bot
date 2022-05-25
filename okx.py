import json
import urllib.request
from lists import okxlist

def handleOkx(message, resultMessage):
    if message.text.upper() in okxlist:
        upperMessage = message.text.upper()
        user_agent = 'Mozilla/5.0'
        url = "https://www.okx.com/api/v5/market/ticker?instId=" + upperMessage + "-USDT"
        headers={'User-Agent':user_agent,} 
        request=urllib.request.Request(url,None,headers)
        response = urllib.request.urlopen(request)
        data = response.read()
        output = json.loads(data)
        price = float(output['data'][0]['last'])
        change = 100*(price-float(output['data'][0]['open24h']))/float(output['data'][0]['open24h'])
        if resultMessage != "":
            resultMessage += "\n"
        resultMessage += "Okx -> " + upperMessage + ': $' + "{:.4f}".format(price) + "  %{:.2f}".format(change)
    return resultMessage