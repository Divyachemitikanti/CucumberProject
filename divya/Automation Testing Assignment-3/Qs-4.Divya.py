from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Initialize the WebDriver (use the appropriate driver for your browser)
driver = webdriver.Chrome()  # Replace with webdriver.Chrome() if using Chrome


# Step 1: Open the URL and Login with credentials
driver.get("http://demo.opencart.com.gr/")
driver.maximize_window()
time.sleep(2)

# Click on MyAccount button
driver.find_element(By.XPATH, '//*[@id="top-links"]/ul/li[2]/a/span[1]').click()
time.sleep(5)

# Select Login button
driver.find_element(By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']").click()
time.sleep(5)

# Enter login credentials
driver.find_element(By.ID, "input-email").send_keys("divyachemitikanti24@gmail.com")  # Replace with valid email
driver.find_element(By.ID, "input-password").send_keys("Divya@1124")  # Replace with valid password
driver.find_element(By.XPATH, "//input[@value='Login']").click()
time.sleep(2)


driver.find_element(By.XPATH, "//a[@class='dropdown-toggle'][normalize-space()='Components']").click()
time.sleep(2)


driver.find_element(By.XPATH, "//a[normalize-space()='Monitors (2)']").click()
time.sleep(2)


dropdown = Select(driver.find_element(By.ID, "input-limit"))
dropdown.select_by_visible_text("25")
time.sleep(2)


driver.find_element(By.XPATH, "//*[@id='content']/div[3]/div[1]/div/div[2]/div[2]/button[1]").click()
time.sleep(2)


driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div[1]/ul[2]/li[2]/a").click()
time.sleep(2)



driver.find_element(By.XPATH, "(//button[@data-original-title='Add to Wish List'])[1]").click()
time.sleep(3)


success_message = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]")
time.sleep(3)


driver.find_element(By.NAME, "search").send_keys("Mobile")
driver.find_element(By.XPATH, "/html/body/header/div/div/div[2]/div/span/button").click()
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/div[2]/div/div/p[1]/label").click()
driver.find_element(By.XPATH,'//*[@id="button-search"]').click()


driver.find_element(By.LINK_TEXT, "HTC Touch HD").click()
time.sleep(2)


qty_box = driver.find_element(By.ID, "input-quantity")
qty_box.clear()
qty_box.send_keys("3")
time.sleep(2)


driver.find_element(By.ID, "button-cart").click()
time.sleep(3)


driver.find_element(By.XPATH, "/html/body/div[2]/div[1]")


driver.find_element(By.LINK_TEXT, "shopping cart").click()
time.sleep(3)


cart_items = driver.find_element(By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr/td[2]/a').text
assert "HTC Touch HD" in cart_items, "Item not found in the cart!"
print("Item verified in the cart!")


driver.find_element(By.LINK_TEXT, "Checkout").click()
time.sleep(2)


driver.find_element(By.LINK_TEXT, "My Account").click()
driver.find_element(By.LINK_TEXT, "Logout").click()
time.sleep(2)


driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/ul/li[5]/a").click()
driver.find_element(By.XPATH,'//*[@id="content"]')

driver.find_element(By.LINK_TEXT, "Continue").click()


# Close the browser
driver.quit()
