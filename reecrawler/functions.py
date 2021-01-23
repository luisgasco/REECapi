TRIALS_LIST_GETSTUDIOS = ["https://reec.aemps.es/reec-services/json/getestudios",
                         "https://reec.aemps.es/reec-services/xml/getestudios"]
TRIALS_LIST_STUDIOS = "https://reec.aemps.es/reec-services/estudios"]

TRIALS_GETDETAILS = ["https://reec.aemps.es/reec-services/json/detalle",
                         "https://reec.aemps.es/reec-services/xml/detalle"]
import requests

        

def get_trials_list(from_date, format = "json"):
    """Function to extract all the trials published in REec or those that meet the criteria defined in the search parameters.

    Args:
        from_date ([type]): Correct format: dd-MM-yyyy
        to_date ([type]): Correct format: dd-MM-yyyy
        format (str, optional): Type of response: "xml" or "json". Only "json" is implemented. Defaults to "json".
    """

    url = TRIALS_LIST_GETSTUDIOS[0] + "/" + from_date
    r = requests.get(url)  
    data = r.json()

    return data

"2020-000116-30"
def get_trial_details(trial_id, format = "json"):
    """Function to extract the complete information of a study defined by "trial_id" published in REEC.

    Args:
        trial_id ([type]): [description]
        format (str, optional): Type of response: "xml" or "json". Only "json" is implemented. Defaults to "json".
    """
    url = TRIALS_GETDETAILS[0] + "/" + trial_id
    r = requests.get(url)  
    data = r.json()

    return data

