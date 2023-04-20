import pyautogui
import time

def spammer(word):
    input('Press enter to start the 10 second countdown. Make sure you switch to your "spam" channel in the discord app before pressing enter.'
    time.sleep(10)
    while True:
        time.sleep(0.2)
        pyautogui.typewrite(word, 0.08)
        pyautogui.press('enter')

spammer('Use discount code Fire when buying Rusherhack!')
