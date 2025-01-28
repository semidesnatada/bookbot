def main(file_path):
    book_text = get_file_content(file_path)
        
    word_count = get_word_count(book_text)

    character_count = get_character_counts(book_text)

    print_report(file_path, word_count, character_count)

def get_word_count(text):
    word_count = len(text.split())
    return word_count

def get_character_counts(text):
    
    character_count = {}

    lowered_text = text.lower()

    for char in lowered_text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count

def sort_on(dict):
    return dict["count"]

def print_report(file_path, word_count, character_counts):

    prepped_char_count = []

    for char, count in character_counts.items():
        prepped_char_count.append({"char": char, "count": count})

    prepped_char_count.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")

    for word_dict in prepped_char_count:
        if word_dict["char"].isalpha():
            print(f"The '{word_dict['char']}' character was found {word_dict['count']} times")

    print("--- End report ---")

def get_file_content(file_path):
    with open(file_path) as f:
        return f.read()

if __name__ == "__main__":
    frank_path = "books/frankenstein.txt"
    main(frank_path)
