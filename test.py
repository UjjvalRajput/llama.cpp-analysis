import json
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        # Write the header based on the keys of the first item
        writer.writerow(data[0].keys())

        # Write the data
        for item in data:
            writer.writerow(item.values())

json_to_csv('issues.json', 'output.csv')


