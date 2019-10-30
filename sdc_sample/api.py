from flask import Flask
app = Flask(__name__)
from flask import request 

import json
import logging
import middleware

@app.route('/v0/launchpad_info')
def return_launchpad_info():
    launchpad_info = middleware.launchpad_info(request.args)

    if launchpad_info.status_code != 200:
        return json.dumps({"msg": "internal server error - please check the logs"}), 500

    return json.dumps(launchpad_info.site_stats), 200 
