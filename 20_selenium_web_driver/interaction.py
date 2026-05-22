from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.wikipedia.org/")


# Click
english_link = driver.find_element(By.XPATH, '//*[@id="js-link-box-en"]/strong')
# english_link.click()

# english_link = driver.find_element(By.LINK_TEXT, "English")
english_link.click()

# Typing
search_bar = driver.find_element(By.NAME, value="search")
search_bar.send_keys("Python")
 
# Sending keyboard input to Selenium
search_bar.send_keys(Keys.ENTER)
 
# driver.quit() 
