import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

# pyautogui.write("12345")
# pyautogui.write("texttest",interval=0.25)

# pyautogui.write(['t','e','s','t','left','left','right','l','a','enter'], interval=0.25)

# 특수 문자
# pyautogui.keyDown("shift") # 누르고 있는 상태
# pyautogui.press("4") # 눌렀다가 뗌
# pyautogui.keyUp("shift") # 뗌

# 조합키 (Hot Key)
# pyautogui.hotkey("ctrl", "a")
# ctrl 누르고 > a 누르고 > a 떼고 > ctrl 떼고

# pyperclip 이용 한글 입력
import pyperclip
pyperclip.copy("테스트") # 텍스트를 클립보드에 저장
pyautogui.hotkey("ctrl", "v")

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

# 자동화 프로그램 종료
# win : ctrl + alt + del
# mac : cmd+ shift + option + q

