import sqlite3

# Connect to the database
conn = sqlite3.connect('data/mydatabase.db')

# Create a cursor object
cursor = conn.cursor()

# Create the python_programming table
cursor.execute('''CREATE TABLE python_programming
                  (id INTEGER PRIMARY KEY,
                   name TEXT,
                   grade INTEGER)''')

# Insert new rows into the table
cursor.execute("INSERT INTO python_programming VALUES (55, 'Carl Davis', 61)")
cursor.execute("INSERT INTO python_programming VALUES (66, 'Dennis Fredrickson', 88)")
cursor.execute("INSERT INTO python_programming VALUES (77, 'Jane Richards', 78)")
cursor.execute("INSERT INTO python_programming VALUES (12, 'Peyton Sawyer', 45)")
cursor.execute("INSERT INTO python_programming VALUES (2, 'Lucas Brooke', 99)")

# Select all records with a grade between 60 and 80
cursor.execute("SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Change Carl Davis's grade to 65
cursor.execute("UPDATE python_programming SET grade = 65 WHERE name = 'Carl Davis'")

# Delete Dennis Fredrickson's row
cursor.execute("DELETE FROM python_programming WHERE name = 'Dennis Fredrickson'")

# Change the grade of all people with an id below than 55
cursor.execute("UPDATE python_programming SET grade = 70 WHERE id < 55")

# Commit changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
