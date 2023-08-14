import json
import csv

def flatten_json(json_obj, parent_key=''):
    items = {}
    for key, value in json_obj.items():
        new_key = f"{parent_key}.{key}" if parent_key else key
        if isinstance(value, dict):
            items.update(flatten_json(value, new_key))
        else:
            items[new_key] = value
    return items

json_filename = 'input.json'
csv_filename = 'output.csv'

with open(json_filename, 'r') as json_file:
    json_data = json.load(json_file)

# Convert JSON data to flattened dictionaries
flattened_data = []
for item in json_data:
    flattened_item = flatten_json(item)
    flattened_data.append(flattened_item)

# Collect all unique keys for CSV headers
all_keys = set()
for item in flattened_data:
    all_keys.update(item.keys())

# Write to CSV File
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(all_keys)  # Write headers

    for item in flattened_data:
        csv_writer.writerow([item.get(key, '') for key in all_keys])

print(f"CSV file '{csv_filename}' created successfully.")
