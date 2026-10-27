
# ==========================================
# PICK A BOOK - API ROUTES
# ==========================================

# Import the tools needed to create API routes
from flask import Blueprint, request, jsonify

# Import the functions that work with our database
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
# CREATE THE ROUTES BLUEPRINT
# ==========================================

# A Blueprint groups related API routes together
book_routes = Blueprint("book_routes", __name__)


# ==========================================
# ROUTE 1: VIEW ALL BOOKS
# ==========================================

@book_routes.route("/books", methods=["GET"])
def view_books():
    # Retrieve all books from the database
    books = get_all_books()

    # Convert database rows into dictionaries for JSON
    books = [dict(book) for book in books]

    # Return the books to the client
    return jsonify(books), 200


# ==========================================
# ROUTE 2: ADD A BOOK
# ==========================================

@book_routes.route("/books", methods=["POST"])
def add_book():
    # Read the data sent by the client
    data = request.get_json(silent=True) or {}

    # Get the title and author from the request
    title = data.get("title")
    author = data.get("author")

    # Check that both fields were provided
    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "Book title is required"}), 400

    if not isinstance(author, str) or not author.strip():
        return jsonify({"error": "Author name is required"}), 400

    # Create a dictionary containing the book information
    book = {
        "title": title.strip(),
        "author": author.strip()
    }

    # Save the book using our existing database function
    save_book(book)

    # Return a confirmation message
    return jsonify({
        "message": "Book added successfully",
        "book": book
    }), 201


# ==========================================
# ROUTE 3: VIEW ONE BOOK
# ==========================================

@book_routes.route("/books/<int:book_id>", methods=["GET"])
def view_book(book_id):
    # Find the requested book using its ID
    book = get_book_by_id(book_id)

    # Check whether the book exists
    if book is None:
        return jsonify({"error": "Book not found"}), 404

    # Convert the database row into a dictionary
    return jsonify(dict(book)), 200


# ==========================================
# ROUTE 4: UPDATE READING PROGRESS
# ==========================================

@book_routes.route("/books/<int:book_id>/progress", methods=["PUT"])
def update_progress(book_id):
    # Read the progress value sent by the client
    data = request.get_json(silent=True) or {}
    progress = data.get("progress")

    # Check that the progress is a whole number
    # between 0 and 100
    if (
        isinstance(progress, bool)
        or not isinstance(progress, int)
        or not 0 <= progress <= 100
    ):
        return jsonify({
            "error": "Progress must be a whole number from 0 to 100"
        }), 400

    # Check whether the book exists
    if get_book_by_id(book_id) is None:
        return jsonify({"error": "Book not found"}), 404

    # Update the progress in the database
    update_reading_progress(book_id, progress)

    # Return a confirmation message
    return jsonify({
        "message": "Reading progress updated successfully",
        "book_id": book_id,
        "progress": progress
    }), 200


# ==========================================
# ROUTE 5: TOGGLE FAVOURITE STATUS
# ==========================================

@book_routes.route("/books/<int:book_id>/favourite", methods=["PATCH"])
def favourite_book(book_id):
    # Check whether the book exists
    if get_book_by_id(book_id) is None:
        return jsonify({"error": "Book not found"}), 404

    # Switch the favourite status in the database
    toggle_favourite(book_id)

    # Return a confirmation message
    return jsonify({
        "message": "Favourite status updated successfully",
        "book_id": book_id
    }), 200


# ==========================================
# ROUTE 6: MARK A BOOK AS COMPLETED
# ==========================================

@book_routes.route("/books/<int:book_id>/complete", methods=["PATCH"])
def complete_book(book_id):
    # Check whether the book exists
    if get_book_by_id(book_id) is None:
        return jsonify({"error": "Book not found"}), 404

    # Mark the book as completed in the database
    mark_book_as_completed(book_id)

    # Return a confirmation message
    return jsonify({
        "message": "Book marked as completed successfully",
        "book_id": book_id
    }), 200


# ==========================================
# ROUTE 7: DELETE A BOOK
# ==========================================

@book_routes.route("/books/<int:book_id>", methods=["DELETE"])
def remove_book(book_id):
    # Check whether the book exists
    if get_book_by_id(book_id) is None:
        return jsonify({"error": "Book not found"}), 404

    # Delete the book from the database
    delete_book(book_id)

    # Return a confirmation message
    return jsonify({
        "message": "Book deleted successfully",
        "book_id": book_id
    }), 200
