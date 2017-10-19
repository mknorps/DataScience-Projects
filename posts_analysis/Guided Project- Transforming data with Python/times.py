import read
from dateutil.parser import parse
import datetime

df = read.load_data()

def hour_parser(timestamp):
    datetime = parse(timestamp)
    return datetime.hour
  
df["submition_hours"] = df["submission_time"].apply(hour_parser)    

submition_hours = df["submition_hours"].value_counts()

print (submition_hours)