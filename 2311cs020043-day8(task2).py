import pandas as pd

# Sample DataFrame
data = {
    'Profit': [500, 1200, 800, 150],
    'Quantity': [50, 100, 80, 15],
    'Sales': [1200, 800, 1500, 900]
}

df = pd.DataFrame(data)

# Add 'Profit_Per_Unit' column
df['Profit_Per_Unit'] = df['Profit'] / df['Quantity']

# Add 'High_Sales' column
df['High_Sales'] = df['Sales'].apply(lambda x: 'Yes' if x > 1000 else 'No')

# Display the updated DataFrame
print(df)