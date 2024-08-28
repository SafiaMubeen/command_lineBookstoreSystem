# Book Class
class Book:
    def __init__(self, isbn, title, author, price, copies):
        # Initialize the book attributes
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price
        self.copies = copies

    def update_inventory(self, quantity):
        # Update the number of available copies
        if quantity <= self.copies:
            self.copies -= quantity
        else:
            raise ValueError("Not enough copies available.")

    def display_info(self):
        # Display the book's information
        return f"{self.title} by {self.author} - ${self.price} ({self.copies} copies available)"

# Cart Class
class Cart:
    def __init__(self):
        # Initialize an empty cart and total cost
        self.books = []
        self.total_cost = 0

    def add_book(self, book, quantity):
        # Add a book to the cart and update the total cost
        self.books.append((book, quantity))
        self.total_cost += book.price * quantity

    def remove_book(self, isbn):
        # Remove a book from the cart and update the total cost
        for i, (book, quantity) in enumerate(self.books):
            if book.isbn == isbn:
                self.total_cost -= book.price * quantity
                del self.books[i]
                return
        print("Book not found in cart.")

    def calculate_total(self):
        # Return the total cost of books in the cart
        return self.total_cost

    def display_cart(self):
        # Display the contents of the cart
        cart_content = [f"{book.title} - {quantity} copies" for book, quantity in self.books]
        return "\n".join(cart_content)

# Store Class
class Store:
    def __init__(self):
        # Initialize an empty inventory
        self.inventory = []

    def add_book_to_inventory(self, book):
        # Add a book to the store's inventory
        self.inventory.append(book)

    def search_book(self, search_term):
        # Search for a book by ISBN, title, or author
        found_books = [book for book in self.inventory if search_term.lower() in book.isbn.lower() 
                       or search_term.lower() in book.title.lower() 
                       or search_term.lower() in book.author.lower()]
        return found_books

    def display_books(self):
        # Display all books in the inventory
        return "\n".join([book.display_info() for book in self.inventory])

    def checkout(self, cart):
        # Checkout books from the cart and update the inventory
        for book, quantity in cart.books:
            book.update_inventory(quantity)
        cart.books.clear()
        cart.total_cost = 0
        print("Purchase successful! Inventory updated.")

def main():
    # Create an instance of the Store and Cart
    store = Store()
    cart = Cart()

    # Add some books to the store inventory
    store.add_book_to_inventory(Book("1234567890", "Python Programming", "John Doe", 29.99, 10))
    store.add_book_to_inventory(Book("0987654321", "Learning AI", "Jane Smith", 39.99, 5))
    store.add_book_to_inventory(Book("5678901234", "Data Science 101", "Alice Brown", 24.99, 8))

    # Command-line interface
    while True:
        print("\nWelcome to the Command-Line Bookstore!")
        print("1. View all books")
        print("2. Search for a book")
        print("3. Add book to cart")
        print("4. Remove book from cart")
        print("5. View cart")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            # Display all books
            print(store.display_books())

        elif choice == '2':
            # Search for a book
            search_term = input("Enter ISBN, title, or author to search: ")
            found_books = store.search_book(search_term)
            if found_books:
                for book in found_books:
                    print(book.display_info())
            else:
                print("No books found.")

        elif choice == '3':
            # Add a book to the cart
            isbn = input("Enter the ISBN of the book you want to add: ")
            quantity = int(input("Enter the quantity: "))
            found_books = store.search_book(isbn)
            if found_books:
                book = found_books[0]
                if quantity <= book.copies:
                    cart.add_book(book, quantity)
                    print(f"{quantity} copy/copies of '{book.title}' added to the cart.")
                else:
                    print("Not enough copies available.")
            else:
                print("Book not found.")

        elif choice == '4':
            # Remove a book from the cart
            isbn = input("Enter the ISBN of the book you want to remove: ")
            cart.remove_book(isbn)

        elif choice == '5':
            # View the cart
            print("Your cart contains:")
            print(cart.display_cart())
            print(f"Total cost: ${cart.calculate_total():.2f}")

        elif choice == '6':
            # Checkout
            if cart.books:
                store.checkout(cart)
            else:
                print("Your cart is empty.")

        elif choice == '7':
            # Exit the system
            print("Thank you for visiting the Command-Line Bookstore!")
            break

        else:
            print("Invalid choice. Please try again.")

# Entry point of the script
if __name__ == "__main__":
    main()
