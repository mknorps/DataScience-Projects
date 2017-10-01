import pandas as pd

import numpy as np
import re


if __name__=="__main__":
    data = pd.read_csv("data/CRDC2013_14.csv")
    
    data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]
    all_enrollment = data["total_enrollment"].sum()
    
    enrollment_header = []
    enrollment_sums = []
    for column in data.columns:
        if re.match("^SCH_ENR_.._.",column):
            enrollment_header.append(column)
            enrollment_sums.append(data[column].sum())
    enrollment_series = pd.Series(enrollment_sums,enrollment_header)/all_enrollment
    
    print( enrollment_series)
    assert (np.isclose(1.0, enrollment_series.sum()))
    
    # data on races from 
    # https://en.wikipedia.org/wiki/Demography_of_the_United_States#Race_and_ethnicity
    races = pd.read_csv("data/races_US.csv", sep=";")
    
    assert (np.isclose(100.0, races["percent"].sum() ))
    
    for race in races["Race code"]:
        enrollment_series["SCH_ENR_"+race+"_M"] = 0.5*enrollment_series["SCH_ENR_"+race+"_M"]/races[races["Race code"]==race]["percent"]*100.0
        enrollment_series["SCH_ENR_"+race+"_F"] = 0.5*enrollment_series["SCH_ENR_"+race+"_F"]/races[races["Race code"]==race]["percent"]*100.0
        
    print (enrollment_series)
    
        
    
    
     
            

    