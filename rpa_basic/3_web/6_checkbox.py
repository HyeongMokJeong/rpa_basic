from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')

driver.switch_to.frame('iframeResult')

# elem = driver.find_element_by_xpath('//*[@id="vehicle1"]')
# By 모듈을 이용한 간략화
elem = driver.find_element(By.XPATH, '//*[@id="vehicle1"]')
if elem.is_selected() == False:
    print("선택하기")
    elem.click()
else:
    print("이미 선택되어 있습니다.")

time.sleep(3)