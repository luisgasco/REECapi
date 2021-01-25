import requests
from reecapi.constants import *

def get_trials_list(from_date, to_date = None, format = "json"):
    """Function to extract all the trials published in REec or those that meet the criteria defined in the search parameters.

    Args:
        from_date (str): Date from which you want to start downloading data. Correct format: dd-MM-yyyy
        to_date (str): Optional. Date to which you want to download data. Correct format: dd-MM-yyyy.
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
        trial_id (str): Code that identifies the clinical trial from REec.
        format (str, optional): Type of response: "xml" or "json". Only "json" is implemented. Defaults to "json".
    """
    url = TRIALS_GETDETAILS[0] + "/" + str(trial_id)
    r = requests.get(url)  
    data = r.json()

    return data

def get_hospital_list(hospital_id = None, format = "json"):
    """Function to obtain the list of all hospital centers listed in the ministry's dictionaries

    Args:
        hospital_id (numeric, optional): Hospital code. Defaults to None.
        format (str, optional): Type of response: "xml" or "json". Only "json" is implemented. Defaults to "json".
    """
    # If hospital_id is None, get all hospitals present in the database
    if hospital_id is None:
        url = HOSPITAL_GET_LIST[0]
    else:
        url =HOSPITAL_GET_LIST[0] + "/" + str(hospital_id)
    
    r = requests.get(url)  
    data = r.json()

    return data

def get_primary_care_list(center_id = None, format = "json"):
    """Function to obtain the list of all primary care centers listed in the ministry's dictionaries

    Args:
        center_id (numeric, optional): Primary primary care center code. Defaults to None.
        format (str, optional): Type of response: "xml" or "json". Only "json" is implemented. Defaults to "json".
    """
    # If center_id is None, get all primary_centers present in the database
    if center_id is None:
        url = PRIMARY_CENTER_GET_LIST[0]
    else:
        url = PRIMARY_CENTER_GET_LIST[0] + "/" + str(center_id)
    
    r = requests.get(url)  
    data = r.json()

    return data
