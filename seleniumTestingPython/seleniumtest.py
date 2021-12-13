from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
import time


PATH = "/users/christophermumma/Documents/chromedriver"
driver = webdriver.Chrome(PATH)

url= "https://techwithtim.net"

driver.get(url)
print(driver.title)

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.save_screenshot("seleniumTestingPython/image.png")

driver.quit()
