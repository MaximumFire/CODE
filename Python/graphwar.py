def get_expression(type: str, values: list):
    if type == "step":
        k, a, c = values
        return f"{k}/(1+exp(-{a}*(x+{-c})))"
    elif type == "spike":
        k, a, c = values
        return f"{k}/(1+({a}(x+{-c}))^2)"
    elif type == "diag":
        a, b, c = values
        a = a / 2
        return f"{a}(abs(x+{-b})-abs(x+{-c}))"
    elif type == "sine":
        a, b = values
        return f"{a}(sin({b}x))"
    elif type == "dsine":
        k, a, b, c = values
        return f"{b}(sin({k}x))/(1+exp(-{a}*(x+{-c})))"

def main():
    numParams = {"step": 3, "spike": 3, "diag": 3, "sine": 2, "dsine": 4}
    params = {"step": ["What is the change in y you would like? : ",
                       "How steep should the step be? (100 is straight) : ",
                       "What is the x position the step should be at? : "],
              "spike": ["How tall should the spike be? : ",
                        "How steep should the spike be? (50 is straight) : ",
                        "What is the x position the spike should be at? : "],
              "diag": ["What should the gradient of the diagonal be? (normally 1 or 0.5) : ",
                       "What x position should the diagonal start at? : ",
                       "What x position should the diagonal end at? : "],
              "sine": ["What should the amplitude of the sine wave be? : ",
                       "What should the frequency of the sine wave be? : "],
              "dsine": ["What should the frequency of the sine wave be? : ",
                        "How quickly should the sine wave start? (50 is straight away) : ",
                        "What should the amplitude of the sine wave be? : ",
                        "What x position should the sine wave start at? : "]}
    while True:
        chain = ""
        type = input("Enter type of graph to generate expression for. (step, spike, diag, sine, dsine or exit) : ")
        if type == "exit":
            break
        values = []
        for i in range(numParams[type]):
            values.append(int(input(params[type][i])))
        print("---------- Generated Expression ----------")
        chain = get_expression(type=type, values=values)
        print(chain)
        print("------------------------------------------")
        choice = input("Would you like to chain another graph onto that one? (y or n) : ")
        while choice == "y":
            print("------------------------------------------")
            type = input("Enter type of graph to chain onto the expression for. (step, spike, diag, sine or dsine) : ")
            values = []
            for i in range(numParams[type]):
                values.append(int(input(params[type][i])))
            chain += " + "
            chain += get_expression(type=type, values=values)
            choice = input("Would you like to chain another graph onto that one? (y or n) : ")
        print("------------------------------------------")
        print(chain)
        print("------------------------------------------")
        
if __name__ == "__main__":
    main()