import pyautogui
import webbrowser
import time

is_playing = False

def play_spotify(song):
    global is_playing
    if is_playing:
        print("Music is already playing.")
        return

    webbrowser.open('https://open.spotify.com/')
    time.sleep(10)
    pyautogui.click(1000, 150) 
    time.sleep(1)
    pyautogui.typewrite(song)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.click(900, 610)
    time.sleep(1)
    pyautogui.press('space')
    is_playing = True

def stop_music():
    global is_playing
    if is_playing:
        pyautogui.hotkey('ctrl', 'w')
        is_playing = False
