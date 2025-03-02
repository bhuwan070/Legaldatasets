import pandas as pd

# Loading the original CSV file
input_file = "output.csv"  
output_file = "output2.csv"

df = pd.read_csv(input_file)

def generate_finetunetext(instruction, text):
    """Wrap the existing content in fine-tune format."""
    return f"<s>[INST] {instruction} [/INST] {text}</s>"

# Fill missing values in 'text' column to avoid errors
df["text"] = df["text"].fillna("")

df["instruction"] = df["instruction"].fillna("")
df["finetunetext"] = df.apply(lambda row: generate_finetunetext(row["instruction"], row["text"]), axis=1)

# Reordering the columns
df = df[["instruction", "text", "finetunetext"]]  

df.to_csv(output_file, index=False)
print("CSV file has been transformed successfully!")
