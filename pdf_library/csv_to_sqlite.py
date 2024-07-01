import csv
import sqlite3

# Path to your CSV file
csv_file = 'Books_mock2.csv'

# Path to SQLite database file
sqlite_db = 'db2.sqlite3'

# Connect to SQLite database
conn = sqlite3.connect(sqlite_db)
cursor = conn.cursor()

# Create a table in the database
cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                    book_id INTEGER PRIMARY KEY,
                    pdf TEXT,
                    title TEXT,
                    author TEXT,
                    genre TEXT,
                    publication_date DATE,
                    price FLOAT,
                    publisher TEXT,
                    isbn BIGINT,
                    page_count INT,
                    language TEXT
                )''')

# Read data from CSV and insert into SQLite database
with open(csv_file, 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute('''INSERT INTO books (pdf,title,author,genre,publication_date,price,publisher,isbn,page_count,language) 
                          VALUES (?,?,?,?,?,?,?,?,?,?)''',
                       (    row['pdf'], row['title'], row['author'], row['genre'], row['publication_date'], row['price'], row['publisher'], row['isbn'], row['page_count'], row['language']))

# Commit changes and close the connection
conn.commit()
conn.close()

print(f"SQLite database created successfully at '{sqlite_db}' with data from '{csv_file}'")
