import numpy as np
import csv

products = []
price = []
electronics = []
sales = []

with open("Electronics_Unique_10000.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        products.append(row["Product_Name"])
        p = float(row["Unit_Price"].replace('$', '').replace(',', '').strip())
        price.append(p)
        electronics.append(float(row["Stock_Quantity"]))
        sales.append(float(row["Sales_Volume"]))

products = np.array(products)
price = np.array(price)
electronics = np.array(electronics)
sales = np.array(sales)

total_electronics_value = price * electronics
discount_revenue = sales * price * 0.8


sorted_indices = np.argsort(sales)
hot_3_idx = sorted_indices[-3:][::-1]
low_3_idx = sorted_indices[:3]


print(f"{'排名':<4} | {'銷售量':<6} | {'產品名稱'}")
print("-" * 60)
print(" 【最暢銷前三名】")
for i, idx in enumerate(hot_3_idx, 1):
    print(f"第 {i} 名 | {sales[idx]:>6.0f} | {products[idx]}")

print("-" * 60)
print(" 【最不暢銷前三名】")
for i, idx in enumerate(low_3_idx, 1):
    print(f"第 {i} 名 | {sales[idx]:>6.0f} | {products[idx]}")

print("-" * 60)
print(f" 全部商品八折總收入為：${np.sum(discount_revenue):,.2f}")
print("-" * 60)


with open("Electronics_Analysis.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)

    w.writerow(["Product_Name", "Electronics_Stock", "Unit_Price", "Sales_Volume", "Inventory_Value"])

    for i in range(len(products)):
        w.writerow([
            products[i],
            electronics[i],
            price[i],
            sales[i],
            total_electronics_value[i]
        ])

print(" Electronics_Analysis.csv 已存檔完成。")