import pyautogui
# pyautogui.FAILSAFE = False 
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용
# pyautogui.mouseInfo()

for i in range(10):
    pyautogui.move(100,100)
    # pyautogui.sleep(1)
    # 중지 시키고 싶다면 모서리 중 한곳으로 커서 옮기기
    # FAILSAFE 옵션을 끄면 작동 안함 (비추천)