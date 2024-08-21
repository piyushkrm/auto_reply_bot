import pyautogui
import pyperclip
import time

# Small delay to give you time to switch to the application
time.sleep(2)

# Click the icon at (541, 1076)
pyautogui.click(961, 1045)

# Small delay before performing the drag
time.sleep(1)

# Click and drag from (538, 66) to (1908, 1030) to select the text
pyautogui.moveTo(716, 242)
pyautogui.dragTo(1295, 912, duration=1, button='left')

# Copy the selected text to the clipboard
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1358, 906)
# Small delay to ensure the text is copied
time.sleep(0.5)

# Get the text from clipboard using pyperclip
text = pyperclip.paste()

# Print the text to check if it's correctly copied
print(f"Copied Text: {text}")
