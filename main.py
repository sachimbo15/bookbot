def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

if __name__ == "__main__":
    main()


def return_count(text):
    each_word = text.split()
    word_count = len(each_word)

    return word_count

def to_lowercase(text):
    #this converts to lowercase
    lowered_text = text.lower()
    char_count = {}

    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count


def count_words_and_characters(text):
    total_words = len(text.split())

    character_counts = {}
    for character in text:
        if character.isalpha():
            if character in character_counts:
                character_counts[character] += 1
            else:
                character_counts[character] = 1

    return total_words, character_counts

