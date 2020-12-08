import pandas as pd
import config as cfg

def load_dataset(path_to_csv):
    return pd.read_csv(path_to_csv)

def save_dataset(df, save_dir):
    df.to_csv(save_dir)

def clean_data(df):
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


if __name__ == "__main__":
    raw_data_path = cfg.data_dir / 'raw' / 'ks-projects.csv'
    print(f"Reading data from: {raw_data_path}")
    df = load_dataset(raw_data_path)
    print(f"Dataset shape before cleaning: {df.shape} ")
    df = clean_data(df)
    print(f"Dataset shape after cleaning: {df.shape}")
    processed_data_path = cfg.data_dir / 'processed' / '01-ks-projects-clean.csv'
    print(f"Saving cleaned data to {processed_data_path}")
    save_dataset(df, processed_data_path)

