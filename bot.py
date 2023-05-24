import pyautogui
import time
import keyboard
import random
import win32api
import win32con
import numpy as np

time.sleep(2)

ORANGE = 238
MANAGERORANGE = 220
BLUE = 211
TOPLEFTBOX = 350
TOPRIGHTBOX = 1580
DISTANCEBETWEEN = 151


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def isColour(pixel, colour):
    if pixel == colour:
        return True
    else:
        return False


while keyboard.is_pressed('q') == False:
    if isColour(pyautogui.pixel(696, 623)[0], MANAGERORANGE):
        click(695, 625)
        time.sleep(np.random.uniform(0.2, 0.7))
        if isColour(pyautogui.pixel(1149, 643)[2], BLUE):
            time.sleep(np.random.uniform(0.1, 0.4))
            while isColour(pyautogui.pixel(1149, 643)[2], BLUE):
                click(1149, 643)
            # close manager window
            click(1801, 123)

    pos = TOPLEFTBOX
    for i in range(6):
        time.sleep(np.random.uniform(0.1, 0.3))
        if isColour(pyautogui.pixel(1175, pos)[0], ORANGE):
            click(1175, pos)
        pos = TOPLEFTBOX + (DISTANCEBETWEEN * i)
        print(pos)

    pos = TOPLEFTBOX
    for i in range(6):
        time.sleep(np.random.uniform(0.2, 0.6))
        if isColour(pyautogui.pixel(TOPRIGHTBOX, pos)[0],  ORANGE):
            click(TOPRIGHTBOX, pos)
        pos = TOPLEFTBOX + (DISTANCEBETWEEN * i)

    if ((pyautogui.pixel(1550, 70)[0] == 206)):
        click(1550, 70)
