from stats import get_word_count, repeat_char_count, get_sort_repeat_chars
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    repeating_chars = repeat_char_count(text)
    sorted_chars = get_sort_repeat_chars(repeating_chars)
    print_report(book_path, word_count, sorted_chars)

def print_report(book_path, word_count, sorted_chars_list):

    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {book_path}")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for char in sorted_chars_list:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")

    print("============= END ===============")

main()
