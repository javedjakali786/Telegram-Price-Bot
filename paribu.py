import json
import urllib.request
from lists import paribulist

def handleParibu(message, resultMessage):
    if message.text.upper() in paribulist:
        lowerMessage = message.text.lower()
        upperMessage = message.text.upper()
        user_agent = 'Mozilla/5.0'
        url = "https://v3.paribu.com/app/initials/"
        headers={'User-Agent':user_agent,} 
        request=urllib.request.Request(url,None,headers)
        response = urllib.request.urlopen(request)
        data = response.read()
        output = json.loads(data)
        pair = lowerMessage + "-tl"
        if resultMessage != "":
            resultMessage += "\n"
        resultMessage += "Paribu -> " + upperMessage + ': ₺' + format(float(output['data']['ticker'][pair]['c'])) + "  %{:.2f}".format(float(output['data']['ticker'][pair]['p']))
    return resultMessage    
