import pandas as pd

file_path = '/Users/spectorpower/Documents/DI_bootcamp/files/posts.json'
df = pd.read_json(file_path)

print(df.head())