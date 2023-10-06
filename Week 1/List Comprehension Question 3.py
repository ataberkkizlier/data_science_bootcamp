import seaborn as sns

df = sns.load_dataset("car_crashes")
print(df.columns)

og_list = ["abbrev","no_previous"]
new_column_names = [column for column in df.columns if column not in og_list]
new_df = df[new_column_names]
print(new_df)
