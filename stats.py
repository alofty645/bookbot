def number_of_words(book_text):
    word_count = len(book_text.split())
    return word_count

def count_characters(book_text):
    book_text = book_text.lower()
    frequency = {}
    for char in book_text:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


