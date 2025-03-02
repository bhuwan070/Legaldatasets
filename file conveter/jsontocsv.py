import json
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if not isinstance(data, list):
        data = [data]

    # Using the  field names from JSON
    keys = ["instruction", "text", "finetunetext"]

    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["index"] + keys)
        writer.writeheader()
        
        for index, entry in enumerate(data):
            instruction = entry.get("instruction", "") 
            text = entry.get("text", "")
            finetunetext = entry.get("finetunetext", f"<s>[INST] {instruction} [/INST] {text}</s>")

            writer.writerow({"index": index, "instruction": instruction, "text": text, "finetunetext": finetunetext})

    print(f'CSV file "{csv_file}" has been created successfully.')


json_to_csv('genderviolencemestral.json', 'output.csv')
