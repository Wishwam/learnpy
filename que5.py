import pandas as pd
filename = "std_data.xlsx"
df = pd.read_excel(filename)
print(df.to_string(index=False))
