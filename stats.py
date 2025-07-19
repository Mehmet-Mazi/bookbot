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
