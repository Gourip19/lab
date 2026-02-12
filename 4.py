import pandas as pd
ages = [12, 15, 18, 22, 25, 30, 34, 40, 45, 50, 55, 60, 65, 70]
df = pd.DataFrame({'Age': ages})
print("Original Age Data:")
print(df)
num_bins = 4
df['EW_Bin'] = pd.cut(df['Age'], bins=num_bins)
print("\nEqual-Width Binning:")
print(df[['Age', 'EW_Bin']])
df['EF_Bin'] = pd.qcut(df['Age'], q=4)
print("\nEqual-Frequency Binning:")
print(df[['Age', 'EF_Bin']])
bins = [0, 12, 19, 59, 100]
labels = ['Child', 'Teen', 'Adult', 'Senior']
df['Custom_Bin'] = pd.cut(df['Age'], bins=bins, labels=labels)
print("\nCustom Binning:")
print(df[['Age', 'Custom_Bin']])