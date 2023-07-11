import io
import pdfplumber

import httpx
from bs4 import BeautifulSoup

import quart
import quart_cors

app = quart_cors.cors(quart.Quart(__name__))


@app.get('/summarize/<path:url>')
async def summarize(url):
  try:

    ## For the below blocks, I have NO idea why this is..? ChatGPT seems to think the error is on the side of OpenAI, so will check to be sure
    url = url.replace(
      ':/', '://'
    ) if '://' not in url else url  ## Checks for url error where a "/" will be missing

    IS_PDF_ = True if url[
      -4:] == '.pdf' else False  ## Environment variable to decide whether to process a PDF or URL

    async with httpx.AsyncClient() as client:
      response = await client.get(url)

    ## The question now is how to handle the token-count limitation and difference thereof between ChatGPT (GPT 3.5) set at 4,096 tokens and the 8,192 tokens available to GPT 4.

    text = process_pdf(response) if IS_PDF_ else process_url(
      response)  ## Processes text whether PDF or URL

    return quart.jsonify({'text':
                          text}), 200  ## Return JSON of the processed text

  except Exception as e:
    error_message = str(e)
    return quart.jsonify({
      'error': 'Unexpected error',
      'message': error_message
    }), 500


def process_pdf(response):
  text = ''
  pdf_file = io.BytesIO(response.content)

  with pdfplumber.open(pdf_file) as pdf:
    for page in pdf.pages:
      text += page.extract_text()

  return text


def process_url(response):
  soup = BeautifulSoup(response.text, 'html.parser')

  for script in soup(['script', 'style', 'meta', 'head', 'title']):
    script.extract()

  text = str(soup)  ## Simpler in this iteration to just return a string

  return text


@app.get('/')
async def home():
  return await quart.render_template('index.html')


@app.get('/about')
async def about():
  return await quart.render_template('about.html')


@app.get('/suggestions')
async def suggestions():
  return await quart.render_template('suggestions.html')


@app.get('/contact')
async def contact():
  return await quart.render_template('contact.html')


@app.get('/.well-known/logo.png')
async def plugin_logo():
  filename = './.well-known/logo.png'
  return await quart.send_file(filename, mimetype='image/png')


@app.get('/.well-known/ai-plugin.json')
async def plugin_mainfest():
  with open('./.well-known/ai-plugin.json') as f:
    text = f.read()
    return quart.Response(text, mimetype='application/json')


@app.get('/.well-known/openapi.yaml')
async def openapi_spec():
  with open('./.well-known/openapi.yaml') as f:
    text = f.read()
    return quart.Response(text, mimetype='text/yaml')


def main():
  app.run(host='0.0.0.0', port=5003)


if __name__ == '__main__':
  main()
