import pandas as pd
import numpy as np

# ---------------------------
# 1. Date Components
# ---------------------------
df = pd.DataFrame({'date': pd.date_range('2025-09-14', periods=7)})

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

print("Date components:")
print(df, "\n")

# ---------------------------
# 2. Data Binning (Age Groups)
# ---------------------------
ages = [19, 18, 20, 40, 55, 70, 85]
bins = [0, 12, 19, 35, 50, 65, 100]
labels = ['Child', 'Teen', 'Young Adult', 'Adult', 'Middle Age', 'Senior']

df_age = pd.DataFrame({'age': ages})
df_age['group'] = pd.cut(df_age['age'], bins=bins, labels=labels)

print("Age groups:")
print(df_age, "\n")

# ---------------------------
# 3. Data Transformation
# ---------------------------
data = pd.DataFrame({
    'income': [1000, 2000, 3000, 4000, 5000],
    'score': [50, 60, 70, 80, 90]
})

# Log transform
data['income_log'] = np.log(data['income'])

# Z-score normalization
data['score_z'] = (data['score'] - data['score'].mean()) / data['score'].std()

# Min-Max scaling
data['score_minmax'] = (data['score'] - data['score'].min()) / (data['score'].max() - data['score'].min())

print("Transformed data:")
print(data)
