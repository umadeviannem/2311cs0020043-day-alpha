import pandas as pd
data = {
    'Name': ['John', 'Alice', 'Bob', 'Diana'],
    'Age': [28, 34, 23, 29],
    'Department': ['HR', 'IT', 'Marketing', 'Finance'],
    'Salary': [45000, 60000, 35000, 50000]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)
