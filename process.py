import pandas as pd
def col_type(df):
    for col in df.columns:
        print(df[col].unique())

df = pd.read_csv("data0.csv")
# dump rows with heart_disease values != 1 or 0
df = df[df["heart_disease"].isin([0, 1])]
df.to_csv("data0.csv", index=False)
print(df["heart_disease"].value_counts())
