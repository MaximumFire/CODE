import random, threading, time

actual = None

def enter_pin(attempt):
    global actual
    print("Entering.... " + str(attempt))
    if str(attempt) == str(actual):
        return True
    else:
        return False

def target1():
    global actual
    changed = ""
    for i in range(1, 5000):
        changed = str(i)
        if 0 < len(changed) < 4:
            while True:
                changed = "0" + changed
                if len(changed) == 4:
                    break
        actual = str(actual)
        if enter_pin(changed):
            print("The pin was successfully hacked as: " + str(changed))
            break

def target2():
    global actual
    changed = ""
    for i in range(5000, 10000):
        changed = str(i)
        actual = str(actual)
        if enter_pin(changed):
            print("The pin was successfully hacked as: " + str(changed))
            break

t1 = threading.Thread(target=target1)
t2 = threading.Thread(target=target2)

actual = input("Enter a pin: ")

if int(actual) >= 5000:
    t2.start()
    t2.join()
else:
    t1.start()
    t1.join()