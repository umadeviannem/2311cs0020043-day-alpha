import pandas as pd

# Assuming 'df' is your DataFrame containing the data
# Example: df = pd.read_csv('your_data.csv')

# 1. Extract all rows where Sales > 1000
sales_greater_than_1000 =df[df['Sales'] > 1000]

# 2. Find all sales records for the "East" region
sales_east_region = df[df['Region'] == 'East']

# Display the results
print("Sales greater than 1000:")
print(sales_greater_than_1000)

print("\nSales records for East region:")
print(sales_east_region)
