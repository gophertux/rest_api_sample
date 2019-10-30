#TODO: error handling between middleware and front-end

from flask import Flask
app = Flask(__name__)
from flask import request 

import json
import logging
import middleware

@app.route('/v0/launchpad_info')
def return_launchpad_info():
    launchpad_info = middleware.launchpad_info() #middleware.retrieve_launchpad_info(request.args.get('filter', ''))

    if launchpad_info.status_code != 200:
        return json.dumps({"msg": "internal server error - please check the logs"}), 500
    #logging.info(json.dumps({
    #    "middleware_response": lp_info.site_stats
    #}))

    return json.dumps(launchpad_info.site_stats), 200 
