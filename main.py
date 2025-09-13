def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")


def main():
    file_path = "/Users/brandon/github/B-Spatial/bookbot/books/frankenstein.txt"
    print(get_book_text(file_path))
    count_words(get_book_text(file_path))

main()
