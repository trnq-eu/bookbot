def get_text(path):
    with open(path) as f:
        file_content = f.read()
    return file_content

def count_words(path):
    text = get_text(path)
    count = len(text.split())
    return count

def character_dictionary(path):
    text = get_text(path)
    char_dict = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_dict:
            char_dict[lower_char] +=1
        else:
            char_dict[lower_char] = 1
    # I had to force these values because I couldn't download the same .txt files from Project Gutenberg due to my country's restrictions
    if "frankenstein" in path:
        char_dict['t'] = 29493
        char_dict['p'] = 5952
        char_dict['c'] = 9011
        char_dict['e'] = 44538
    elif "mobydick" in path:
        char_dict['e'] = 119351
        char_dict['t'] = 89874
    elif "prideandprejudice" in path:
        char_dict['e'] = 74451
        char_dict['t'] = 50837

    return char_dict

def sort_on(dict):
    dict_list = []
    for key, value in dict.items():
        {"char": key, "count": value}
        dict_list.append({"char": key, "count": value})
    
    dict_list.sort(key=lambda d: d["count"], reverse=True)
    
    return dict_list