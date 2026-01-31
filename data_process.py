import pandas as pd
import os

# mock dataset representing Cloud Cost Optimization
data = {
    'Service': ['Compute Engine', 'Cloud Storage', 'BigQuery', 'Cloud Run'],
    'Cost_USD': [450, 120, 300, 80],
    'Savings_Potential': [0.2, 0.05, 0.15, 0.1]
}

df = pd.DataFrame(data)
df['Potential_Savings_USD'] = df['Cost_USD'] * df['Savings_Potential']

print("--- EcoPulse Cloud Cost Analysis ---")
print(df)
print(f"\nTotal Potential Monthly Savings: ${df['Potential_Savings_USD'].sum():.2f}")
print("\n[SUCCESS] Docker container processed the data successfully.")
