import pyautogui, pyperclip

pyautogui.keyDown("win")
pyautogui.press("r")
pyautogui.keyUp("win")
pyautogui.write("mspaint")
pyautogui.press("enter")

pyautogui.sleep(1)
w = pyautogui.getWindowsWithTitle("제목 없음")[0]
if w.isMaximized == False:
    w.maximize()

w_btn = pyautogui.locateOnScreen("write_btn.png")
if w_btn:
    pyautogui.click(w_btn)
else:
    print("버튼을 찾을 수 없습니다.")

pyautogui.move(0, 300)
pyautogui.click()
pyautogui.sleep(1)
pyperclip.copy("참 잘했어요")
pyautogui.hotkey("ctrl", 'v')

pyautogui.sleep(5)
w.close()
pyautogui.press("n")
