def isValid(s: str) -> bool:
    isValid = None
    current_open = []
    for c in s:
        if (c == "(" or c == "[" or c == "{"):
            current_open.append(c)
        elif current_open == []:
            isValid = False
            break
        elif (c == ")" and current_open[len(current_open)-1] == "(") or (c == "]" and current_open[len(current_open)-1] == "[") or (c == "}" and current_open[len(current_open)-1] == "{"):
            current_open.pop(len(current_open)-1)
            isValid = True
        else:
            isValid = False
            break
    if current_open != []:
        isValid = False
    return isValid
                




print(isValid(s = "([]){"))