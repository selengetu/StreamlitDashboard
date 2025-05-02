import pandas as pd
import numpy as np
import os

# Define custom property names
property_names = [
    "Villa Solara", "Casa Seraphina", "Villa Azure Cove", "The Marula Nest",
    "Villa Cielo Alto", "Whispering Palms Estate", "Villa Luna Blanca",
    "The Velvet Horizon", "Villa Élan Grove", "Casa del Mariposa",
    "The Golden Banyan", "Villa Sereno", "The Orchid Pavilion", "Villa Terra Nova",
    "Casa Aurora", "Villa Driftwood", "Sapphire Ridge Retreat", "Villa Olivetta"
]

input_dir = "real_csvs"
output_dir = "property_only_dummy_csvs"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith(".csv"):
        print(f"Updating Property Name in: {filename}")
        df = pd.read_csv(os.path.join(input_dir, filename))
        
        if "Property Name" in df.columns:
            unique_properties = df["Property Name"].dropna().unique()
            mapping = {original: np.random.choice(property_names) for original in unique_properties}
            df["Property Name"] = df["Property Name"].map(mapping)

        df.to_csv(os.path.join(output_dir, filename), index=False)
