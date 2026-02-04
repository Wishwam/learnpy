import csv
filename = "data.csv"
column_name = "Marks"        
total = 0
count = 0
with open(filename, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total += float(row[column_name])
        count += 1
average = total / count
print(f"Average of {column_name}: {average}")

