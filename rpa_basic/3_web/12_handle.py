import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.w3schools.com/tags/att_input_type_radio.asp')

curr_handle = driver.current_window_handle
# 현재 윈도우 핸들 정보

# try it yourself 클릭
driver.find_element_by_xpath('//*[@id="main"]/div[2]/a').click()

handles = driver.window_handles # 모든 핸들 정보
for handle in handles:
    print(handle) # 핸들 정보 출력
    driver.switch_to_window(handle) # 각 핸들로 이동
    print(driver.title)

# 새로 이동된 브라우저에서 자동화 작업을 수행

# 그 브라우저를 종료
print('현재 핸들 닫기')
driver.close()

# 이전 핸들로 돌아오기
print('처음 핸들로 돌아오기')
driver.switch_to_window(curr_handle)

print(driver.title)
