import json
import os
import pandas as pd

# Define your entity names
entity_names = [
    "COURT",
    "PETITIONER",
    "RESPONDENT",
    "JUDGE",
    "LAWYER",
    "DATE",
    "ORG",
    "GPE",
    "STATUTE",
    "PROVISION",
    "PRECEDENT",
    "CASE_NUMBER",
    "WITNESS",
    "PROCEDURES",
    "OTHERS"
]

# Set the directory where your JSON files are located
json_folder = '/home/hp/Documents/Mini_Project/Labelled/json'

# List all files in the directory
json_files = [f for f in os.listdir(json_folder) if f.endswith('.json')]

# Iterate over each JSON file
for filename in json_files:
    file_path = os.path.join(json_folder, filename)
    
    # Load the JSON data from the file
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Process the data similar to your original code
    train_data = data['annotations']
    
    for annotation in train_data:
        if annotation['entities'] == []:
            annotation['entities'] = [(0, 0, entity_name) for entity_name in entity_names]
        else:
            for idx, entity in enumerate(annotation['entities']):
                annotation['entities'][idx] = tuple(entity) if isinstance(entity, list) else (0, 0, entity)

    # Save the modified data back to the same file or a new file
    with open(file_path, 'w') as f:
        json.dump(data, f)

    print(f"Processed {filename}")

print("All files processed.")

