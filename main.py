from stats import get_word_count
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
    print(f"{word_count} words found in the document")
    #print(character_count)
    #print(letter_count)

def get_book_contents(path):
    with open(path) as f:
        return f.read()

def get_character_count(text):
    char_count = {}
    lowered_text = text.lower()
    for word in lowered_text:
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def get_letter_count(char_dict):
    chars_list = []
    for char in char_dict:
        if char.isalpha():
            new_char_dict = {}
            count = char_dict[char]
            new_char_dict["letter"] = char
            new_char_dict["count"] = count
            chars_list.append(new_char_dict)
    def get_sorted(dict):
        return dict["count"]
    chars_list.sort(reverse=True, key=get_sorted)
    return chars_list






main()
