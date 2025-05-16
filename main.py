from stats import *

filepath = 'books/frankenstein.txt'  

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()




def main():
    book_text = get_book_text(filepath)
    wordcount = number_of_words(book_text)
    charactercount = count_characters(book_text)
    
    print(f"{wordcount} words found in the document")
    print(charactercount)
main()