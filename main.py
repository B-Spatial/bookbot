from stats import *
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    else:
        path = sys.argv[1]
        text = get_book_text(path)



    num_words = count_words(text)
    #char_count = (count_char(text))
    sorted_dict = (sort_dict(count_char(text)))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path} ...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_dict:
        if not item["char"].isalpha(): continue
        
        else:
            print (f"{item['char']}: {item['num']}")


main()
