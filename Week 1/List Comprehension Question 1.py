import pandas as pd
import seaborn as sns

df = sns.load_dataset("car_crashes")

df =["NUM_"+col.upper() if df[col].dtype in ["int64","float64"] else col.upper() for col in df.columns]
print(df)