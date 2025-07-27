import pandas as pd

# Step 1: Extract
raw_data = pd.read_csv('raw_sales_data.csv')

# Step 2: Transform
# Add a new column: Total_Sales = Quantity * Price
raw_data['Total_Sales'] = raw_data['Quantity'] * raw_data['Price']

# Filter only orders with Total_Sales > $1000
filtered_data = raw_data[raw_data['Total_Sales'] > 1000]

# Step 3: Load
filtered_data.to_csv('cleaned_sales_data.csv', index=False)

print("ETL pipeline complete. Cleaned data saved to 'cleaned_sales_data.csv'")
