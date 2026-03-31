
"""This function counts the amount of words in the book Frankenstein"""
def count_words(path):
    word_count = 0
    with open(path) as word_counting:
        for words in word_counting:
            listed_words = words.split()           #splits string into sentences
            for individual_words in listed_words:  #splits string into words
                individual_words.split()
                word_count += 1
        return f"Found {word_count} total words"

"""This function reads and can print the entire book Frankenstein"""
def get_book_text(path):
    with open(path) as f:
        print(f.read())


"""Iterates through each char and returns a dict count of each
    The first loop iterates through each line and could print 
    a word, the second loop interates through and could print char.
    the conditional checks if a value is in the dict and then counts the 
    values.
"""
def character_count(path):
    character_dict = {}
    with open(path) as character_counts:
        for words in character_counts: 
            for chars in words:       
                lower_chars = chars.lower()
                if lower_chars not in character_dict:
                    character_dict[lower_chars] = 1  
                else:
                    character_dict[lower_chars] += 1
        return character_dict

"""This is the function that uses the lambda value to sort. We obtain
the kv pair using .items() then can sort by specifying K index value"""
def select_dict_value(dictionary): 
    dictionary_items = dictionary.items()
    dictionary = sorted(dictionary_items, key=lambda k: k[1], reverse=True)
    return dictionary

"""This function prints a report and shows info about the book
    and removes any non-alphabetic chars"""
def generate_report(words, character_count, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(words)
    print("--------- Character Count -------")
    for i in character_count:
        if i[0].isalpha():
            print(f"{i[0]}: {i[1]}")
                    
