def phrase_to_acronym(phrase):
    words = phrase.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

if __name__ == "__main__":
    input_phrase = input("enter a phrase: ")
    if(phrase_to_acronym(input_phrase) == "ICE"):
        print("men that is freedommmmm")
    else:
        print(phrase_to_acronym(input_phrase))