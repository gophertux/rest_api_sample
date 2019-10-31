from flask import Flask
app = Flask(__name__)
from flask import request 

import json
import logging
import middleware

#TODO: consider whether I want to run flake8

"""
    This route allows a user to query for launchpad information. It is fulfilled
    via a middle abstraction to preserve modularity and decouple this from the 
    system handling the request
"""
@app.route('/v0/launchpad_info')
def return_launchpad_info():
    launchpad_info = middleware.LaunchpadInfo(request.args)
    url = request.url

    if launchpad_info.status_code == 400:
        return json.dumps(
            {"msg": f"Request {url} is invalid. Please check your syntax"})
    elif launchpad_info.status_code != 200:
        return json.dumps({"msg": "internal server error - please check the logs"}), 500

    return json.dumps(launchpad_info.site_stats), 200 
