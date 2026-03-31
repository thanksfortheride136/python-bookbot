#This function counts the amount of words in the book Frankenstein
def count_words():
    word_count = 0
    with open("books/frankenstein.txt") as word_counting:
        for words in word_counting:
            listed_words = words.split()           #splits string into sentences
            for individual_words in listed_words:  #splits string into words
                individual_words.split()
                word_count += 1
        return f"Found {word_count} total words"

#This function reads the entire book Frankenstein
def get_book_text():
    with open("books/frankenstein.txt") as f:
        print(f.read())


"""Iterates through each char and returns a dict count of each
    The first loop iterates through each line and could print 
    a word, the second loop interates through and could print char.
    the conditional checks if a value is in the dict and then counts the 
    values.
"""
def character_count():
    character_dict = {}
    with open("books/frankenstein.txt") as character_counts:
        for words in character_counts: 
            for chars in words:       
                lower_chars = chars.lower()
                if lower_chars not in character_dict:
                    character_dict[lower_chars] = 1  
                else:
                    character_dict[lower_chars] += 1
        return character_dict

#This is the function that uses the lambda value to sort. We obtain
#the kv pair using .items() then can sort by specifying K index value
def select_dict_value(dictionary): 
    dictionary_items = dictionary.items()
    dictionary = sorted(dictionary_items, key=lambda k: k[1], reverse=True)
    return dictionary


def generate_report(character_dictionary, words, character_count):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(words)
    print("--------- Character Count -------")
    for i in character_count:
        if i[0].isalpha():
            print(f"{i[0]}: {i[1]}")

    

    #Print greeting message & bookbot title
    #print returned number of words & word heading
    #iterate through each dict value and sort
    #print sorted value


                    
