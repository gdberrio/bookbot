import sys

from stats import count_chars, count_words, sort_list_dicts


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    frankenstein = get_book_text(book_path)
    number_of_words = count_words(frankenstein)
    number_of_chars = count_chars(frankenstein)
    sorted_chars = sort_list_dicts(number_of_chars)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for dicts in sorted_chars:
        if dicts["char"].isalpha():
            print(f"{dicts['char']}: {dicts['count']}")
    print("============= END ===============")


main()
