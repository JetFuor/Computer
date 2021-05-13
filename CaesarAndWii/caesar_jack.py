
alphabet = "abcdefghijklmnopqrstuvwxyz"

def cipher(word, shift):
    output_text = ""
    for letter in word:
        index = alphabet.find(letter)
        index = index + int(shift)
        if index > 25:
            index = index - 26
        elif index < 0:
            index = index + 26
        output_text += alphabet[index]
    return output_text


if __name__ == "__main__":
    print("Hey, to encrypt set shift as a positive value")
    print("to decrypt set shift as a negative value")
    word_user = input("your text:")
    shift_user = input("shift by:")
    cipher("word_user", int(shift_user)) 

#assisted by stephen (●'◡'●)





    