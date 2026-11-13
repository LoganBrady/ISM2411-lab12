#csv_practice.py
# Author: Logan Brady
# Module 12 lab: Read a Sales CSV, Write a cleaned report

# Reflection 1:
# Python can read, clean, and process large amounts of data automatically.
# Excel is easier for manually viewing data, making charts, and editing cells.

# Reflection 2:
# A business could use an append-mode log to track daily sales transactions.
# Append mode is useful because it adds new records without deleting old ones.

import csv
from datetime import datetime

SALES_CSV = 'data/sales.csv'
CLEANED_CSV = 'data/cleaned_sales.csv'
LOG_FILE = 'data/sales_log.txt'

print("---Exercise 1---")
with open(SALES_CSV, 'r') as f:
    print(f"Opened {SALES_CSV} .")

print("---Exercise 2---")
with open(SALES_CSV, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("---Exercise 3---")
with open(SALES_CSV, 'r') as f:
    reader = csv.reader(f)
    header = next(reader) # Next() returns the next item from the iterator, in this case the first row of the CSV file
    print(f"Header: {header}")
    for row in reader:
        print(row)

print("---Exercise 4---")
total_revenue = 0
with open(SALES_CSV,'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row
    for row in reader: 
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        total_revenue += total
        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")

print("---Exercise 5---")
high_value = []
rows_read = 0
with open(SALES_CSV, 'r') as f:
    reader =csv.reader(f)
    next(reader) # Skip the header row
    for row in reader:
        rows_read += 1
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        if total > 100:
            high_value.append([product, f"{price:.2f}", quantity, f"{total:.2f}"])

with open(CLEANED_CSV, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['product', 'price', 'quantity', 'total'])
    for row in high_value:
        writer.writerow(row)

print(f"Wrote {len(high_value)} high-value sales to {CLEANED_CSV}.")
print(f"Original rows: {rows_read}")
print("---Exercise 6---")
dict_total = 0
with open(SALES_CSV, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row['price'])
        quantity = int(row['quantity'])
        total = price * quantity
        dict_total += total
        print(f"{row['product']}: {quantity} units x ${price:.2f} = ${total:.2f}")
print(f"Total revenue: ${dict_total:.2f}")

print("---Exercise 7---")
summary = {}


with open(SALES_CSV, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader: 
        product = row['product']
        total = float(row['price']) * int(row['quantity'])
        summary[product] = summary.get(product, 0) + total

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

print("---Exercise 8---")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG_FILE, 'a') as f:
    f.write(f"{timestamp} total revenue: ${dict_total:.2f}\n")
entries = 0
with open(LOG_FILE, 'r') as f:
    for line in f:
        entries += 1
        print(line.strip())
print(f"Log entries so far: {entries}")