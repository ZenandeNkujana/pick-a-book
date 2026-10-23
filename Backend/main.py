# ==========================================
# MAIN APPLICATION
# ==========================================
# Collect book information, create book records,
# and display them to the user.
# ==========================================


from database import save_book
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

# ==========================================
# SAVE THE BOOK TO THE DATABASE
# ==========================================

# Send the book record to database.py to be saved
save_book(book)

# Confirm that the book was saved
print("\nBook saved successfully!")