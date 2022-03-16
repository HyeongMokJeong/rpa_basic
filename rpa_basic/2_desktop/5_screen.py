import pyautogui

# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장

# pyautogui.mouseInfo()
# 1020,24 60,169,242 #3CA9F2

pixel = pyautogui.pixel(1020, 24)
print(pixel)

# print(pyautogui.pixelMatchesColor(1020, 24, (60,169,242)))
print(pyautogui.pixelMatchesColor(1020, 24, pixel))
