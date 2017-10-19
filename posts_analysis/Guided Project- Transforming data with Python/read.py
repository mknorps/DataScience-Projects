import pandas as pd


def load_data():
    columns = ["submission_time","upvotes","url","headline"]
    stories = pd.read_csv("hn_stories.csv",header=None,\
                      names=columns,index_col=False)
    return stories

if __name__ == "__main__":
    data = load_data()
    print(data.head())