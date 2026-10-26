# ==========================================
# BOOK MODEL
# ==========================================
# This file defines the structure of a book
# in our Pick a Book application.
#
# It groups the information belonging to a
# book into one object.
#
# It also allows us to convert a book object
# into a dictionary when needed.
# ==========================================


# ==========================================
# CREATE THE BOOK CLASS
# ==========================================

class Book:

    # Initialise a book with its information
    def __init__(
        self,
        title,
        author,
        book_id=None,
        progress=0,
        favourite=False,
        completed=False
    ):

        # Store the book's information
        self.id = book_id
        self.title = title
        self.author = author
        self.progress = progress
        self.favourite = favourite
        self.completed = completed

    # ==========================================
    # CONVERT THE BOOK INTO A DICTIONARY
    # ==========================================

    def to_dict(self):

        # Group the book's information into a dictionary
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "progress": self.progress,
            "favourite": self.favourite,
            "completed": self.completed
        }