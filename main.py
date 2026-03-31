import sys
from stats import count_words, character_count, generate_report, select_dict_value
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path = sys.argv[1] #This checks for arguments from the CLI, it needs to have 1 argument (including main.py) to

def main(book_path):
        char_dict = character_count(book_path)
        total_words = count_words(book_path)
        char_count = select_dict_value(char_dict)
        generate_report(char_dict, total_words, char_count, book_path)

main(path)