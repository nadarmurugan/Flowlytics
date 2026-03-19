import pandas as pd

print("🔄 Cleaning started...")

df = pd.read_csv("data/raw/input.csv")

# Remove duplicates
df = df.drop_duplicates()

# Convert empty strings to NaN
df.replace("", pd.NA, inplace=True)

# Fill missing values
df = df.fillna(0)

# Ensure numeric columns are correct
df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0)
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').fillna(0)

# Normalize column names
df.columns = df.columns.str.strip().str.lower()

df.to_csv("data/processed/cleaned.csv", index=False)

print("✅ Cleaning completed")