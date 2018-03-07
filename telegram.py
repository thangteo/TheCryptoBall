import datetime
import json
import requests
import time
import urllib

# define  key/global variables
baseURL = "https://api.telegram.org/bot"

# send message through telegram bot
def send_message(text, chatID , token):
    text = urllib.parse.quote(text)
    url = baseURL + token + "/sendMessage?text={0}&chat_id={1}".format(text, chat_id)

# decode response into JSON object
def get_json(url):
    content = get_url(url)
    js = json.loads(content)
    return js
    
# send command and return response
def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content