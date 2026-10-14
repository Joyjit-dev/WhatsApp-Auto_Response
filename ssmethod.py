import pyautogui
import time
import pyperclip


pyautogui.click(1265 , 1049)
time.sleep(1)

pyautogui.click(256 , 134)
time.sleep(10)

pyautogui.click(267 , 471)
time.sleep(2)


pyautogui.hotkey('win' , 'shift' , 's')
time.sleep(2)
#
pyautogui.moveTo(656, 231)
pyautogui.dragTo(1872, 931 , duration = 1.0 , button = 'left')
time.sleep(1)
pyautogui.hotkey('ctrl' , 'c')
time.sleep(1)

pyautogui.click(326,130)
time.sleep(5)

pyautogui.click(669 , 585)
time.sleep(1)

pyautogui.hotkey('ctrl' , 'v')
time.sleep(10)
pyautogui.typewrite('analyse the converstation and write an appropriate response for the latest message write just the reply so i can just copy and paste')
pyautogui.press('enter')
time.sleep(30)


pyautogui.moveTo(480, 583)
pyautogui.dragTo(1458, 865 , duration = 1.0 , button = 'left')

pyautogui.hotkey('ctrl' , 'c')
time.sleep(1)


pyautogui.click(256 , 134)
time.sleep(10)

pyautogui.click(267 , 471)
time.sleep(2)

pyautogui.click(872 , 977)
time.sleep(2)

pyautogui.hotkey('ctrl' , 'v')
time.sleep(1)
pyautogui.press('enter')

text = pyperclip.paste()

print(text)