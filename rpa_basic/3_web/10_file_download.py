from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('prefs',{'download.default_directory':r'C:\Users\jhm10\Desktop\pg\파이썬'})

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

driver.switch_to.frame('iframeResult')

elem = driver.find_element_by_xpath('/html/body/p[2]/a')
elem.click()