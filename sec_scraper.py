from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

ticker = 'FSLR'

PATH = '/Users/ivanshaydulin/Personal/MyGit/SFD-Tracker/chrome_driver/chromedriver'
driver = webdriver.Chrome(PATH)
driver.get('https://www.sec.gov/edgar/search/')
# driver.close() - close tab
# driver.quit() - quit browser
search = driver.find_element('id', 'entity-short-form')
# element2 = driver.find_element_by_id('date-range-select') entity-full-form

driver.implicitly_wait(10)

search.send_keys(ticker)
search.send_keys(Keys.RETURN)