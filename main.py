
def get_book_text(path):
    book_contents = path.read()
    return book_contents

def get_word_count(text):
    words = []
    word_count = 0

    words = text.split()

    for i in range(0,len(words)):
        word_count += 1

    return word_count


def main():
    with open("books/frankenstein.txt") as f:
        text = (get_book_text(f))
        word_count = (get_word_count(text))
        print(f"{word_count} words found in the document")
main()