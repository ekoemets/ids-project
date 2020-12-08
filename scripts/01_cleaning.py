from idskicker import config, cleaning

raw_data_path = config.data_dir / 'raw' / 'ks-projects.csv'
print(f"Reading data from: {raw_data_path}")
df = cleaning.load_dataset(raw_data_path)
print(f"Dataset shape before cleaning: {df.shape} ")
df = cleaning.clean_data(df)
print(f"Dataset shape after cleaning: {df.shape}")
processed_data_path = config.data_dir / 'processed' / '01-ks-projects-clean.csv'
print(f"Saving cleaned data to {processed_data_path}")
cleaning.save_dataset(df, processed_data_path)

