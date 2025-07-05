def get_word_count(file_string):
    #counts the words within a given string

    words_list = file_string.split()
    return len(words_list)


def get_char_stats(file_string):
    #counts the number of times each character occurs
    
    sanitised = file_string.lower()
    char_dict = {}

    for char in sanitised:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict