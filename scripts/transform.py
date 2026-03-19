import pandas as pd

print("🔄 Transformation started...")

df = pd.read_csv("data/processed/cleaned.csv")

# Ensure numeric
df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0)
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').fillna(0)

# Add total column
df['total'] = df['price'] * df['quantity']

df.to_csv("data/processed/final.csv", index=False)

print("✅ Transformation completed")