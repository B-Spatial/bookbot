def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words

def count_char(file_contents):
    text = file_contents.lower()
    counts = {}
    for ch in text:
        if ch not in counts:
            counts[ch] = 1
        else:
            counts[ch] +=1
    return counts

def sort_on(items):
    return items["num"]

def sort_dict(counts_dict):
    counts_list = []
    for k, v in counts_dict.items():
        entry = {"char": k, "num": v}
        counts_list.append(entry)
    counts_list.sort(reverse=True, key=sort_on)
    return counts_list