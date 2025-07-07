from stats import get_word_count
from stats import get_char_stats
from stats import split_sort
import sys

def get_book_text(book_path):
    #reads a file and returns it as a string

    with open(book_path) as file:
        return file.read()

def main():
    # main function
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_string = get_book_text(book_path)
    word_count = get_word_count(book_string)
    char_stats = get_char_stats(book_string)
    sorted_dict = split_sort(char_stats)

    #The following is fornmatting for the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print ("--------- Character Count -------")
    for item in sorted_dict:
        if item["name"].isalpha():
            print(f"{item["name"]}: {item["num"]}")
    print("============= END ===============")

main()