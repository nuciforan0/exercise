import pandas as pd
import json

# Load the Excel file
file_path = 'exercise plan.xlsx'
sheet_name = 'Sheet1'

# Read the Excel file
df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

# Find the starting row of the "HOW THE EXERCISE ACTUALLY IS DONE" section
start_row = df[df[0] == "HOW THE EXERCISE ACTUALLY IS DONE IN REALITY WITH SEQUENTIAL SETS"].index[0] + 2

# Extract the section headers
section_headers = df.iloc[start_row - 1].dropna().values

# Initialize the JSON structure
exercise_data = {}

# Iterate through each section
for i, section in enumerate(section_headers):
    section_name = section.strip()
    exercise_data[section_name] = []
    
    # Determine the column range for the current section
    start_col = i * 7
    end_col = start_col + 7
    
    # Iterate through the rows in the section, skipping the header row
    for row in range(start_row + 1, len(df)):
        exercise_name = df.iloc[row, start_col]
        if pd.isna(exercise_name):
            break
        
        # Extract exercise details
        exercise_details = {
            "Name": exercise_name,
            "Sets": df.iloc[row, start_col + 1],
            "Reps": df.iloc[row, start_col + 2],
            "Duration": df.iloc[row, start_col + 3],
            "Notes": df.iloc[row, start_col + 4],
            "Explanation": df.iloc[row, start_col + 5],
            "Images": df.iloc[row, start_col + 6]
        }
        
        # Replace NaN with None for JSON compatibility
        for key in exercise_details:
            if pd.isna(exercise_details[key]):
                exercise_details[key] = None
        
        exercise_data[section_name].append(exercise_details)

# Convert the dictionary to JSON
json_output = json.dumps(exercise_data, indent=4)

# Print the JSON output
print(json_output)

# Save the JSON to a file
with open('exercise_data.json', 'w') as json_file:
    json_file.write(json_output)