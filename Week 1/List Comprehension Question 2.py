import pandas as pd
import seaborn as sns

df = sns.load_dataset("car_crashes")


df = [" " + col.upper() if "no" in col else col.upper() +"_FLAG" for col in df.columns]

print(df)