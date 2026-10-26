
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
# DATABASE CONNECTION
# ==========================================

def get_connection():
    # Connect to the SQLite database file.
    connection = sqlite3.connect("books.db")

    # Return rows as dictionaries accessible by column name.
    connection.row_factory = sqlite3.Row

    return connection


# ==========================================
# DATABASE INITIALIZATION
# ==========================================

def initialize_database():
    # Create the books table if it does not exist.
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                progress INTEGER NOT NULL DEFAULT 0,
                favourite INTEGER NOT NULL DEFAULT 0,
                completed INTEGER NOT NULL DEFAULT 0
            )
        """)

        # Add new columns when upgrading an existing database.
        existing_columns = {
            row["name"]
            for row in connection.execute("PRAGMA table_info(books)")
        }

        if "progress" not in existing_columns:
            connection.execute(
                "ALTER TABLE books ADD COLUMN progress INTEGER NOT NULL DEFAULT 0"
            )

        if "favourite" not in existing_columns:
            connection.execute(
                "ALTER TABLE books ADD COLUMN favourite INTEGER NOT NULL DEFAULT 0"
            )

        if "completed" not in existing_columns:
            connection.execute(
                "ALTER TABLE books ADD COLUMN completed INTEGER NOT NULL DEFAULT 0"
            )


# ==========================================
# SAVE THE BOOK TO THE DATABASE
# ==========================================

def save_book(book):
    # Ensure the database table is ready.
    initialize_database()

    # Insert the book information into the table.
    with get_connection() as connection:
        connection.execute(
            "INSERT INTO books (title, author) VALUES (?, ?)",
            (book["title"], book["author"])
        )


# ==========================================
# RETRIEVE ALL SAVED BOOKS
# ==========================================

def get_all_books():
    # Retrieve all book records from the database.
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT * FROM books ORDER BY id"
        ).fetchall()

        # Convert database rows into dictionaries.
        return [dict(row) for row in rows]


# ==========================================
# RETRIEVE A BOOK BY ITS ID
# ==========================================

def get_book_by_id(book_id):
    # Find the book matching the supplied ID.
    with get_connection() as connection:
        row = connection.execute(
            "SELECT * FROM books WHERE id = ?",
            (book_id,)
        ).fetchone()

        # Return the book record if it exists.
        return dict(row) if row else None


# ==========================================
# UPDATE READING PROGRESS
# ==========================================

def update_reading_progress(book_id, progress):
    # Update the reading progress for the selected book.
    with get_connection() as connection:
        connection.execute(
            """
            UPDATE books
            SET progress = ?, completed = ?
            WHERE id = ?
            """,
            (progress, 1 if progress == 100 else 0, book_id)
        )


# ==========================================
# UPDATE FAVOURITE STATUS
# ==========================================

def toggle_favourite(book_id):
    # Switch the selected book's favourite status.
    with get_connection() as connection:
        connection.execute(
            """
            UPDATE books
            SET favourite = CASE
                WHEN favourite = 1 THEN 0
                ELSE 1
            END
            WHERE id = ?
            """,
            (book_id,)
        )


# ==========================================
# MARK A BOOK AS COMPLETED
# ==========================================

def mark_book_as_completed(book_id):
    # Mark the selected book as completed.
    with get_connection() as connection:
        connection.execute(
            """
            UPDATE books
            SET completed = 1, progress = 100
            WHERE id = ?
            """,
            (book_id,)
        )


# ==========================================
# DELETE A BOOK
# ==========================================

def delete_book(book_id):
    # Delete the selected book from the database.
    with get_connection() as connection:
        connection.execute(
            "DELETE FROM books WHERE id = ?",
            (book_id,)
        )


# ==========================================
# RUN DATABASE SETUP
# ==========================================

if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully!")
