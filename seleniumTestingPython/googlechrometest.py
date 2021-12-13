from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
import time


PATH = "/users/christophermumma/Documents/chromedriver"
driver = webdriver.Chrome(PATH)

url= "https://google.com"

driver.get(url)
print(driver.title)

search = driver.find_element_by_name("q")
search.send_keys("Chicago Bears")
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.save_screenshot("seleniumTestingPython/ChicagoBears.png")

driver.quit()