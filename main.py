from stats import *
import sys

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def print_report(filepath, charactercount, sortedlist):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {charactercount} total words")
    print("--------- Character Count -------")
    for item in sortedlist:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    wordcount = number_of_words(book_text)
    charactercount = count_characters(book_text)
    sortedlist = chars_dict_to_sorted_list(charactercount)
    print_report(filepath, wordcount, sortedlist)

main()