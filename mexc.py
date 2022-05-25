import json
import urllib.request
from lists import mexclist

def handleMexc(message, resultMessage):
    if message.text.upper() in mexclist:
        upperMessage = message.text.upper()
        user_agent = 'Mozilla/5.0'
        url = "https://www.mexc.com/open/api/v2/market/ticker?symbol=" + upperMessage + "_USDT"
        headers={'User-Agent':user_agent,} 
        request=urllib.request.Request(url,None,headers)
        response = urllib.request.urlopen(request)
        data = response.read()
        output = json.loads(data)

        if resultMessage != "":
            resultMessage += "\n"
        else:
            resultMessage += "Mexc -> " + upperMessage + ': $' + format(float(output['data'][0]['last'])) + "  %{:.2f}".format(100*float(output['data'][0]['change_rate']))
    return resultMessage        