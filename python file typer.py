import pyautogui

inp = input('File: ')

for x in open(inp, 'r').read():
   pyautogui.press(str(x))
