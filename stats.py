def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")

def count_char(file_contents):
    text = file_contents.lower()
    counts = {}
    for ch in text:
        if ch not in counts:
            counts[ch] = 1
        else:
            counts[ch] +=1
    return counts