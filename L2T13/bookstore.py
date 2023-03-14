# Import the sqlite3 module
import sqlite3

# Function to create the books table in the ebookstore database
def create_table():
    # Connect to the ebookstore database
    conn = sqlite3.connect('ebookstore.db')
    # Create a cursor object to execute SQL commands
    c = conn.cursor()
    # Execute an SQL command to create the books table if it doesn't already exist
    c.execute('''CREATE TABLE IF NOT EXISTS books
                 (id INTEGER PRIMARY KEY,
                 title TEXT NOT NULL,
                 author TEXT NOT NULL,
                 qty INTEGER NOT NULL)''')
    # Commit the changes to the database
    conn.commit()
    # Close the database connection
    conn.close()
# Function to add a new book to the books table
def add_book():
    # Connect to the ebookstore database
    conn = sqlite3.connect('ebookstore.db')
    # Create a cursor object to execute SQL commands
    c = conn.cursor()
    # Prompt the user for the book's title, author, and quantity
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    qty = int(input("Enter book quantity: "))
    # Execute an SQL command to insert the new book into the books table
    c.execute("INSERT INTO books (title, author, qty) VALUES (?, ?, ?)", (title, author, qty))
    # Commit the changes to the database
    conn.commit()
    # Print a success message to the user
    print("Book added successfully!")
    conn.close()
# Function to update an existing book in the books table
def update_book():
    conn = sqlite3.connect('ebookstore.db')
    c = conn.cursor()
    book_id = int(input("Enter book ID: "))
    title = input("Enter new book title (leave blank to keep current title): ")
    author = input("Enter new book author (leave blank to keep current author): ")
    qty = input("Enter new book quantity (leave blank to keep current quantity): ")
    c.execute("SELECT * FROM books WHERE id=?", (book_id,))
    book = c.fetchone()
    if not book:
        print("Book not found!")
        return
    if title.strip():
        c.execute("UPDATE books SET title=? WHERE id=?", (title, book_id))
    if author.strip():
        c.execute("UPDATE books SET author=? WHERE id=?", (author, book_id))
    if qty.strip():
        c.execute("UPDATE books SET qty=? WHERE id=?", (qty, book_id))
    conn.commit()
    print("Book updated successfully!")
    conn.close()

def delete_book():
    conn = sqlite3.connect('ebookstore.db')
    c = conn.cursor()
    book_id = int(input("Enter book ID: "))
    c.execute("SELECT * FROM books WHERE id=?", (book_id,))
    book = c.fetchone()
    if not book:
        print("Book not found!")
        return
    c.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    print("Book deleted successfully!")
    conn.close()

def search_book():
    conn = sqlite3.connect('ebookstore.db')
    c = conn.cursor()
    search_title = input("Enter book title to search: ")
    c.execute("SELECT * FROM books WHERE title=?", (search_title,))
    books = c.fetchall()
    if not books:
        print("Book not found!")
        return
    for book in books:
        print(f"{book[0]} {book[1]} {book[2]} {book[3]}")
    conn.close()

def menu():
    print("""
1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit
""")
    choice = input("Enter your choice: ")
    return choice

if __name__ == "__main__":
    create_table()
    while True:
        choice = menu()
        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            search_book()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again!")
