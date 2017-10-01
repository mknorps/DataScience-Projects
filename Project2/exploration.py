import pandas as pd



if __name__=="__main__":
    data = pd.read_csv("data/CRDC2013_14.csv",encoding="Latin-1")

    JJ_data_count = data["JJ"].value_counts() 
#   SSM_data_count = data["SCH_STATUS_MAGNET"].value_counts() 
    SSM_data_count = data["SCH_STATUS_MAGNET"].value_counts() 
    #print ("JJ = ",JJ_data_count, "\n SCH_STATUS_MAGNET = ",SSM_data_count)
    
    #creating pivot tables
    pivot_exploration = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index=["JJ","SCH_STATUS_MAGNET"], aggfunc="sum")
    print(pivot_exploration)
    