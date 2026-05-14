import numpy as np
import csv

electronics_list = []
input_file = "Electronics_Unique_10000.csv"

with open(input_file, "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        if row: electronics_list.append(row)

electronics_array = np.array(electronics_list)

def clean_numeric(column_index):
    col = electronics_array[:, column_index]
    cleaned = [str(x).replace('$', '').replace(',', '').strip() for x in col]
    return np.array(cleaned).astype(float)

items = electronics_array[:, 1]
stocks = clean_numeric(5)
prices = clean_numeric(8)
sales = clean_numeric(13)


inventory_values = stocks * prices

min_sales_value = np.min(sales)
worst_indices = np.where(sales == min_sales_value)[0]
all_worst_items = items[worst_indices]

discounted_income_per_item = sales * prices * 0.8
total_income = np.sum(discounted_income_per_item)

print(f"========== 唯一產品大數據分析 (10,000 筆) ==========")
print(f"最低銷售數量：{min_sales_value:.0f}")
print(f"最不暢銷商品總數：{len(all_worst_items)} 項")

print(f"\n銷量最低的具體型號：")
for name in all_worst_items[:10]:
    print(f" - {name}")

print(f"\n全部商品【八折】後的總收入為：${total_income:,.2f} 元")
print(f"====================================================\n")

new_header = header + ["Inventory_Value", "80_Percent_Revenue"]
final_data = np.column_stack((electronics_array, inventory_values, discounted_income_per_item))

with open("electronics_unique_final.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(new_header)
    writer.writerows(final_data)

print(f"分析完成！已存入 electronics_unique_final.csv")