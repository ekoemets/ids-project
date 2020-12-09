import pandas as pd

def load_dataset(path_to_csv, *args, **kwargs):
    """
    Wrapper method for loading the dataset as csv.
    """
    return pd.read_csv(path_to_csv, *args, **kwargs)

def save_dataset(df, save_dir, *args, **kwargs):
    """
    Wrapper method for saving the dataset as csv.
    Ignores index on saving.
    """
    df.to_csv(save_dir, *args, index=False,**kwargs)

def clean_data(df):
    """
    Removes unwanted rows from the initial raw kickstarter
    projects dataset.
    
    Returns new dataset.
    """
    # Use the value conversions done by the external API
    data = df.drop(columns=["goal", "usd pledged", "pledged"])

    # Remove projects that were ongoing at the time or cancelled
    data = data.loc[(data["state"] == "successful") | (data["state"] == "failed")]
    
    # Remove N/A values
    data = data.dropna()
    
    # Remove incorrect country codes
    data = data.loc[data["country"].str.len() == 2]

    # Remove projects that had only one backer and were succesful
    data = data.drop(data[(data["backers"] == 1) & 
            (data["usd_pledged_real"] >= data["usd_goal_real"])].index)
    
    # Remove projects with really small goal amount
    data = data.drop(data[data["usd_goal_real"] < 20].index)

    # Remove projects with really high goal amount that had almost no backers
    data = data.drop(data[(data["usd_goal_real"] > 1000000) & (data["backers"] < 3)].index)

    return data

