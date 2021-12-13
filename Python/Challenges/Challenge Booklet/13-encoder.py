alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

rotations = int(input("Enter a number of rotations for the cipher: ")) + 1

new_indexes = []
for letter in alphabet:
    i = alphabet.index(letter)
    i += rotations
    if i > 26:
        i -= 26
    new_indexes.append(i-1)

new_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
j = 0
for index in new_indexes:
    new_alphabet[j] = alphabet[index]
    j += 1

def translate(phrase):
    phraselist = []
    for i in phrase:
        phraselist.append(i)
    final = ""
    for j in phraselist:
        original_index = alphabet.index(j)
        new_letter = new_alphabet[original_index]
        final = final + new_letter
    print(final)

translate("hello")