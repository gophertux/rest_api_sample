import json
import logging
import os 
import requests

base_url = os.getenv("LAUNCHPAD_URL")
logging.basicConfig(filename="output.log", level=logging.INFO)

#This function allows us to modularize how we collect data, so we can easily
#change what function is called from our launchpad_info class, which represents
#our data model.
def retrieve_data_from_spacex_api(query_filter):
    query_url    = base_url
    query_params = query_filter.keys()

    #This is done to ensure we're able to filter data in the manner expected by
    #the third-party API
    if query_filter and "limit" not in query_params:
        logging.info(f"msg: No valid query parameter provided - API supports limit")
    
        return None, 400

    elif query_filter and "limit" in query_params:
        query_url = base_url + "?limit" + "=" + query_filter.get("limit")

    api_response = requests.get(query_url)
    site_stats   = []

    if api_response.status_code >= 400:
        logging.info(f"msg: API call to {url} did not complete successfully")

        return None, api_response.status_code
    
    raw_launch_data = api_response.json()

    for launch in raw_launch_data:
        harvested_data = {
            "launchpad_id":     launch["id"],
            "launchpad_name":   launch["full_name"],
            "launchpad_status": launch["status"]
        }
    
        site_stats.append(harvested_data)

    return site_stats, 200

#TODO: this will be used when we migrate from using the API directly to 
#instead retrieving data from a DB
#TODO: decide on comment about breaking abstraction to facility rapid dev
def retrieve_data_from_database(query_filter=None):
    pass

"""
    This class models the data received from the SpaceX API according to our
    specified format. It calls a function to populate its data model, since we
    expect to change our retrieval mechanism in the near future. This ensures
    that we should only need to update the function call to populate the model 
    with new data, and can develop these functions independently of one another.
    This should also make testing easier because the functions are more atomic
    and can also be tested in parallel for performance improvements, if desired 
"""
class LaunchpadInfo():
    def __init__(self, query_filter):
        self.site_stats, self.status_code = retrieve_data_from_spacex_api(
                query_filter.to_dict())
    

if __name__ == "__main__":
    LaunchpadInfo()
