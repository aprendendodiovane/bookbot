def main():
    with open("./books/frankenstein.txt", "r") as f:
        report(document_letters(f.read()))

def count_words(line):
    quantity_of_words = 0
    for _ in line.split():
        quantity_of_words += 1
    return quantity_of_words

def document_letters(line):
    letters_document = {}
    line = line.lower()
    for word in line.split():
        for letter in word:
            if letter in letters_document:
                letters_document[letter] += 1
            else:
                letters_document[letter] = 1
    return letters_document

def report(document):
    for letter in document.keys():
        if letter.isalpha():
            print(f"The '{letter}' character was found {document[letter]} times")

main()