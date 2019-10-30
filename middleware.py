import requests
import os 

url = os.getenv("LAUNCHPAD_URL")

#This function allows us to modularize how we collect data, so we can easily
#change what function is called from our launchpad_info class, which represents
#our data model.
def retrieve_data_from_spacex_api():
    raw_launch_data = (requests.get(url)).json()
    site_stats = []

    for launch in raw_launch_data:
        harvested_data = {
            "launchpad_id":     launch["id"],
            "launchpad_name":   launch["full_name"],
            "launchpad_status": launch["status"]
        }
    
        site_stats.append(harvested_data)

    return site_stats

#TODO: this will be used when we migrate from using the API directly to 
#instead retrieving data from a DB
def retrieve_data_from_database():
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
class launchpad_info():
    def __init__(self):
        self.site_stats = retrieve_data_from_spacex_api() 
        print(self.site_stats)


    #if filter == None:
    #    return requests.get(url) 
    #else: 
    #    return requests.get(url + "?flight_number=" + filter)
    

if __name__ == "__main__":
    launchpad_info()
