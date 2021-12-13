#Simple Life Calc

def add_vat(original):
    return original * 1.2

def rem_vat(original):
    return original / 1.2

def get_tax(salary):
    if salary <= 12570:
        return [salary, 0, salary]
    if 12571 < salary <= 50270:
        temp = salary - 12570
        temp = temp / 1.2
        return [salary, temp, salary - temp]
    if 50271 < salary <= 150000:
        temp = salary - 50270
        temp2 = temp - 12570
        temp = temp / 1.4
        temp2 = temp2 / 1.2
        return [salary, temp + temp2, salary - temp - temp2]
    if salary > 150000:
        temp = salary - 150000
        temp2 = temp - 50270
        temp3 = temp2 - 12570
        temp = temp / 1.45
        temp2 = temp3 / 1.4
        temp3 = temp3 / 1.2
        return [salary, temp + temp2 + temp3, salary - temp - temp2 - temp3]
    
salary = int(input("Enter a salary to find the tax: "))
values = get_tax(salary)
print(f"The original salary is: {values[0]}, the total tax is: {values[1]}, and the salary minus the total tax is: {values[2]}")