import pyautogui

# 절대 좌표로 마우스 이동
# pyautogui.moveTo(100, 100) # 지정 위치로 마우스 이동
# pyautogui.moveTo(100,200, duration=5) # 5초 동안 좌표로 마우스 이동

# 상대 좌표로 마우스 이동 (현재 커서 위치로부터)
pyautogui.move(100, 100)
print(pyautogui.position()) # 마우스 좌표 출력

p = pyautogui.position()
print(p[0], p[1]) # x, y
print(p.x, p.y) # x, y