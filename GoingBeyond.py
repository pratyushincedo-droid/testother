import time

from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from offboarding import click_element

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https:google.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//button[@type='button']").click()
wait = WebDriverWait(driver, 20)
email_box = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='i0116']"))
)
email_box.send_keys("test.in")
driver.find_element(By.XPATH, "//input[@id='idSIButton9']").click()
time.sleep(5)
# wait = WebDriverWait(driver, 10)
password_box = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='passwd']"))
)
password_box.send_keys("test")
time.sleep(5)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSIButton9"]'))).click()
time.sleep(5)
driver.find_element(By.ID, "idSIButton9").click()
time.sleep(5)

# Wait for dashboard container
dashboard_wait = WebDriverWait(driver, 25)
dashboard_wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[2]")))
# Click Employee Off-Boarding tile
click_element(driver, '//*[@id="root"]/div/div[2]/div[8]/div/button/div[1]/div/img')
time.sleep(8)

# Click Reporting Manager Clearance
driver.find_element(By.XPATH,"//button[normalize-space()='Reporting Manager Clearance']").click()
time.sleep(5)
# rm_clearance_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Reporting Manager Clearance']")))
# rm_clearance_btn.click()
# time.sleep(5)

# Click Employee, "Manager2"
driver.find_element(By.XPATH, "(//p[normalize-space()='View Details'])[1]").click()
time.sleep(2)

# Click Leave Review/Update (On behalf of employee)
leave_review_btn = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Leave Review/Update (On behalf of employee)']"))
)
leave_review_btn.click()
time.sleep(2)
# driver.find_element(By.XPATH,"//span[normalize-space()='Leave Review/Update (On behalf of employee)']").click()
# time.sleep(2)
driver.find_element(By.XPATH,"//div[@role='dialog']//div//input[@type='checkbox']").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//button[@type='button'][normalize-space()='Submit'])[2]").click()
time.sleep(2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(1)

# Click Knowledge Transfer
driver.find_element(By.XPATH, "(//input[@type='checkbox' and contains(@class,'MuiSwitch-input')])[2]").click()
time.sleep(2)

# Click Incedo Timesheet
driver.find_element(By.XPATH, "(//input[@type='checkbox' and contains(@class,'MuiSwitch-input')])[3]").click()
time.sleep(2)

# Click Client Timesheet
driver.find_element(By.XPATH,"//input[@data-indeterminate='false']").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

# Click Client Asset Handover
driver.find_element(By.XPATH,"//input[@data-indeterminate='false']").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

# Click Save
driver.find_element(By.XPATH,"//button[text()='Save']").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)









# wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@title='Going Beyond']"))).click()
# time.sleep(10)
# wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='+ Create Investment']"))).click()
# request_title = wait.until(EC.element_to_be_clickable((By.XPATH,
#                                                        "//label[normalize-space()='Request Title*']/following::input[1]"))
#                            )
# request_title.send_keys("Automation Testing")
# request_output = wait.until(
#     EC.element_to_be_clickable((
#         By.XPATH, "//label[normalize-space()='Request Output*']/following::textarea[1]"))
# )
# request_output.send_keys("Automation Testing Output")
# comboboxes = driver.find_elements(By.XPATH, "//input[@role='combobox' and @aria-autocomplete='list']")
# For Request Type
# Step 1: Click the combobox to open the dropdown
# comboboxes[0].click()
#
# # Step 2: Wait for dropdown options to appear (MUI renders them as <li> elements)
# option = wait.until(
#     EC.element_to_be_clickable((
#         By.XPATH,
#         "//li[normalize-space()='POC']"
#     ))
# )
#
# # Step 3: Click the option you want
# option.click()
# # For Request For
# comboboxes[1].click()
# option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[normalize-space()='Client']"))
#                     )
# option.click()
# # for priority
# # comboboxes[2].click()

comboboxes[0].click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//li[normalize-space()='POC']"))).click()
comboboxes[0].send_keys(Keys.ESCAPE)
# IMPORTANT: wait until the dropdown closes (prevents click interception)
wait.until(EC.invisibility_of_element_located((By.XPATH, "//ul[@role='listbox']")))

# Now the second combobox
comboboxes[1].click()
calendars = driver.find_elements(By.XPATH, "//body//div[@id='root']//div//div//div[1]//div[6]//div[1]//div[1]//div[1]//button[1]//*[name()='svg']")
calendars[0].click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[normalize-space()='30']").click()
time.sleep(2)
# 2) Get the visible picker container (Dialog OR Popper)
# picker = wait.until(EC.visibility_of_element_located((
#     By.XPATH,
#     "("
#     "//div[@role='dialog']"
#     " | //div[contains(@class,'MuiPickersPopper-root') and not(contains(@style,'display: none'))]"
#     ")"
# )))
#
# # 3) Click the day (example: 8) inside the open picker only
# day = wait.until(EC.element_to_be_clickable((
#     By.XPATH,
#     "("
#     "//div[@role='dialog']"
#     " | //div[contains(@class,'MuiPickersPopper-root') and not(contains(@style,'display: none'))]"
#     ")"
#     "//div[contains(@class,'MuiDayCalendar') or contains(@class,'MuiPickersCalendar')]"
#     "//button[@role='gridcell' and normalize-space()='8' and not(@disabled)]"
# )))
# day.click()
#
# # 4) Some variants require confirming with OK (safe to try)
# try:
#     picker.find_element(By.XPATH, ".//button[normalize-space()='OK']").click()
# except:
#     pass



# wait.until(EC.element_to_be_clickable((By.XPATH, "//li[normalize-space()='Client']"))).click()
# dialog = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))
# # Preferred: the cell marked as 'today'
# try:
#     dialog.find_element(By.XPATH, ".//button[@role='gridcell' and @aria-current='date' and not(@disabled)]").click()
# except:
#     dialog.find_element(By.XPATH, ".//button[normalize-space()='Today']").click()

# dialog = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))
# day_btn = wait.until(EC.element_to_be_clickable((
#     By.XPATH,
#     "//div[@role='dialog']"
#     "//div[contains(@class,'MuiPickersCalendar') or contains(@class,'MuiDayCalendar')]"
#     "//button[@role='gridcell' and normalize-space()='8' and not(@disabled)]"
# )))
# day_btn.click()
#
# # Some variants ask for confirmation
# try:
#     dialog.find_element(By.XPATH, ".//button[normalize-space()='OK']").click()
# except:
#     pass
# wait.until(EC.invisibility_of_element_located((By.XPATH, "//ul[@role='listbox']")))
# comboboxes[0].send_keys(Keys.ESCAPE)
#
#
#
#
#
# # Step 2: Wait until the dropdown listbox appears
# wait.until(EC.visibility_of_element_located((
#     By.XPATH, "//div[@role='presentation']//ul[@role='listbox']"
# )))
# # Step 3: Locate the "High" option inside the listbox
# opt_high = wait.until(EC.element_to_be_clickable((
#     By.XPATH,
#     "//div[@role='presentation']//ul[@role='listbox']//li[@role='option'][normalize-space()='High' or .//div[normalize-space()='High']]"
# )))
# # Step 4: Click the option using JavaScript to avoid overlay interception
# driver.execute_script("arguments[0].click();", opt_high)
# # Step 5: (Optional) Assert to verify value is now selected
#
# # Investment Start Date
# calendars = driver.find_elements(By.XPATH, "//button[@type='button' and @aria-label='Choose date']")
# calendars[0].click()
# date = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='8']"))
#                   )
# date.click()
#
# # project name
# project_name = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id=":r2c:"]')))
# project_name.send_keys("Automation_testing")
#
# # LOB
# comboboxes[3].click()
# division = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[normalize-space()='Wealth Management']")))
# division.click()
#
# # business unit
# comboboxes[4].click()
# vertical = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[normalize-space()='Wealth Management']")))
# vertical.click()