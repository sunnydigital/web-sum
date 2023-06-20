import json

import quart
import quart_cors
from quart import request

app = quart_cors.cors(quart.Quart(__name__), allow_origin='https://chat.openai.com')



def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()