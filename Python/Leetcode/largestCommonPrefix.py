def longestCommonPrefix(strs: list[str]) -> str:
    prefix = ""
    equal = None
    for i in range(0, len(strs[0])): # max length of prefix cannot be higher than length of 1st word
        current_char = strs[0][i]
        for j in range(0, len(strs)):
            try: 
                if current_char == strs[j][i]:
                    equal = True
                else:
                    equal = False
                    break
            except IndexError:
                equal = False
                break
        if equal:
           prefix += current_char
        else:
            break
    return prefix

strs = ["flower", "flow", "flight"]

print(longestCommonPrefix(strs=strs))

