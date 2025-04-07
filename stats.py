def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    char_count = {}
    lowered_text = text.lower()
    for char in lowered_text:
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
            #new_char_dict[char] = count
            new_char_dict["letter"] = char
            new_char_dict["count"] = count
            chars_list.append(new_char_dict)
    def get_sorted(dict):
        #return dict[char]
        return dict["count"]
    chars_list.sort(reverse=True, key=get_sorted)
    return chars_list

def get_total_char_count(char_dict):
    return sum(char_dict.values())

def get_total_letter_count(letter_list):
    #return sum(letter_dict.values())
    total = 0
    for letter_dict in letter_list:
        total += letter_dict["count"]
    return total
