PROJECT README: WhatsApp Auto-Responder with Gemini AI

PROJECT DEMO VIDEO EXPLAINER : https://drive.google.com/file/d/1soryAd-w8vNJTxWUv6dyeaJ6IOxyBIj8/view?usp=sharing



OVERVIEW:

This project is an automation script written in Python that interacts with WhatsApp Desktop (or web wrapper). It captures incoming chat history by simulating mouse drag-and-drop actions, sends the text to the Google Gemini API (using the 'gemini-2.5-flash' model) with a specific persona ("Joyjit"), and automatically types and sends the AI's generated response back into the chat.



PREREQUISITES:

- Python 3.x installed on your machine.

- WhatsApp Desktop application open and positioned at the target chat.

- A valid Google Gemini API Key.



REQUIRED PYTHON LIBRARIES:

You will need to install the following packages using pip:

- pyautogui

- pyperclip

- google-genai



You can install them via terminal:

pip install pyautogui pyperclip google-genai



ENVIRONMENT SETUP:

Before running the script, you must set your Gemini API key as an environment variable in your operating system:

- On Windows (Command Prompt): 

  set GEMINI_API_KEY="your_api_key_here"

- On Linux/macOS: 

  export GEMINI_API_KEY="your_api_key_here"



HOW IT WORKS:

1. The script clicks on the taskbar/window to focus on WhatsApp.

2. It drags the mouse across a predefined coordinate box to select and copy the chat history to the clipboard.

3. It passes the chat conversation to the Google GenAI client, instructing it to respond as "Joyjit" like a genuine human.

4. The generated reply is copied to the clipboard, pasted into the WhatsApp message box, and automatically sent by pressing 'Enter'.



IMPORTANT NOTES & CONFIGURATION:

- Coordinate-Based Automation: This script relies heavily on hardcoded screen coordinates (`pyautogui.click`, `pyautogui.moveTo`, etc.). These values are specific to your monitor resolution, scaling settings, and window placement. You will likely need to adjust the pixel coordinates in the script to match your desktop layout.

- Safety and Ethics: Automating messaging apps can sometimes violate Terms of Service if abused. Use responsibly for personal automation and testing purposes.