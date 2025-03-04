import csv
import json

def csv_to_jsonl(csv_file_path, jsonl_file_path):
    """
    Converts a CSV file to JSONL format.

    Args:
        csv_file_path (str): Path to the input CSV file.
        jsonl_file_path (str): Path to the output JSONL file.
    """
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile, \
             open(jsonl_file_path, 'w', encoding='utf-8') as jsonlfile:

            reader = csv.DictReader(csvfile)
            if reader.fieldnames is None:
                print(f"Error: CSV file '{csv_file_path}' is empty or has no header.")
                return

            for row in reader:
                json.dump(row, jsonlfile, ensure_ascii=False) 

        print(f"Successfully converted '{csv_file_path}' to '{jsonl_file_path}'")

    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


csv_file = 'output2.csv'  # Changed to 'output2.csv'
jsonl_file = 'output.jsonl' # Path to your JSONL file
csv_to_jsonl(csv_file, jsonl_file)