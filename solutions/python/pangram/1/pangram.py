def is_pangram(sentence):
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    for letter in abeceda:
        if letter not in sentence.lower():
            return False
    return True
