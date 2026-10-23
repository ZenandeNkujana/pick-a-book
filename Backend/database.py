# ==========================================
# DATABASE CONNECTION AND SETUP
# ==========================================
# 1. Import the necessary SQLite modules.
# 2. Connect to the SQLite database.
# 3. Create the database file if it does not exist.
# 4. Create the necessary database tables.
# 5. Manage database connections.
# 6. Provide database access for saving, retrieving,
#    updating, and deleting book records.
# ==========================================


# ==========================================
# DATABASE MANAGEMENT
# ==========================================
# 1. Connect to the SQLite database.
# 2. Create the books table if it does not exist.
# 3. Save book records to the database.
# 4. Commit changes and close the connection.
# ==========================================


import sqlite3


# ==========================================
# INITIALIZE THE DATABASE
# ==========================================

def initialize_database():
    # Connect to the database file.
    connection = sqlite3.connect("books.db")

    # Create the books table if it does not exist.
    connection.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL
        )
    """)

    # Save the database changes and close the connection.
    connection.commit()
    connection.close()


# ==========================================
# SAVE THE BOOK TO THE DATABASE
# ==========================================

def save_book(book):
    # Ensure the database and table are ready.
    initialize_database()

    # Connect to the database file.
    connection = sqlite3.connect("books.db")

    # Insert the book information into the table.
    connection.execute(
        "INSERT INTO books (title, author) VALUES (?, ?)",
        (book["title"], book["author"])
    )

    # Save the changes and close the connection.
    connection.commit()
    connection.close()


# ==========================================
# RUN DATABASE SETUP
# ==========================================

if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully!")