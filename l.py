import pandas as pd
dataset ="Data\dataset_with_3Class.xlsx"

# Load dataset
rl = pd.read_excel(dataset)

cols = pd.read_excel(dataset, nrows=0).columns.tolist()
print(cols)