import xlutils
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome("C:\\Users\\nabay\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://staging-cassette.audiobee.ai/")
driver.maximize_window()

path = "C:\\Users\\nabay\\Downloads\\Testsheet.xlsx"

driver.find_element_by_link_text("Signup").click()

driver.implicitly_wait(2)



rows = xlutils.getRowCount(path, 'Signup')

for r in range(2, rows+1):
    FirstName = xlutils.readData(path, "Signup", r, 1)
    LastName = xlutils.readData(path, "Signup", r, 2)
    Email=xlutils.readData(path, "Signup", r, 3)
    Password= xlutils.readData(path,"Signup", r, 4)

    driver.find_element(By.XPATH, "//input[@placeholder='Enter your First Name']").send_keys(FirstName)
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your Last Name']").send_keys(LastName)
    driver.find_element(By.XPATH,"//input[@placeholder='Enter your email']").send_keys(Email)
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys(Password)

    driver.find_element(By.XPATH, "//input[@type='checkbox']").click()

    driver.find_element(By.XPATH, "//button[@variant='primary']").click()

    time.sleep(2)
    url = driver.current_url
    print(driver.title)
    print(url)

    if driver.current_url == "https://staging-cassette.audiobee.ai/sign-up":
        print("Fail")
        xlutils.writeData(path, "Signup", r, 5, "Fail")

        driver.refresh()



    elif driver.current_url == "https://staging-cassette.audiobee.ai":
        print("Fail")
        xlutils.writeData(path, "Signup", r, 5, "Fail")



    else:
        print("Pass")
        xlutils.writeData(path, "Signup", r, 5, "Pass")

        time.sleep(3)

        driver.find_element(By.XPATH, "//img[@class='sc-eCApnc iylGhi ant-dropdown-trigger']").click()

        driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-link ant-btn-dangerous']").click()









