# 1. File Processing and ReporƟng (15 minutes)
# Task:
# Develop a Python script to read a CSV file containing user transacƟon data:
# Copy code
# transacƟon_id,user_id,amount,transacƟon_date
# 1,101,500,2024-11-01
# 2,102,1500,2024-11-05
# 3,101,700,2024-11-10
# Requirements:
# 1. Calculate the total transacƟon amount for each user.
# 2. Save the result to a new CSV file (user_totals.csv) in the format:
# Copy code
# user_id,total_amount
# 101,1200
# 102,1500
# Bonus: Handle missing or corrupt data in the file gracefully


import csv
from collections import defaultdict

totals = defaultdict(int)

with open('transactions.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        user_id = row['user_id']
        amount = int(row['amount'])
        totals[user_id] += amount

with open('user_totals.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['user_id', 'total_amount']) 
    for user_id, total in totals.items():
        writer.writerow([user_id, total])





