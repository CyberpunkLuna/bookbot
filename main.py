from stats import get_word_count
from stats import get_char_stats

def get_book_text(book_path):
    #reads a file and returns it as a string

    with open(book_path) as file:
        return file.read()

def main():
    # main function
    book_path = "./books/frankenstein.txt"
    book_string = get_book_text(book_path)
    word_count = get_word_count(book_string)
    char_stats = get_char_stats(book_string)
    print(f"{word_count} words found in the document")
    print(char_stats)

main()