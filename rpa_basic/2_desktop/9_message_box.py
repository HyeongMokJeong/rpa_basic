import pyautogui
# pyautogui.countdown(3)
# print("자동화 시작")

# pyautogui.alert("자동화 수행에 실패하였습니다.", "경고") # 확인 버튼만 있는 팝업

# result = pyautogui.confirm("계속하시겠습니까?", "확인") # 확인, 취소
# print(result) # OK or Cancel 반환

# result = pyautogui.prompt("파일명을 무엇으로 하시겠습니까?", "입력") # 사용자 입력
# print(result)

result = pyautogui.password("암호를 입력하세요.") # 암호 입력
print(result)