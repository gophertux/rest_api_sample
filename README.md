# rest_api_sample

*****INITIAL SETUP*****
1. Clone the repository to your local machine
2. Run `pip install -r requirements.txt` in order to install all necessary dependencies

*****EXECUTION*****
1. All commands should be executed from the root of the project folder
2. Execute `EXPORT FLASK_APP=api.py` to set the environmental variable for the testing webserver
3. Execute `flask run --host=0.0.0.0` to bind the test webserver to an external port

*****USAGE*****
1. URL is `http://<localhost>:5000/v0/launchpad_info`
2. If desired, responses can be filtered by using "limit=<return value>" ex. `https://<localhost>:5000/v0/launchpad_info?limit=1`

