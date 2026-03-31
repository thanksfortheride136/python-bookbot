from stats import count_words, character_count, generate_report, select_dict_value
def main():
    char_dict = character_count()
    total_words = count_words()
    char_count = select_dict_value(char_dict)
    select_dict_value(char_dict)
    generate_report(char_dict, total_words, char_count)
  

main()