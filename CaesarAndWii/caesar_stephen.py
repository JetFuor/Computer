#Made By Stephen

alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(word, key):
    new_word = ""
    for letter in word:
        # Go through each letter, first go 1 letter, shift it by key, then store somewhere else
        place = alphabet.find(letter)
        place = place + int(key)
        if place > 25:
            place = place - 26
        elif place < 0:
            place = place + 26
        new_word += alphabet[place]

    return new_word