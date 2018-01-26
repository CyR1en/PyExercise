from collections import namedtuple

Book = namedtuple("Book", "author title genre year price instock")
book_1 = Book("Sunny M", "C", "Fiction", 2000, 23, 10)
book_2 = Book("Sunny M", "A", "Fiction", 2000, 1231, 32)
book_3 = Book("Sunny M", "B", "Fiction", 2000, 20, 10)
book_4 = Book("Sunny M", "E", "Fiction", 2000, 1233, 42)
book_5 = Book("Sunny M", "D", "Fiction", 2000, 20, 10)

book_store_inventory = [book_1, book_2, book_3, book_4, book_5]

print("Printing unsorted")
for b in book_store_inventory:
    print(b.title + " by " + b.author)

sorted_inventory = sorted(book_store_inventory, key=lambda t: t.title)

print("Printing sorted")
for b in sorted_inventory:
    print(b.title + " by " + b.author)


def inv_val(book):
    return book.price * book.instock


def top_val(books):
    h_book = books[0]
    for iB in books:
        if inv_val(iB) > inv_val(h_book):
            h_book = iB
    return h_book


print("Top stocked: " + top_val(sorted_inventory).title)
