def number_of_words(book_text):
    word_count = len(book_text.split())
    return word_count

def count_characters(book_text):
    book_text = book_text.lower()
    frequency = {}
    for char in book_text:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

def sorting(frequency):
    
