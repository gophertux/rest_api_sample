#TODO: Create route launchpad_info
#TODO: Create obj exposing required attrs
#TODO: error handling between middleware and front-end
#TODO: README and requirements file

#launchpad_id = id; launchpad_name = full_name; launchpad_status = status
#TODO: logging, db

from flask import Flask
app = Flask(__name__)
from flask import request 

import middleware
import json

@app.route('/v0/launchpad_info')
def return_launchpad_info():
    response = middleware.launchpad_info() #middleware.retrieve_launchpad_info(request.args.get('filter', ''))
    
    return json.dumps(response.site_stats)
