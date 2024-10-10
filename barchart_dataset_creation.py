import pandas as pd
import re

# Function to clean country names (e.g., remove text inside parentheses)
def clean_country_name(name):
    # Use regex to remove anything in parentheses
    return re.sub(r'\s*\(.*?\)\s*', '', name).strip()

# Load the datasets with the provided file names
gdp_df = pd.read_csv('gdp-per-capita-worldbank.csv')         # Dataset with GDP per capita
poverty_df = pd.read_csv('subset_poverty_data.csv')          # Dataset with poverty rate
population_df = pd.read_csv('population-and-demography.csv') # Dataset with population

# Apply the clean_country_name function to standardize country names in all datasets
gdp_df['Country'] = gdp_df['Country'].apply(clean_country_name)
poverty_df['Country'] = poverty_df['Country'].apply(clean_country_name)
population_df['Country'] = population_df['Country'].apply(clean_country_name)

# Filter for years between 1991 and 2022 in all datasets
gdp_df = gdp_df[(gdp_df['Year'] >= 1991) & (gdp_df['Year'] <= 2022)]
poverty_df = poverty_df[(poverty_df['Year'] >= 1991) & (poverty_df['Year'] <= 2022)]
population_df = population_df[(population_df['Year'] >= 1991) & (population_df['Year'] <= 2022)]

# Merge the datasets on 'Country' and 'Year'
merged_df = pd.merge(gdp_df, poverty_df, on=['Country', 'Year'], how='outer')
merged_df = pd.merge(merged_df, population_df, on=['Country', 'Year'], how='outer')

# Drop the 'Code_x' column if it exists
if 'Code_x' in merged_df.columns:
    merged_df.drop('Code_x', axis=1, inplace=True)

if 'Code_y' in merged_df.columns:
    merged_df.drop('Code_y', axis=1, inplace=True)

# Inspect the merged data to ensure it's correct
print(merged_df.head())

# Save the cleaned and merged data to a new CSV file
merged_df.to_csv('merged_poverty_gdp_population.csv', index=False)
