# ==========================================
# MAIN APPLICATION
# ==========================================
# 1. Import the necessary modules and functions.
# 2. Create and configure the Flask application.
# 3. Register the application routes.
# 4. Set up any required startup tasks.
# 5. Start the Flask development server.
# ==========================================



# ==========================================
# REQUIREMENT 1: CREATE A BOOK RECORD
# ==========================================
# 1. Ask the user to enter the book's title.
# 2. Ask the user to enter the author's name.
# 3. Store the information in a dictionary.
# 4. Display the complete book record.
# ==========================================


# ==========================================
# COLLECT BOOK INFORMATION
# ==========================================

# Ask the user to enter the book's title
book_title = input("Enter the book title: ")

# Ask the user to enter the author's name
book_author = input("Enter the author's name: ")


# ==========================================
# CREATE A BOOK RECORD
# ==========================================

# Store the book information together in a dictionary
book = {
    "title": book_title,
    "author": book_author
}


# ==========================================
# REQUIREMENT 3: DISPLAY THE BOOK RECORD
# ==========================================

# Display the information stored in the book record
print("\nBook Information")
print("----------------")
print(f"Title: {book['title']}")
print(f"Author: {book['author']}")

