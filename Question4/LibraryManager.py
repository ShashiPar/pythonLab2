# LibraryManager.py

class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, publisher, volume, year, isbn_code):

        if isbn in self.books:
            return "Book already exists in the library."
        self.books[isbn] = {
            "title": title,
            "author": author,
            "publisher": publisher,
            "volume": volume,
            "year": year,
            "isbn": isbn_code
        }
        return "Book added successfully."

    def remove_book(self, isbn):

        if isbn not in self.books:
            return "Book not found in the library."
        del self.books[isbn]
        return "Book removed successfully."

    def retrieve_book(self, isbn):

        if isbn not in self.books:
            return "Book not found in the library."
        return self.books[isbn]

    def search_books(self, search_term, search_type="title"):

        results = []
        for book in self.books.values():
            if search_term.lower() in book[search_type].lower():
                results.append(book)
        return results

    def list_books(self):

        return list(self.books.values())

    def update_book(self, isbn, **kwargs):

        if isbn not in self.books:
            return "Book not found in the library."
        for key, value in kwargs.items():
            if key in self.books[isbn]:
                self.books[isbn][key] = value
        return "Book details updated successfully."

    def is_book_available(self, isbn):

        return isbn in self.books
