import codecs

hex = input("Enter a hexadecimal string: ")
try:
    b64 = codecs.encode(codecs.decode(hex, "hex"), "base64").decode()
    print(f"{hex} in base64 is: {b64}")
except:
    print("That was not a valid hexadecimal string.")
