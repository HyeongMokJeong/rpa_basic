import pyautogui

pyautogui.sleep(3) # 3초 대기
# print(pyautogui.position())

# pyautogui.click(1070, 26, duration=1) # 1초 동안 해당 좌표로 이동 후 클릭
# pyautogui.mouseDown() # 마우스 왼쪽 누른 상태
# pyautogui.mouseUp() # 마우스 왼쪽 뗀 상태
# -> pyautogui.click()

# pyautogui.doubleClick()
# pyautogui.click(clicks=200) # clicks는 클릭 횟수

# pyautogui.moveTo(200, 200)
# pyautogui.mouseDown()
# pyautogui.moveTo(300, 300)
# pyautogui.mouseUp()

# pyautogui.rightClick()
# pyautogui.middleClick()

# pyautogui.moveTo()
# pyautogui.drag(100, 0) # 현재 위치 기준으로 x 100만큼, y 0만큼 드래그
# pyautogui.drag(100, 0, duration=0.25)
# pyautogui.dragTo(100, 100) # 절대 좌표 기준으로 x 100 y 100으로 드래그 

pyautogui.scroll(300) # 양수이면 위 방향으로, 음수이면 아래 방향으로 300만큼 스크롤
