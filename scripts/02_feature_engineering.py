from idskicker import features
from idskicker.config import data_dir
from idskicker.cleaning import load_dataset, save_dataset

dataset_path = data_dir / "processed" / "01-ks-projects-clean.csv"
print(f"Loading dataset from {dataset_path}")
df = load_dataset(dataset_path)
features.add_date_as_features(df, "deadline")
features.add_date_as_features(df, "launched")
features.add_time_as_features(df, "launched")
features.add_text_as_features(df, "name")
dataset_save_path = data_dir / "processed" / "02-ks-projects-engineered.csv"
print(f"Saving dataset to {dataset_save_path}")
save_dataset(df, dataset_save_path)




