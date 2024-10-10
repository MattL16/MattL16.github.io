import pandas as pd

# Step 1: Read the CSV file
df = pd.read_csv('poverty-explorer.csv')

# Assuming 'df' is your DataFrame with many columns

# Specify the 3 columns you want to keep
columns_to_keep = ['Country', 'Year', 'Share below $6.85 a day']

# Create a new DataFrame with only these 3 columns
df_subset = df[columns_to_keep]

# Save the subset DataFrame to a CSV file
df_subset.to_csv('subset_poverty_data.csv', index=False)

print("Data saved to subset_data.csv")