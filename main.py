from stats import count_words


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


def main():
    frankenstein = get_book_text("./books/frankenstein.txt")
    number_of_words = count_words(frankenstein)
    print(f"{number_of_words} words found in the document")


main()
