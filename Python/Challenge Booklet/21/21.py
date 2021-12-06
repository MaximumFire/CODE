import json

def get_details():
    data = ["", "", "", "", ""]
    data[0] = input("Enter your full name: ")
    data[1] = input("Enter your date of birth (DD/MM/YYYY): ")
    data[2] = input("Enter your email address: ")
    data[3] = input("Enter your phone number: ")
    data[4] = input("Enter your age: ")
    return data

res = []
seen = set()

def add_entry(res, name, dob, email, phone, age):

    # check if in seen set
    if (name, dob, email, phone, age) in seen:
        return res

    # add to seen set
    seen.add(tuple([name, dob, email, phone, age]))

    # append to results list
    res.append({'name': name, "dob": dob, "email": email, "phone": phone, "age": age})

    return res

def write_json(lst, fn):
    with open(fn, 'a', encoding="utf-8") as file:
        for item in lst:
            x = json.dumps(item, indent=4)
            file.write(x + "\n")

def main():
    global res
    while True:
        choice = input("What would you like to do? (add, search, quit): ")
        if choice == "add":
            while True:
                details = get_details()
                choice = input(f"Is this correct(y/n): {details} ")
                if choice == "y":
                    break
                else:
                    continue
            res = add_entry(res, *details)
            write_json(res, "members.json")
        elif choice == "quit":
            print("Thanks for using our system.")
            break
        else:
            return      
main()