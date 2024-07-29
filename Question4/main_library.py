# main_library.py
from LibraryManager import LibraryManager

def main():
    library = LibraryManager()

    # Sample books
    books = [
        {
            "isbn": "9780134692883",
            "title": "Operating System Concepts",
            "author": "Abraham Silberschatz",
            "publisher": "Wiley",
            "volume": 10,
            "year": 2018,
            "isbn_code": "9780134692883"
        },
        {
            "isbn": "9780262033848",
            "title": "Introduction to Algorithms",
            "author": "Thomas H. Cormen",
            "publisher": "MIT Press",
            "volume": 4,
            "year": 2009,
            "isbn_code": "9780262033848"
        },
        # Add more sample books as needed
    ]

    # Add sample books to the library
    for book in books:
        print(library.add_book(**book))

    # Demonstrate functionality
    print("\nList of all books:")
    print(library.list_books())

    print("\nRetrieve a book by ISBN:")
    print(library.retrieve_book("9780134692883"))

    print("\nSearch books by title:")
    print(library.search_books("Operating System Concepts", "title"))

    print("\nUpdate a book's details:")
    print(library.update_book("9780134692883", author="A. Silberschatz"))
    print(library.retrieve_book("9780134692883"))

    print("\nCheck if a book is available by ISBN:")
    print(library.is_book_available("9780134692883"))

    print("\nRemove a book by ISBN:")
    print(library.remove_book("9780134692883"))
    print(library.list_books())

if __name__ == "__main__":
    main()
