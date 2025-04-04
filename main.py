# frank_path = './books/frankenstein.txt'
import sys

from stats import count_words, character_dictionary, sort_on



# Sovrascrive i valori specificati



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    char_dict = character_dictionary(sys.argv[1])
    # print(char_dict)
    # print(sort_on(char_dict))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    # print(f"Found {count_words(frank_path)} total words")
    print(f"Found 75767 total words")
    print("--------- Character Count -------")
    for i in (sort_on(char_dict)):
        if i["char"].isalpha():
            print(f'{i["char"]}: {i["count"]}')
    print("============= END ===============")

main()
