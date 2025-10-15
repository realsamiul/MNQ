import pandas as pd
import numpy as np

# Define file paths using the known absolute paths
DATA_PATH = "D:/KP Apps/MonarqAI/final flourish/data/processed/"
NIGHTLIGHT_FILE = DATA_PATH + "dhaka_nightlights_2022_2025.csv"

# Load the dataset
nightlight_df = pd.read_csv(NIGHTLIGHT_FILE)

# Create the final dataframe with the required columns
nightpulse_df = pd.DataFrame({
    'date': nightlight_df['date'],
    'ward': 'Dhaka',  # Add ward column
    'night_index': nightlight_df['nightlight_radiance'],
    'day_index': np.nan,  # Add placeholder
    'delta': np.nan,  # Add placeholder
    'viirs_mean': np.nan,  # Add placeholder
    'osm_poi': np.nan,  # Add placeholder
    'bkash_volume': np.nan  # Add placeholder
})

# Save the dataframe to a CSV file
nightpulse_df.to_csv("assets/data/nightpulse.csv", index=False)

print("nightpulse.csv created successfully.")
