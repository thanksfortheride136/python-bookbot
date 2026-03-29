#This function counts the amount of words in the book Frankenstein
def count_words():
    word_count = 0
    with open("books/frankenstein.txt") as word_counting:
        for words in word_counting:
            listed_words = words.split()           #splits string into sentences
            for individual_words in listed_words:  #splits string into words
                individual_words.split()
                word_count += 1
        print(f"Found {word_count} total words")

#This function reads the entire book Frankenstein
def get_book_text():
    with open("books/frankenstein.txt") as f:
        print(f.read())



def character_count():
    character_dict = {}
    with open("books/frankenstein.txt") as character_count:
        for words in character_count: 
            for chars in words: #chars prints each character out, i just nee to count them essentially
                if chars in character_dict:
                    character_dict.update({chars: character_dict[chars]})
                else:
                    character_dict.update({chars: value})
            print(character_dict[chars])
                    
