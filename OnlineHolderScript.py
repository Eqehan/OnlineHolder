import random

import pyautogui


i = 0

while i < 10:
    pyautogui.moveTo(500,500,duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(500, 1000, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(3000, 1000, duration=0.5)
    pyautogui.click()
    pyautogui.moveTo(3000, 500, duration=0.5)
    pyautogui.click()
    pyautogui.press('shift')