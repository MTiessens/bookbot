def word_count(book_text):
    words = book_text.split()
    num_words = len(words)
    return {num_words}

def char_sym_count(book_text):
    elements = []
    base_text = book_text.lower()
    for char in base_text:
        elements.append(char)
    element_count = {}
    for char in elements:
        if char in element_count:
            element_count[char] += 1
        else:
            element_count[char] = 1
    return element_count
    
def sort_char_count(element_count):
    char_list = []
    for char, count in element_count.items():
        char_list.append({"character": char, "count": count})
    
    def sort_on(dict):
        return dict["count"]
    
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list




