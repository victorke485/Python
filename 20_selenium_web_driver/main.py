from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/Garmin-Forerunner-Smartwatch-Colorful-Training/dp/B0CT3SGHXL/")

price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole").text
price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction").text

print(f"The price is {price_dollar}.{price_cents}")

# driver.close() # Close current tab
driver.quit() # Close entire window
