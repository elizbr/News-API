import secrets
import requests

 
base_url = 'https://newsapi.org/v2/top-headlines'
params = {
    "q": "New Hampshire",    
    "apiKey": secrets.NEWSAPI_KEY
}

response = requests.get(base_url, params)
result = response.json()
for x in result['articles']:
    print(x['title'])
