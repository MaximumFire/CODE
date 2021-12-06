try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import pyautogui as pg
from time import sleep as s

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

s(3)

words = []

while True:
    pg.screenshot("Macros/Human-benchmark/Verbal-memory/Text.png", region=(400,400, 1000,90))

    text = pytesseract.image_to_string(Image.open('Macros/Human-benchmark/Verbal-memory/Text.png'))


    if text in words:
        button = pg.locateOnScreen("Macros/Human-benchmark/Verbal-memory/Seen.PNG", confidence=0.75)
        pg.click(button)

    else:
        button =pg.locateOnScreen("Macros/Human-benchmark/Verbal-memory/New.PNG", confidence=0.75)
        pg.click(button)
        words.append(text)
    
    pg.move(0,100)
    s(0.1)
    