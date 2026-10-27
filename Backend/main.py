
# ==========================================
# MAIN APPLICATION
# ==========================================
# Collect book information, create book records,
# and allow the user to manage their library.
# ==========================================
#Terminal applicaction-Command line application

from database import (
    save_book,
    get_all_books,
    get_book_by_id,
    update_reading_progress,
    toggle_favourite,
    mark_book_as_completed,
    delete_book
)


# ==========================================
# DISPLAY ALL SAVED BOOKS
# ==========================================

def view_books():
    # Retrieve all saved books from the database
    books = get_all_books()

    # Check whether the library contains any books
    if not books:
        print("\nYour library is empty.")
        return

    # Display the saved book records
    print("\nMy Library")
    print("==========")

    for saved_book in books:
        print(f"\nID: {saved_book['id']}")
        print(f"Title: {saved_book['title']}")
        print(f"Author: {saved_book['author']}")
        print(f"Reading progress: {saved_book['progress']}%")
        print(f"Favourite: {'Yes' if saved_book['favourite'] else 'No'}")
        print(f"Completed: {'Yes' if saved_book['completed'] else 'No'}")


# ==========================================
# SELECT A BOOK
# ==========================================

def select_book():
    # Display the saved books
    view_books()

    # Ask the user to enter the ID of the selected book
    try:
        book_id = int(input("\nEnter the book ID: "))
    except ValueError:
        print("\nPlease enter a valid numeric ID.")
        return None

    # Retrieve the selected book from the database
    selected_book = get_book_by_id(book_id)

    if selected_book is None:
        print("\nBook not found.")
        return None

    print(f"\nSelected book: {selected_book['title']}")
    return selected_book


# ==========================================
# REQUIREMENT 6: UPDATE READING PROGRESS
# ==========================================

def update_progress():
    # Ask the user to select a book
    selected_book = select_book()

    if selected_book is None:
        return

    # Ask the user to enter the reading progress
    try:
        progress = int(input("Enter reading progress (0-100): "))
    except ValueError:
        print("\nPlease enter a valid percentage.")
        return

    # Validate the reading progress
    if not 0 <= progress <= 100:
        print("\nProgress must be between 0 and 100.")
        return

    # Save the updated reading progress
    update_reading_progress(selected_book["id"], progress)

    print("\nReading progress updated successfully!")


# ==========================================
# REQUIREMENT 7: MANAGE FAVOURITE BOOKS
# ==========================================

def favourite_book():
    # Ask the user to select a book
    selected_book = select_book()

    if selected_book is None:
        return

    # Add or remove the book from favourites
    toggle_favourite(selected_book["id"])

    print("\nFavourite status updated successfully!")


# ==========================================
# REQUIREMENT 8: MARK A BOOK AS COMPLETED
# ==========================================

def complete_book():
    # Ask the user to select a book
    selected_book = select_book()

    if selected_book is None:
        return

    # Mark the selected book as completed
    mark_book_as_completed(selected_book["id"])

    print("\nBook marked as completed!")


# ==========================================
# REQUIREMENT 9: DELETE A BOOK
# ==========================================

def remove_book():
    # Ask the user to select a book
    selected_book = select_book()

    if selected_book is None:
        return

    # Confirm the deletion before removing the book
    confirmation = input(
        f"Delete '{selected_book['title']}'? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        # Delete the selected book from the database
        delete_book(selected_book["id"])
        print("\nBook deleted successfully!")
    else:
        print("\nDeletion cancelled.")


# ==========================================
# MAIN MENU
# ==========================================

def main():
    # Display the available actions
    while True:
        print("\n========== PICK A BOOK ==========")
        print("1. Add a book")
        print("2. View all saved books")
        print("3. Update reading progress")
        print("4. Add or remove a favourite")
        print("5. Mark a book as completed")
        print("6. Delete a book")
        print("0. Exit")

        # Ask the user to choose an action
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            # Collect book information
            book_title = input("Enter the book title: ").strip()
            book_author = input("Enter the author's name: ").strip()

            # Create a book record
            book = {
                "title": book_title,
                "author": book_author
            }

            # Save the book to the database
            save_book(book)

            print("\nBook saved successfully!")

        elif choice == "2":
            view_books()

        elif choice == "3":
            update_progress()

        elif choice == "4":
            favourite_book()

        elif choice == "5":
            complete_book()

        elif choice == "6":
            remove_book()

        elif choice == "0":
            print("\nThank you for using Pick a Book!")
            break

        else:
            print("\nInvalid option. Please choose again.")


# ==========================================
# START THE APPLICATION
# ==========================================

if __name__ == "__main__":
    main()
