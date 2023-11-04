# A simple library management system

# Define a book as a tuple with (title, author, genre)
Book = tuple[str, str, str]

# Initialize an empty list to store all books in the library
library = []

# Initialize a set to store different genres
genres = set()

# Initialize a dictionary to store borrowed books with user names
borrowed_books = {}

# Function to add a new book to the library
def add_book(title, author, genre):
    book = (title, author, genre)
    library.append(book)
    genres.add(genre)
    print(f"Book '{title}' by {author} added to the library under the genre '{genre}'.")

# Function to search for a book by title
def search_books(title):
    return [book for book in library if book[0].lower() == title.lower()]

# Function to borrow a book from the library
def borrow_book(title, user):
    for book in library:
        if book[0].lower() == title.lower():
            borrowed_books[title] = user
            library.remove(book)
            print(f"Book '{title}' has been borrowed by {user}.")
            return
    print(f"Book '{title}' is not available.")

# Function to return a book to the library
def return_book(title):
    if title in borrowed_books:
        user = borrowed_books.pop(title)
        for book in library:
            if book[0].lower() == title.lower():
                print(f"Book '{title}' has already been returned by {user}.")
                return
        print(f"Book '{title}' returned by {user}.")
    else:
        print(f"Book '{title}' was not borrowed.")

# Function to list all books in the library by genre
def list_books_by_genre():
    books_by_genre = {}
    for genre in genres:
        books_by_genre[genre] = [book for book in library if book[2] == genre]
    
    for genre, books in books_by_genre.items():
        print(f"\nGenre: {genre}")
        for book in books:
            print(f"Title: {book[0]}, Author: {book[1]}")

# Example usage
add_book("The Hobbit", "J.R.R. Tolkien", "Fantasy")
add_book("1984", "George Orwell", "Dystopian")
add_book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")

borrow_book("The Hobbit", "Alice")
list_books_by_genre()
return_book("The Hobbit")
