from stats import *

def main():
    file_path = "/Users/brandon/github/B-Spatial/bookbot/books/frankenstein.txt"

    print(get_book_text(file_path))
    count_words(get_book_text(file_path))

main()
