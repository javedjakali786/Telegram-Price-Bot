import json
import urllib.request
from lists import nstlist

def handleCoingecko(message, resultMessage):
    if message.text.upper() in nstlist:
        upperMessage = message.text.upper()
        user_agent = 'Mozilla/5.0'
        url = "https://api.coingecko.com/api/v3/coins/ninja-squad/"
        headers={'User-Agent':user_agent,} 
        request=urllib.request.Request(url,None,headers)
        response = urllib.request.urlopen(request)
        data = response.read()
        output = json.loads(data)

        if resultMessage != "":
            resultMessage += "\n"
        resultMessage += "Sushiswap -> " + upperMessage + ': $' + format(float(output['market_data']['current_price']['usd'])) + "  %{:.2f}".format(float(output['market_data']['price_change_percentage_24h']))        
    return resultMessage