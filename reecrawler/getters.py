import requests

# URL constants for the REEC API Requests.
TRIALS_LIST_GETSTUDIOS = ["https://reec.aemps.es/reec-services/json/getestudios",
                         "https://reec.aemps.es/reec-services/xml/getestudios"]
TRIALS_LIST_STUDIOS = "https://reec.aemps.es/reec-services/estudios"
TRIALS_GETDETAILS = ["https://reec.aemps.es/reec-services/json/detalle",
                         "https://reec.aemps.es/reec-services/xml/detalle"]

        
def get_trials_list(from_date, to_date = None, format = "json"):
    """Function to extract all the trials published in REec or those that meet the criteria defined in the search parameters.

    Args:
        from_date ([type]): Correct format: dd-MM-yyyy
        to_date ([type]): Correct format: dd-MM-yyyy. Not Implemented yet.
        format (str, optional): Type of response: "xml" or "json". Only "json" is implemented. Defaults to "json".
    """
    if to_date is not None:
        # When to_date is not None, we use the TRIALS_LIST_STUDIOS constant, that use another date format.
        # EXAMPLE QUery http://reec.aemps.es/reec-services/estudios/?fechadesde=01/11/2020&fechahasta=01/01/2021
        from_date = from_date.replace("-", "/")
        to_date = to_date.replace("-", "/")
        url = TRIALS_LIST_STUDIOS + "/?fechadesde=" + from_date + "&fechahasta=" + to_date
    else:
        url = TRIALS_LIST_GETSTUDIOS[0] + "/" + from_date
         
    r = requests.get(url) 
    data = r.json()

    return data

def get_trial_details(trial_id, format = "json"):
    """Function to extract the complete information of a study defined by "trial_id" published in REEC.

    Args:
        trial_id ([type]): Code that identifies the clinical trial from REec.
        format (str, optional): Type of response: "xml" or "json". Only "json" is implemented. Defaults to "json".
    """
    url = TRIALS_GETDETAILS[0] + "/" + trial_id
    r = requests.get(url)  
    data = r.json()

    return data

