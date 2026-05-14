import numpy as np
import csv

input_file = "Electronics_Unique_10000.csv"
output_file = "Electronics_Final_Report.csv"

products, price, stock, sales = [], [], [], []

with open(input_file, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        products.append(row["Product_Name"])
        p = float(row["Unit_Price"].replace('$', '').replace(',', '').strip())
        price.append(p)
        stock.append(float(row["Stock_Quantity"]))
        sales.append(float(row["Sales_Volume"]))

products = np.array(products)
price = np.array(price)
stock = np.array(stock)
sales = np.array(sales)


total_value = price * stock
discount_revenue = sales * price * 0.8

sorted_indices = np.argsort(sales)
hot_3_idx = sorted_indices[-3:][::-1]
low_3_idx = sorted_indices[:3]

print("\n" + "="*70)
print(f" 【最暢銷前三名】")
for i, idx in enumerate(hot_3_idx, 1):
    print(f"第 {i} 名: {products[idx]} (銷量: {sales[idx]:.0f})")

print("-" * 70)
print(f"❄ 【最不暢銷前三名】")
for i, idx in enumerate(low_3_idx, 1):
    print(f"第 {i} 名: {products[idx]} (銷量: {sales[idx]:.0f})")

print("-" * 70)

print(f" 全部商品八折後的總收入為：${np.sum(discount_revenue):,.2f}")
print("="*70 + "\n")


with open(output_file, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)

    w.writerow(["Product", "Stock", "Price", "Sales", "Inventory_Value"])

    for i in range(len(products)):
        w.writerow([
            products[i],
            stock[i],
            price[i],
            sales[i],
            total_value[i]
        ])

print(f" 分析完畢！CSV 檔案已儲存為：{output_file}")