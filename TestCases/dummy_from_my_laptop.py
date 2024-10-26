import pandas as pd

df = pd.read_excel(r'F:\archive\HW_dataset.xlsx')
print(df["Output"])

for i in range(len(df)):
    print(df["Output"][i])
    with open(f"file{i}.py", 'w') as fh:
        fh.write(df["Output"][i])
