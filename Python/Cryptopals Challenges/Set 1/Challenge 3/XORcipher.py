import string

def frequencyCheck(value):
    frequencies = {}
    for char in value:
        try:
            frequencies[char] += 1
        except:
            frequencies[char] = 1
    return frequencies

def decodeHex(value, value2):
    a_string = bytes.fromhex(value)
    a_string = a_string.decode("ascii")
    return a_string

hexString = int("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", 16)
alphabet = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
alphabet2 = []
for i in alphabet:
    alphabet2.append(hex(i))

for letter in alphabet2:
    result = hexXOR(hexString, int(letter, 16))
    print(result)
    frequencies = frequencyCheck(str(result))
    highest = ""
    highest_freq = 0
    for frequency in frequencies:
        if frequencies[frequency] > highest_freq:
            highest = frequency
            highest_freq = frequencies[frequency]
    if highest == "e":
        print(result)
