from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://shopping.naver.com/home/p/index.nhn")

driver.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]').send_keys("무선마우스")

driver.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]').click()

# 스크롤
# 지정한 위치로 스크롤 내리기
#driver.execute_script('window.scrollTo(0,1080)') # 모니터 해상도 이용

# 화면 가장 아래로 스크롤 내리기
# driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')


# 동적 페이지에 대해서 마지막까지 스크롤 반복 수행
interval = 2 # 2초에 한번씩 스크롤 내리기

# 현재 문서 높이를 가져와서 저장
prev_height = driver.execute_script('return document.body.scrollHeight')

# 반복 수행
while True:
    # 스크롤을 화면 가장 아래로 내림
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    # 페이지 로딩 대기
    time.sleep(1)

    # 현재 문서 높이 가져와서 저장
    curr_height = driver.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height:
        break
    
    prev_height = curr_height