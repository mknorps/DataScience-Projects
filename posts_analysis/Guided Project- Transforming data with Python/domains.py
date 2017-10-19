import read
import pandas as pd

df = read.load_data()

def remove_subdomain(s):
    if pd.notnull(s):
        splitted = str(s).split(".")
        splitted_length = len(splitted)
        return splitted[splitted_length-2]+"."+splitted[splitted_length-1]

url_count = df["url"].value_counts()
url_count_with_subdomens = df["url"].apply(remove_subdomain).value_counts()





