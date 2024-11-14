import pandas as pd

def clean_data(input_path, output_path):
    # Load the raw CSV file
    df = pd.read_csv(input_path)

    # Perform data cleaning (e.g., remove rows with missing values)
    df.dropna(inplace=True)

    # Save the cleaned data to a new CSV file
    df.to_csv(output_path, index=False)

    print("Data cleaned and saved successfully!")

# Use raw string for file paths
clean_data(r'C:\Users\Sweety\Documents\mydata.csv', r'C:\Users\Sweety\Documents\cleaned_data.csv')
