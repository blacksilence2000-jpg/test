def phrase_to_acronym(phrase):
    words = phrase.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

if __name__ == "__main__":
    input_phrase = input("enter a phrase: ")
    if(phrase_to_acronym(input_phrase) == "NIGGER"):
        print("men that racist")
    else:
        print(phrase_to_acronym(input_phrase))