from stats import get_num_words
from stats import char_counter
from stats import report
import sys
print(len(sys.argv))
#for arg in sys.argv[1:]:
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Now it's safe to use sys.argv[1]
file_path = sys.argv[1]


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
#books/frankenstein.txt
def main():
    text = get_book_text(file_path)
    x = text.split()
    y = get_num_words(x)
    z = char_counter(text)
    a = report(z)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {y} total words")
    print("--------- Character Count -------")
    for x in a:
        char = x["Letter"]
        counter = x["Count"]
        if char.isalpha() == True:
            print(f"{char}: {counter}")
    print("============= END ===============")
if __name__ == "__main__":
    main()

