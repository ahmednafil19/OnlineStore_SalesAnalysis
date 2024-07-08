import pandas as pd
import numpy as np
data =pd.DataFrame({
    'Order ID': ['O001', 'O002', 'O003', 'O004', 'O005', 'O006', 'O007'],
    'Customer ID': ['C001', 'C002', 'C001', 'C003', 'C002', 'C004', 'C001'],
    'Order Date': ['2021-01-15', '2021-02-20', '2021-03-10', '2022-05-18', '2022-07-25', '2022-09-30', '2023-11-11'],
    'Product Category': ['Electronics', 'Home Appliances', 'Electronics', 'Furniture', 'Home Appliances', 'Electronics', 'Furniture'],
    'Product Name': ['Smartphone', 'Blender', 'Laptop', 'Chair', 'Vacuum Cleaner', 'Headphones', 'Table'],
    'Quantity': [2, 1, 1, 4, 1, 3, 2],
    'Price': [300, 100, 800, 50, 200, 150, 250],
    'Discount': [0.10, 0.05, 0.15, 0.20, 0.10, 0.05, 0.25]
})
totalprice=data['Price']*data['Quantity']
data['Total price']=totalprice
data['Discounted Price'] = data['Total price'] * (1 - data['Discount'])
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['YearMonth'] = data['Order Date'].dt.to_period('M')
data1=data.groupby('YearMonth')['Discounted Price'].sum().reset_index()
data1.columns = ['Month', 'Total Sales']
data2=data.groupby('Customer ID')['Discounted Price'].sum().reset_index()
data2 = data2.sort_values(by='Discounted Price', ascending=False).head(2)
data2.columns=['Customer ID','Total spending']
print(data2)
popular_products = data.groupby('Product Name')['Quantity'].sum().reset_index()
popular_products = popular_products.sort_values(by='Quantity', ascending=False).head(2)
popular_products.columns = ['Product Name', 'Total Quantity Sold']
print(popular_products)

print(data1)
print(data)
data['Year'] = data['Order Date'].dt.year

yearly_sales = data.groupby('Year')['Discounted Price'].sum().reset_index()
yearly_sales.columns = ['Year', 'Total Sales']
yearly_sales['Growth Rate'] = yearly_sales['Total Sales'].pct_change() * 100

print(yearly_sales)