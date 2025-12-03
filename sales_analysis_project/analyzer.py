import os
import pandas as pd
import json
# print(os.getcwd())


# data_path ="data/sales.csv"

# if os.path.exists(data_path):
#     print(f"Data file found at: {data_path}")
# else:
#     print(f"Data file not found at: {data_path}")  

csv_data= pd.read_csv("data/sales.csv")
print(csv_data)
df= csv_data

print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")


df['total'] = df['quantity'] * df['price']
print("\nWith totals:")
print(df)

# Create output directory  With exist_ok=True, it won’t raise an error if the directory is already 
os.makedirs('output', exist_ok=True)


df.to_json("data/sales.json",orient='records',indent=3)


df.to_excel('output/sales_data.xlsx', index=False)

df.to_csv('output/sales_with_totals.csv')

print("\nFiles saved:")