from stats import count_words, character_count, generate_report, sort_character_values, select_dict_value
def main():
    char_dict = character_count()
    total_words = count_words()
    sorted_dict = sort_character_values(char_dict)

    generate_report(char_dict, total_words, sorted_dict)
  

main()