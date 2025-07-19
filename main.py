from stats import get_word_count, repeat_char_count

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    # print(text)
    word_count = get_word_count(text)
    print(f"{word_count} words found in the document")
    repeating_chars = repeat_char_count(text)
    print(repeating_chars)

main()
