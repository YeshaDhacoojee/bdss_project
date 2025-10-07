import pandas as pd

# Load the CSV file
df = pd.read_csv("data/daily_transactions.csv")

print("✅ Data loaded successfully!")
print(df.head())

print("\n📊 Data Summary:")
print(df.describe())


