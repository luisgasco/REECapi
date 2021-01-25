from reecapi import getters

def test_get_trials_list():
    assert type(getters.get_trials_list(from_date = "01-01-2021")["estudio"]) is list 
    assert type(getters.get_trials_list(from_date = "11-11-2020", to_date = "11-12-2020")["estudio"]) is list

# def test_get_trials_list():
#     # TO BE DONE
