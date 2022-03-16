from PIL.ImageOps import grayscale
import pyautogui

# Window 버튼 + Shift + s -> 부분 캡처

# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# 이미지 발견 못하면 None 반환

# 같은 이미지 모두 찾기
# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i)

# 속도 개선
# 1. GrayScale # 이미지를 흑백으로 전환해서 속도 개선
# file_menu = pyautogui.locateOnScreen("file_menu.png", grayscale=True)
# pyautogui.click(file_menu)

# 2. 범위 지정
# file_menu = pyautogui.locateOnScreen("file_menu.png", region=(961, 6, 882 ,193))
# pyautogui.click(file_menu)

# 3. 정확도 조정
# run_btn = pyautogui.locateOnScreen("run_btn.png", confidence=0.9) # 90% 이상 일치하면 같다고 봄
# pyautogui.moveTo(run_btn)


# 자동화 대상이 바로 보여지지 않는 경우 (웹페이지 로딩 딜레이 등)
# 1, 계속 기다리기
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("발견 실패")
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     print("발견 실패")

# pyautogui.click(file_menu_notepad)

# 2. 일정 시간동안 기다리기 (TimeOut)
import time
import sys

# timeout = 10 # 10초 대기
# start = time.time() # 시작 시간 설정

# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time() # 종료 시간 설정
#     if end - start > timeout: # 지정한 10초를 초과하면
#         print("시간 종료")
#         sys.exit()

def find_target(img_file, timeout = 30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program. ")
        sys.exit()

my_click("file_menu_notepad.png", 10)