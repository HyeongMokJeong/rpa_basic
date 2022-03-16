from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.w3schools.com/html/')
driver.maximize_window()

driver.implicitly_wait(5)

# 특정 영역 스크롤
elem = driver.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[61]')

# 방법 1 : ActionChain
# actions = ActionChains(driver)
# actions.move_to_element(elem).perform()

# 방법 2 : # 좌표 정보 이용
xy = elem.location_once_scrolled_into_view
# 주 목적인 좌표 정보를 얻으면서 스크롤을 해줌
print("type : ", type(xy))
print("value : ", xy)