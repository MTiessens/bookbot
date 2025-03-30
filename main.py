import sys

if len(sys.argv) == 2:
    path_to_file = sys.argv[1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

from stats import word_count, char_sym_count, sort_char_count

# Remove the hardcoded filepath to books    
book_text = get_book_text(path_to_file)
words = book_text.split()
total_words = len(words)
char_counts = char_sym_count(book_text)
sorted_chars = sort_char_count(char_counts)
print("============ BOOKBOT ============")
print(f"Analyzing book found at {path_to_file}...")
print("----------- Word Count ----------")
print(f"Found {total_words} total words")
print("--------- Character Count -------")

for char_dict in sorted_chars:
    char = char_dict["character"]
    count = char_dict["count"]
    if char.isalpha():
        print(f"{char}: {count}")

print("============= END ===============")

