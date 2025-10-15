import pandas as pd
import numpy as np

# Define file paths using the known absolute paths
DATA_PATH = "D:/KP Apps/MonarqAI/final flourish/data/processed/"
DENGUE_FILE = DATA_PATH + "bangladesh_dengue_cases_2022_2025.csv"
WEATHER_FILE = DATA_PATH + "dhaka_weather_2022_2025.csv"

# Load the datasets
dengue_df = pd.read_csv(DENGUE_FILE)
weather_df = pd.read_csv(WEATHER_FILE)

# Merge the dataframes
merged_df = pd.merge(dengue_df, weather_df, on='date', how='inner')

# Create the final dataframe with the required columns
health_causal_df = pd.DataFrame({
    'date': merged_df['date'],
    'district': 'Dhaka',  # Add district column
    'rain_mm': merged_df['rainfall'],
    'temp_c': merged_df['temperature'],
    'humidity': merged_df['humidity'],
    'dengue_cases': merged_df['dhaka_cases'],
    'mosquito_risk': np.nan  # Add placeholder for mosquito risk
})

# Save the dataframe to a CSV file
health_causal_df.to_csv("assets/data/health_causal.csv", index=False)

print("health_causal.csv created successfully.")
