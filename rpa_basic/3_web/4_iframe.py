from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

driver.switch_to.frame('iframeResult') # frame 전환

elem = driver.find_element_by_xpath('//*[@id="html"]')
elem.click()

driver.switch_to.default_content() # 상위 프레임을 나옴