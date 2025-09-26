import pandas as pd
import os

# Get the path to the user's Downloads folder
downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')

# The path for your input CSV file
input_file_path = os.path.join(downloads_path, 'attendance_mixed_30_days.csv')

# The path for your output Excel file
output_file_path = os.path.join(downloads_path, 'attendance_22_days.xlsx')

try:
    # Read the CSV file from the specified path
    df = pd.read_csv(input_file_path)

    # Convert the 'att_date' column to datetime objects
    df['att_date'] = pd.to_datetime(df['att_date'])

    # Define the start and end dates for the 22-day period
    start_date = '2025-09-01'
    end_date = '2025-09-22'

    # Filter the DataFrame to the 22-day period
    filtered_df = df[(df['att_date'] >= start_date) & (df['att_date'] <= end_date)].copy()

    # Save the filtered DataFrame to the new Excel file
    filtered_df.to_excel(output_file_path, index=False)

    print(f"Data for 22 days has been successfully saved to {output_file_path}")
    print("Check your Downloads folder for the new file.")

except FileNotFoundError:
    print(f"Error: The file '{input_file_path}' was not found.")
    print("Please make sure the file is in your Downloads folder and the name is spelled correctly.")