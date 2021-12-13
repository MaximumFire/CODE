import codecs

hex1 = input("Enter a hexadecimal string: ")
hex2 = "686974207468652062756c6c277320657965"
hex1 = int(hex1, 16)
hex2 = int(hex2, 16)

# Bitwise XOR in python is "^"
print(hex(hex1 ^ hex2))
