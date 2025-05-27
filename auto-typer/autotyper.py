import pyautogui
import time
import random
import keyboard

# Text to type
text = """
your text goes here
"""
print("Autotyper will start in 5 seconds")
time.sleep(5)

# Keys that need to be held together to stop the script
stop_keys = ['Esc']

for char in text:
    # Check if all keys in stop_keys are pressed
    if all(keyboard.is_pressed(k) for k in stop_keys):
        print("\nScript stopped by user pressing n+i+g+e+r")
        break
 
    # Random chance to fake a typo and backspace it
    if random.random() < 0.02:  # 2% chance
        typo = random.choice('abcdefghijklmnopqrstuvwxyz')
        pyautogui.write(typo)
        time.sleep(random.uniform(0.05, 0.1))
        pyautogui.press('backspace')
        time.sleep(random.uniform(0.1, 0.2))

    pyautogui.write(char)

    # Delay between characters (more natural)
    if char in ['.', '!', '?']:
        time.sleep(random.uniform(0.4, 0.7))  # pause at sentence end
    elif char == ',':
        time.sleep(random.uniform(0.2, 0.4))  # pause at comma
    elif char == '\n':
        time.sleep(random.uniform(0.3, 0.5))  # paragraph break
    else:
        time.sleep(random.uniform(0.03, 0.12))  # normal typing speed

    # Occasionally pause like you're "thinking"
    if random.random() < 0.01:  # 1% chance
        time.sleep(random.uniform(0.5, 1.5))
