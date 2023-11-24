import requests


proxies = {
    'https': 'https://'
             'x.x.x.x:yyyyy'    # ip address : port number
}

response = requests.get("https://ipinfo.io/json", proxies=proxies)
print(response.text)