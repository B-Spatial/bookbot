def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")


def main():
    print(get_book_text("/Users/brandon/github/B-Spatial/bookbot/books/frankenstein.txt"))
    count_words(get_book_text("/Users/brandon/github/B-Spatial/bookbot/books/frankenstein.txt"))

main()
