from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException

# reusable click function
def click_element(driver, xpath, wait_time=15):
    wait = WebDriverWait(driver, wait_time)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    driver.execute_script("arguments[0].click();", element)


# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://google.com")
wait = WebDriverWait(driver, 5)
# click sign in button
click_element(driver, '//*[@id="hero"]/div[1]/div/div[4]/button')
time.sleep(3)
# Wait for email input and enter email
email_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="i0116"]')))
email_input.clear()
email_input.send_keys("testuser.in")
# Click Next button using same helper
click_element(driver, '//*[@id="idSIButton9"]')
time.sleep(5)
# Enter password
password_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="i0118"]')))
password_input.clear()
password_input.send_keys("test")
click_element(driver, '//*[@id="idSIButton9"]')
time.sleep(3)
click_element(driver, '//*[@id="idBtn_Back"]')
# Wait for dashboard container
dashboard_wait = WebDriverWait(driver, 25)
dashboard_wait.until(EC.presence_of_element_located((By.XPATH, "//h2[normalize-space()='Travel']")))
# Click Employee Off-Boarding tile
click_element(driver, '//h2[normalize-space()="Travel"]')
time.sleep(5)
# Click create new travel request
driver.find_element(By.XPATH,"//p[normalize-space()='+ New Travel Request']").click()
time.sleep(2)

# Click title box,
driver.find_element(By.XPATH, "(//div[@role='combobox'])[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//li[normalize-space()='Mr.']").click()

# first name
driver.find_element(By.XPATH,"//input[@id='FirstMiddle-Name']").send_keys("buhead")
time.sleep(3)

# last name
driver.find_element(By.XPATH,"//input[@id='Last-Name']").send_keys("user")
time.sleep(3)

#
# gender
driver.find_element(By.XPATH,"(//div[@role='combobox'])[2]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//li[normalize-space()='Male']").click()
time.sleep(3)
#
# Select dob
driver.find_element(By.XPATH,"(//*[name()='svg'][@focusable='false'])[4]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[normalize-space()='5']").click()
time.sleep(3)

# # Select client name
driver.find_element(By.XPATH,"//button[2]//*[name()='svg']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@value='Cetera Financial Group']").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//input[@type='text'])[5]").send_keys('29.00')
time.sleep(3)
#
# # Select Locker & Key- (Recovery)
# driver.find_element(By.XPATH,"(//div[@role='combobox'])[4]").click()
# time.sleep(3)
# driver.find_element(By.XPATH,"//li[@role='option' and normalize-space()='Recovery']").click()
# time.sleep(3)
# driver.find_element(By.XPATH,"(//input[@type='text'])[7]").send_keys('1301')
# time.sleep(3)
# # Click Submit
# driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
# time.sleep(10)
# # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# # # time.sleep(3)
# # driver.find_element(By.XPATH,"//span[normalize-space()='Dushyant Goswami']")
# # time.sleep(3)
#
# driver.find_element(By.XPATH,"(//p[contains(text(),'View Details')])[7]").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
# time.sleep(3)
#
#
#
#

























# # Click Employee Clearance Screen
# click_element(driver, '//*[@id="root"]/div/div[1]/main/div[2]/div/div[1]/div[2]/button')
# WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[1]/main")))
# time.sleep(5)
# # Exit Feedback Form toggle clicked
#
#
#
#
# wait = WebDriverWait(driver, 20)
#
# # 1) Ensure the table is actually rendered
# wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']//table//tbody")))
#
# # 2) Locate the first row’s toggle by its visible container (label/span), not the hidden input
# #    This targets the MUI Switch root or switchBase inside td[2]
# toggle_container = wait.until(EC.presence_of_element_located((
#     By.XPATH,
#     "//*[@id='root']//table//tbody//tr[1]//td[2]//*[contains(@class,'MuiSwitch-root') "
#     "or contains(@class,'MuiSwitch-switchBase') or contains(@class,'MuiSwitch-thumb')]"
# )))
#
# # 3) Scroll the row into view (virtualized tables need this), then click safely
# driver.execute_script("arguments[0].scrollIntoView({block:'center'});", toggle_container)
#
# try:
#     wait.until(EC.element_to_be_clickable((By.XPATH,
#         "//*[@id='root']//table//tbody//tr[1]//td[2]//*[contains(@class,'MuiSwitch-root') "
#         "or contains(@class,'MuiSwitch-switchBase') or contains(@class,'MuiSwitch-thumb')]"
#     ))).click()
# except (ElementClickInterceptedException, TimeoutException):
#     # Fallback: JS click on the container
#     driver.execute_script("arguments[0].click();", toggle_container)
# time.sleep(2)
#
# driver.find_element(By.XPATH,"//span[normalize-space()='Personal Details Update']").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//div[@role='dialog']//div//input[@type='checkbox']").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"(//button[@type='button'][normalize-space()='Submit'])[3]").click()
# time.sleep(2)
# # 1) Toggle (use clickable, not presence)
# toggle = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']//table//tr[1]//td[2]//input[@type='checkbox']")))
# driver.execute_script("arguments[0].scrollIntoView({block:'center'});", toggle)
# toggle.click()
#
# # 2) Open the dialog via menu item text
# wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Personal Details Update']"))).click()
#
# # 3) Wait for the MUI dialog to be fully visible (role='dialog')
# dialog = wait.until(EC.visibility_of_element_located((
#     By.XPATH,
#     "//div[@role='dialog' and not(@aria-hidden='true')]"
# )))
#
# # 4) (Optional) Tick the checkbox inside the dialog (use relative path)
# chk = wait.until(EC.element_to_be_clickable((
#     By.XPATH, ".//input[@type='checkbox']"
# )))
# driver.execute_script("arguments[0].scrollIntoView({block:'center'});", chk)
# if not chk.is_selected():
#     chk.click()
#
# # 5) Wait for button to be enabled + visible and not covered by backdrop
# #    Avoid absolute /html/body/div[5] — use text-based relative locator
# submit_btn = wait.until(EC.visibility_of_element_located((
#     By.XPATH, ".//button[.//span[normalize-space()='Submit'] or normalize-space()='Submit']"
# )))
#
# # Some MUI buttons use 'disabled' attribute; ensure it's enabled
# wait.until(lambda d: submit_btn.is_enabled() and submit_btn.get_attribute("disabled") in (None, "false"))
#
# # MUI animates in; also ensure backdrop is not intercepting
# wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".MuiBackdrop-root.MuiModal-backdrop[style*='opacity: 1']")))
#
# # 6) Scroll button into view within the dialog and click with a safe fallback
# driver.execute_script("arguments[0].scrollIntoView({block:'center'});", submit_btn)
# try:
#     submit_btn.click()
# except ElementClickInterceptedException:
#     # Fallback to JS click if still intercepted by subtle overlay
#     driver.execute_script("arguments[0].click();", submit_btn)
#






# toggle_xpath = '//*[@id="root"]/div/div[1]/main/div[2]/div/div[3]/div/div/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/div/div/div/span/span[1]/input'
# toggle = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, toggle_xpath)))
# driver.execute_script("arguments[0].scrollIntoView({block:'center'});", toggle)
# driver.execute_script("arguments[0].click();", toggle)
# time.sleep(3)
#
# # Click Personal Details Update to open dialog
# personal_details_xpath = ("//span[normalize-space()='Personal Details Update']")
# personal_details = WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.XPATH, personal_details_xpath))).click()
# time.sleep(3)
# # Click the checkbox inside dialog
# driver.find_element(By.XPATH, "(//input[@type='checkbox'])[11]").click()
# time.sleep(3)
# # # Click Submit inside dialog
# # driver.find_element(By.XPATH,"(/html[1]/body[1]/div[8]/div[3]/div[1]/div[2]/button[2]").click()
# # time.sleep(3)
# # # Click Submit inside dialog
# # driver.find_element(By.XPATH, "/html/body/div[8]/div[3]/div/div[2]/button[2]").click()
# # time.sleep(3)
# submit_xpath = '/html/body/div[5]/div[3]/div/div[2]/button[2]'
# submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, submit_xpath)))
# wait = WebDriverWait(driver, 10)


