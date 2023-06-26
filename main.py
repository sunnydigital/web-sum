import json
import requests
from bs4 import BeautifulSoup
import waitress

import quart
from quart import send_file
import quart_cors
from quart import request

app = quart_cors.cors(quart.Quart(__name__),
                      allow_origin='https://chat.openai.com')

async def get_links(url):
  response = await requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  links = [a['href'] for a in soup.find_all('a', href=True)]
  return links

@app.get('/assets/logo.png')
async def plugin_logo():
  filename = 'logo.png'
  return await quart.send_file(filename, mimetype='image/png')

@app.get('/.well-known/ai-plugin.json')
async def plugin_mainfest():
  host = request.headers['Host']
  with open('./.well-known/ai-plugin.json') as f:
    text = f.read()
    return quart.Response(text, mimetype='application/json')

@app.get('/.well-known/openaip.yaml')
async def openapi_spec():
  host = request.headers['Host']
  with open('./.well-known/openapi.yaml') as f:
    text = f.read()
    return quart.Response(text, mimetype='text/yaml')

def main():
  app.run(debug=True, host='0.0.0.0', port=8080)

if __name__ == '__main__':
  main()