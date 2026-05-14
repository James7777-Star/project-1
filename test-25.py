import numpy as np
import csv

grocery_list = []
input_file = "Grocery_Inventory_and_Sales_Dataset.csv"

with open(input_file, "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    grocery_header = next(reader)
    for row in reader:
        if row: grocery_list.append(row)

grocery_array = np.array(grocery_list)

def clean_numeric(column_index):
    col = grocery_array[:, column_index]
    cleaned = [str(x).replace('$', '').replace(',', '').strip() for x in col]
    return np.array(cleaned).astype(float)

items = grocery_array[:, 1]
stocks = clean_numeric(5)
prices = clean_numeric(8)
sales = clean_numeric(13)

inventory_value = stocks * prices

max_sales_value = np.max(sales)

best_seller_indices = np.where(sales == max_sales_value)[0]

best_grocery_items = items[best_seller_indices]

discounted_income = sales * prices * 0.9
total_income = np.sum(discounted_income)

print(f"--- 雜貨店數據分析報告 ---")
print(f"最高銷售數量為：{max_sales_value}")
print(f"最暢銷商品共 {len(best_grocery_items)} 項：")
for name in best_grocery_items:
    print(f" - {name}")

print(f"\n全部商品 9 折後的總收入為：${total_income:,.2f} 元")

new_header = grocery_header + ["Inventory_Value", "Discounted_Revenue"]
final_data = np.column_stack((grocery_array, inventory_value, discounted_income))

with open("grocery_ok.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(new_header)
    writer.writerows(final_data)

print(f"\n[系統訊息] 檔案 grocery_ok.csv 已成功生成！")