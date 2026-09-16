import pyautogui
import time

# open the browser
pyautogui.click(x=1094, y=1061)
time.sleep(1)

# click on the three dots
pyautogui.click(x=1815, y=300)
time.sleep(1)

# Reply to all
pyautogui.click(x=1633, y=381)
time.sleep(1)

# click the pen
pyautogui.click(x=690, y=963)
time.sleep(1)

# click message
pyautogui.click(x=754, y=770)
time.sleep(1)

# click text
pyautogui.click(x=1434, y=866)
time.sleep(1)

# write date
pyautogui.write("16")