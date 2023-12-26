## (1) turn computer volume to 100%
## (2) set all minecraft volume to 0 except: 
## - master volume: set to 100
## - friendly creatures: set to 100
## (3) set device output to BlackHole 2ch
## (4) stand on block next to open water
## (5) holding fishing rod, position cursor on ocean horizon
## (6) pause minecraft, run program, start minecraft

# Constants
threshold = 20 # sound threshold

# Imports
import pyautogui
import time
import sounddevice as sd
import numpy as np

# countdown
def countdown():
    print("3")
    time.sleep(.75)
    print("2")
    time.sleep(0.75)
    print("1")
    time.sleep(0.75)
    print("fish!")

# how to click
def right_click_and_release():
    pyautogui.mouseDown(button="right")
    time.sleep(0.05)
    pyautogui.mouseUp(button="right")

## listen for fish and click! 
def listen_and_fish(indata, frames, t, status):
    volume = np.round(np.linalg.norm(indata) * 10, decimals = 2)
    if volume > threshold:
        print(" ".join([str(volume), "-> FISH DETECTED"]))
        right_click_and_release()
        time.sleep(0.5)
        right_click_and_release()
    else:
        print(str(volume))

## bring it together 
def main():
    countdown()
    right_click_and_release()
    with sd.InputStream(device="BlackHole 2ch", callback=listen_and_fish):
        while True:
            sd.sleep(1000)

## run it
if __name__ == "__main__":
    main()
