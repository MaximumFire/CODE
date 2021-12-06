import pyautogui
import threading
import time

exitFlag = False

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
        click(self.name)
        print("Exiting " + self.name)

def click(threadName):
    global exitFlag
    while True:
        screen = pyautogui.screenshot(region=(200, 151, 1723, 690))
        try:
            target = pyautogui.locateOnScreen("target.png", confidence=0.5)
            target = pyautogui.center(target)
            pyautogui.click(x=target[0], y=target[1])
        except Exception:
            print("target.png not found")
        if exitFlag:
            threadName.exit()
            break
    exitFlag = True

thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread3 = myThread(3, "Thread-3", 3)
thread4 = myThread(4, "Thread-4", 4)

thread1.start()
thread2.start()
thread3.start()
thread4.start()

print("Exiting main thread")
