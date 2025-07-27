# Sales Data ETL Pipeline

## 📌 Project Overview
This is a simple ETL (Extract, Transform, Load) project built using Python and pandas. It processes raw sales data, calculates total sales for each order, filters high-value transactions, and saves the clean data for reporting.

## 🔧 Tools Used
- Python
- pandas
- CSV files

## 📂 Files
- `raw_sales_data.csv`: Raw input sales file
- `etl_script.py`: Python script for ETL process
- `cleaned_sales_data.csv`: Output after transformation

## 🚀 ETL Steps
1. **Extract**: Load raw sales CSV file
2. **Transform**:
   - Calculate total sales per order
   - Filter orders where Total Sales > $1000
3. **Load**: Save filtered data to a new CSV file

## 📈 Output Sample

| OrderID | Customer | Product     | Total_Sales |
|---------|----------|-------------|-------------|
| 1002    | Bob      | Samsung S22 | 1598        |
| 1003    | Carol    | Pixel 7     | 2097        |
| 1004    | Dave     | iPhone 13   | 1798        |

---

## ✅ Status
Completed and working!

Author: Namo bhavani Maganti
linkedin url: https://www.linkedin.com/in/namomaganti/
