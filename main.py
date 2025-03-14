from stats import get_word_count, count_characters, sort_dict
import sys

def get_book_text(path):
    book_contents = path.read()
    return book_contents


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    with open(sys.argv[1]) as path:
        text = (get_book_text(path))
        word_count = (get_word_count(text))
        chr_count_dict = count_characters(text)
        sorted_list = sort_dict(chr_count_dict)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for c in range(0, len(sorted_list)):
            print(f"{sorted_list[c]["char"]}: {sorted_list[c]["num"]}")
        print("============= END ===============")
        

main()