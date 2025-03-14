
def get_book_text(path):
    book_contents = path.read()
    return book_contents

def main():
    with open("books/frankenstein.txt") as f:
        print(get_book_text(f))

main()