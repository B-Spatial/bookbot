from stats import *

def main():
    file_path = "/Users/brandon/github/B-Spatial/bookbot/books/frankenstein.txt"

    text = get_book_text(file_path)
    #print(text)

    num_words = count_words(text)
    char_count = (count_char(text))
    sorted_dict = (sort_dict(count_char(text)))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    #print(char_count)
    #print(sorted_dict)
    for item in sorted_dict:
        if not item["char"].isalpha(): continue
        
        else:
            print (f"{item["char"]}: {item["num"]}")


main()
