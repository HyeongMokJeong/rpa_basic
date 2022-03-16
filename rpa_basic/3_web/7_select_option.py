from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')

driver.switch_to.frame('iframeResult')

# elem = driver.find_element_by_xpath('//*[@id="cars"]/option[4]')
# elem.click()

# 텍스트 값을 통해 선택하는 방법
# elem = driver.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')
# elem.click()

# 텍스트 값이 부분 일치하는 항목 선택
elem = driver.find_element_by_xpath('//*[@id="cars"]/option[contains(text(), "Au")]')
elem.click()