def repeat_char_count(text):
    repeat_char = {}
    for char in text:
        low_char = char.lower()
        if low_char not in repeat_char:
            repeat_char[low_char] = 0
        repeat_char[low_char] += 1
    return repeat_char

def get_word_count(text):
    return len(text.split())

def sort_on(items):
    return items["num"]

def get_sort_repeat_chars(char_dict):
    sort_list = []
    for key in char_dict:
        sort_list.append({"char":key, "num": char_dict[key]})
        
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list

