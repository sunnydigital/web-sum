import json
import requests
from bs4 import BeautifulSoup

import quart
import quart_cors
from quart import request

app = quart_cors.cors(quart.Quart(__name__), allow_origin='https://chat.openai.com')

async def get_links(url):
    response = await requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links

def main():
    app.run(debug=True, host='0.0.0.0', port=5003)

if __name__ == '__main__':
    main()