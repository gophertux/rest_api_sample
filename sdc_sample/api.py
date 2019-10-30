from flask import Flask
app = Flask(__name__)
from flask import request 

import json
import logging
import middleware

@app.route('/v0/launchpad_info')
def return_launchpad_info():
    launchpad_info = middleware.launchpad_info(request.args)
    url = request.url

    if launchpad_info.status_code == 400:
        return json.dumps({"msg": f"Your request {url} was unsuccessful. Please check your query and try again"})
    elif launchpad_info.status_code != 200:
        return json.dumps({"msg": "internal server error - please check the logs"}), 500

    return json.dumps(launchpad_info.site_stats), 200 
