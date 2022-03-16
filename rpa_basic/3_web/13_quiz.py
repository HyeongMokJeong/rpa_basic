from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.w3schools.com/')

# LEARN HTML 클릭
driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[1]/a[1]').click()
driver.implicitly_wait(2)

# HOW TO 클릭
driver.find_element_by_xpath('//*[@id="topnav"]/div/div/a[10]').click()
driver.implicitly_wait(2)

# Contact Form 클릭
driver.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[116]').click()
driver.implicitly_wait(2)

# 입력칸에 값 입력
list = ['나도','코딩','Canada','퀴즈 완료하였습니다.']
driver.find_element_by_xpath('//*[@id="fname"]').send_keys(list[0])
driver.find_element_by_xpath('//*[@id="lname"]').send_keys(list[1])
driver.find_element_by_xpath(f'//*[@id="country"]/option[text()="{list[2]}"]').click()
driver.find_element_by_xpath('//*[@id="main"]/div[3]/textarea').send_keys(list[3])

# 5초 대기 후 Submit 버튼 클릭
time.sleep(5)
driver.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()

# 5초 대기 후 브라우저 종료
time.sleep(5)
driver.quit()