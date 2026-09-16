import pyautogui
import time

# TO COPY SYSTEM DATA
pyautogui.click(x=1224, y=1056)
time.sleep(0.5)
pyautogui.click(x=552, y=538)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "c")

# TO OPEN EXCEL
pyautogui.click(x=1266, y=1051)
time.sleep(1)
pyautogui.click(x=1053, y=938)
time.sleep(0.5)
pyautogui.click(x=1353, y=243)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

# OPEN THE SYSTEM AGAIN
pyautogui.click(x=1224, y=1064)
time.sleep(0.5)
pyautogui.click(x=650, y=537)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "c")

# TO OPEN EXCEL AGAIN
pyautogui.click(x=1266, y=1051)
time.sleep(1)
pyautogui.click(x=1053, y=938)
time.sleep(0.5)
pyautogui.click(x=1555, y=246)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)

# OPEN THE SYSTEM AGAIN
pyautogui.click(x=1224, y=1064)
time.sleep(0.5)
pyautogui.click(x=1113, y=538)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "c")

# TO OPEN EXCEL AGAIN
pyautogui.click(x=1266, y=1051)
time.sleep(1)
pyautogui.click(x=1053, y=938)
time.sleep(0.5)
pyautogui.click(x=1447, y=250)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)