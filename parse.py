
board_letters = "bowlmne"  # Enter all board letters
key_letter = "b"  # Enter the center yellow letter


board_letters = set((key_letter.lower() + board_letters.lower()))

alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z'}

invalid_letters = alphabet - board_letters

def get_valid_words():
    with open("dict.txt", "r") as file:
        valid_words = set()
        for line in file:
            if len(line[0:-1]) > 3 and key_letter in line and line[0:-1] not in valid_words and any(c in invalid_letters for c in line[0:-1]) is False:
                valid_words.add(line[0:-1])
    return valid_words

sorted_list = sorted(get_valid_words(), key=len)


print(sorted_list)