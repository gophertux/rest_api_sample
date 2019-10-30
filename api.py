#TODO: Create route launchpad_info
#TODO: Create obj exposing required attrs
#TODO: error handling between middleware and front-end
#TODO: README and requirements file

from flask import Flask
app = Flask(__name__)
from flask import request 

import middleware
import json

@app.route('/launchpad_info')
def return_launchpad_info():
    r = middleware.retrieve_launchpad_info(request.args.get('key', ''))

    return json.dumps(r.json())
