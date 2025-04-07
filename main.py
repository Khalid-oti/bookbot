from stats import get_word_count, get_character_count, get_letter_count, get_total_char_count, get_total_letter_count
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1] #"books/frankenstein.txt"
    book_contents = get_book_contents(book_path)
    word_count = get_word_count(book_contents)
    character_count = get_character_count(book_contents)
    letter_count = get_letter_count(character_count)
    total_char_count = get_total_char_count(character_count)
    total_letter_count = get_total_letter_count(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter_dict in letter_count:
        print(f"{letter_dict["letter"]}: {letter_dict["count"]}")
    print("============= END ===============")
    #print(f"{total_letter_count} letters found in the document")
    #print(f"{total_char_count} characters found in the document")
    #print(character_count)
    #print(letter_count)

def get_book_contents(path):
    with open(path) as f:
        return f.read()



main()
