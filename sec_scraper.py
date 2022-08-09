from selenium import webdriver

PATH = '/Users/ivanshaydulin/Personal/MyGit/SFD-Tracker/chrome_driver/chromedriver'
driver = webdriver.Chrome(PATH)
driver.get('https://www.sec.gov/')
# driver.close() - close tab
# driver.quit() - quit browser