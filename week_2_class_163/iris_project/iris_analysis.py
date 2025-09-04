import pandas as pd
df = pd.read_csv("week_2_class_163/iris_project/Iris_dataset.csv")
print(df.head())

df = pd.read_csv("week_2_class_163/iris_project/Iris_dataset.csv", header=None)
df.columns = ['data_1', 'data_2', 'data_3', 'data_4', 'flower_name']
print(df.head())

import pandas as pd

data = {
    "Name": ["Tony Soprano", "Paulie Walnuts", "Christopher Moltisanti", "Carmela Soprano"],
    "Age": ['dead', 62, 'dead', 45]
}

df_simple = pd.DataFrame(data)
print(df_simple)

df_simple.to_excel("soprano_data.xlsx", index=False)  #  Excel
df_simple.to_json("soprano_data.json", orient="records", indent=4)  #  JSON