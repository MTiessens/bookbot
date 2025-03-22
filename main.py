def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def word_count(book_text):
    words = book_text.split()
    num_words = len(words)
    return f"{num_words} words found in the document"
    
book_text = get_book_text("books/frankenstein.txt")
result = word_count(book_text)
print(result)