# reecapi <img src="www/reecapi_logo.png" align="right"  height = 150/>

<!-- badges: start -->

<!-- badges: end -->

This package provides a list of functions to facilitate access to the
data offered by [Registro Español de Estudios Clínicos](https://reec.aemps.es/reec/public/web.html) in its
[REST API](https://sede.aemps.gob.es/docs/Manual-Interaccion-REEC-Servicio-Extraccion-Datos-v1.pdf).



> REEC does not offer any support for this library, which has been developed individually by the author from the documentation shown by [REEC on its web site](https://sede.aemps.gob.es/docs/Manual-Interaccion-REEC-Servicio-Extraccion-Datos-v1.pdf). 

## Installation

You can install the latest version of reecapi from Pypi with the
following command.
``` python
# Install the PyPI version of the library
pip install reecapi
```

## Usage
Before using it, you must import the library module with the functions of interest:
```python
from reecapi.getters import *
```
The library has 4 functions to access the records of REEC:

 1. **get_trials_list(from_date, to_date = None, format = "json")** :Extract all the trials published in REec or those that meet the criteria defined in the search parameters with the function:
    - *from_date*(str):  Date from which you want to start downloading data. Correct format: "dd-MM-yyyy"
    - *to_date* (str, Optional): Date to which you want to download data. Correct format: "dd-MM-yyyy"
    - *format* (str, Optional):  Type of response: "xml" or "json". Only "json" is implemented. Defaults to "json".

    ``` python 
    # Get Clinical Trial Records from "01-01-2020" to "30-01-2020"
    get_trials_list(from_date = "01-01-2020", to_date = "30-01-2020")
    # Get Clinical Trial Records from "01-01-2020" until today.
    get_trials_list(from_date = "01-01-2020")
    ```
2. **get_trial_details(trial_id, format = "json")** :Extract all the trials published in REec or those that meet the criteria defined in the search parameters with the function:
    - *trial_id* (str): Code that identifies the clinical trial from REec.
    - *format* (str, Optional):  Type of response: "xml" or "json". Only "json" is implemented. Defaults to "json".
    ``` python 
    # Get the Clinical Trial Record with id "2013-000491-14"
    get_trial_details(trial_id ="2013-000491-14")
    ```
3. **get_hospital_list(hospital_id = None, format = "json")** :Extract all the trials published in REec or those that meet the criteria defined in the search parameters with the function:
    - *hospital_id* (numeric, Optional): Hospital code. Defaults to None.
    - *format* (str, Optional):  Type of response: "xml" or "json". Only "json" is implemented. Defaults to "json".
    ``` python 
    # Get the whole list of hospitals registered in the Ministry dictionary.
    get_hospital_list()
    # Get the list of hospitals registered in the Ministry dictionary with the hospital_id="25812"
    get_hospital_list(hospital_id=25812)
    ```
4. **get_primary_care_list(center_id = None, format = "json")** :Extract all the trials published in REec or those that meet the criteria defined in the search parameters with the function:
    - *center_id* (numeric, optional): Primary primary care center code. Defaults to None.
    - *format* (str, Optional):  Type of response: "xml" or "json". Only "json" is implemented. Defaults to "json".
    ``` python 
     # Get the whole list of primary care centers registered in the Ministry dictionary.
    get_primary_care_list()
    # Get the list of primary care centers registered in the Ministry dictionary with the center_id="25812"
    get_primary_care_list(center_id=25812)
    ```



## License
MIT License

## You may also like…

  - [Noytext](https://github.com/luisgasco/Ropensky) - A web-based platform for annotating short-text documents to be used in applied     text-mining based research.
  - [ropenskyr](https://github.com/luisgasco/openskyr) - R library to get data from OpenSky Network API.
 

-------


> [luisgasco.es](http://luisgasco.es/) · GitHub:
> [@luisgasco](https://github.com/luisgasco) · Twitter:
> [@luisgasco](https://twitter.com/luisgasco) · Facebook: [Luis Gascó
> Sánchez
> page](https://www.facebook.com/Luis-Gasco-Sanchez-165003227504667)
