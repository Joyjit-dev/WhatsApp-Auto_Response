import pyautogui
import time
import pyperclip
from google import genai

import os
from google import genai

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY environment variable is not set."
    )

client = genai.Client(api_key=api_key)

pyautogui.click(1265 , 1049)
time.sleep(1)

"""pyautogui.click(256 , 134)
time.sleep(7)"""

pyautogui.click(267 , 550)
time.sleep(2)

pyautogui.moveTo(660, 235)
pyautogui.dragTo(1872, 931 , duration = 1.0 , button = 'left')

pyautogui.hotkey('ctrl' , 'c')
time.sleep(1)
pyautogui.click(900 , 900)

chat_hist=pyperclip.paste()

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
        "You are a person named Joyjit . you analyse the conversation and just write the reply to the latest message like a genuine human",
        chat_hist
    ]
)

output_text = response.text
print(output_text)

# This copies the text to your clipboard automatically
pyperclip.copy(output_text)


pyautogui.click(872 , 977)
time.sleep(2)

pyautogui.hotkey('ctrl' , 'v')
time.sleep(1)
pyautogui.press('enter')

text = pyperclip.paste()

print(text)