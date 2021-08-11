import xlutils
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:\\Users\\nabay\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://staging-cassette.audiobee.ai/")
driver.maximize_window()

#excel sheet path
path = "C:\\Users\\nabay\\Downloads\\Testsheet.xlsx"

#Rowcount from excel sheet
rows = xlutils.getRowCount(path, 'Login')

#reading data and looping
for r in range (2, rows+1):

            Email = xlutils.readData(path, "Login", r, 1)
            Password = xlutils.readData(path, "Login", r, 2)


#Finding element from login page and data entering to field

            driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys(Email)
            driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys(Password)
            driver.find_element(By.XPATH, "//input[@id='loginForm_rememberMe']").click()


            driver.find_element(By.XPATH, "//button[@variant='primary']").click()

            time.sleep(5)
            url=driver.current_url
            print(driver.title)
            print(url)


            if url== "https://staging-cassette.audiobee.ai/dashboard":
                print("pass")
                xlutils.writeData(path, "Login", r, 3, "Pass")

                driver.find_element(By.XPATH, "//img[@class='sc-eCApnc iylGhi ant-dropdown-trigger']").click()

                driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-link ant-btn-dangerous']").click()

            else:
                print("fail")
                xlutils.writeData(path, "Login", r, 3, "Fail ")
                driver.refresh()












