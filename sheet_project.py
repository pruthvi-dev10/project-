import csv

# Set your CSV file path (make sure the path is correct)
csv_file_path = r'C:\Users\jadha\Downloads\Soul AI _ Non Tech Roles (Responses) - Form responses 1.csv'

# Set the table name where data should be inserted
table_name = 'info'

# Open the CSV file and read its content
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Skip the header row if your CSV has one
    headers = next(csvreader)  # Uncomment this if there is a header row
    
    # Generate INSERT INTO statements for each row
    for row in csvreader:
        sql = f"INSERT INTO {table_name} ({', '.join(headers)}) VALUES ({', '.join([f'\"{value}\"' for value in row])});"
        print(sql)

