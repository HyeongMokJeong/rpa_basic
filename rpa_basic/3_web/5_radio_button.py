from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')
driver.switch_to.frame('iframeResult') # frame 전환

elem = driver.find_element_by_xpath('//*[@id="html"]')

# 선택이 안 되어 있으면 선택하기
if elem.is_selected() == False:
    print("선택하기")
    elem.click()
else:
    print("이미 선택되어 있습니다.")

time.sleep(3)

if elem.is_selected() == False:
    print("선택하기")
    elem.click()
else:
    print("이미 선택되어 있습니다.")

driver.quit()