import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def master():
    driver = webdriver.Chrome("C:\\Users\\nabay\\Downloads\\chromedriver_win32\\chromedriver.exe")

    driver.get("https://staging-cassette.audiobee.ai/login")
    driver.maximize_window()

    time.sleep(2)
    return driver


class SignupTest_P(unittest.TestCase):

    def test2(self):
        driver = master()

        driver.find_element_by_link_text("Signup").click()
        driver.implicitly_wait(4)

        driver.find_element(By.XPATH, "(//button[@type='button'])[1]").click()

        driver.implicitly_wait(2)

        driver.find_element(By.XPATH, "(//button[@type='button'])[1]").click()

        driver.find_element(By.XPATH, "//input[@placeholder='Enter your First Name']").send_keys("")
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your Last Name']").send_keys("")
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("")
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("")

        driver.find_element(By.XPATH, "//input[@type='checkbox']")

        driver.find_element(By.XPATH, "//button[@variant='primary']").click()

        text1 = driver.find_element(By.XPATH,"//div[contains(text(),'First name is required.')]").text
        text2 = driver.find_element(By.XPATH,"//div[contains(text(),'Last name is required.')]").text
        text3 = driver.find_element(By.XPATH, "//div[contains(text(),'Email is required.')]").text
        text4 = driver.find_element(By.XPATH, "//div[contains(text(),'Passwords must have at least 8 characters with one lowercase, uppercase, number, and special character.')]").text
        text5 = driver.find_element(By.XPATH, "//div[contains(text(),'Should accept terms and condtions.')]").text

        self.assertEqual("First name is required.", text1, "Fail")
        self.assertEqual("Last name is required.", text2, "Fail")
        self.assertEqual("Email is required.", text3, "Fail")
        self.assertEqual("Passwords must have at least 8 characters with one lowercase, uppercase, number, and special character.", text4, "Fail")
        self.assertEqual("Should accept terms and condtions.", text5, "Fail")

        driver.close()

    def test3(self):
        driver = master()

        driver.find_element_by_link_text("Signup").click()

        driver.implicitly_wait(4)

        driver.find_element(By.XPATH, "(//button[@type='button'])[1]").click()

        driver.find_element(By.XPATH, "//input[@placeholder='Enter your First Name']").send_keys("nabayubak")
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your Last Name']").send_keys("rajbahak")
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("asrlenovo1@yopmail.com")
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("Test@1234")

        driver.find_element(By.XPATH, "//input[@type='checkbox']").click()

        driver.find_element(By.XPATH, "//button[@variant='primary']").click()

        time.sleep(2)
        text1 = driver.find_element(By.XPATH, "//div[contains(text(),'Email already registered')]").text

        self.assertEqual("Email already registered", text1 , "Fail")

        driver.close()

    def test4(self):
        driver = master()

        driver.find_element_by_link_text("Signup").click()

        driver.implicitly_wait(4)

        driver.find_element(By.XPATH, "//input[@placeholder='Enter your First Name']").send_keys("nabayubak")
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your Last Name']").send_keys("rajbahak")
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("asrlenovo1565@yopmail.com")
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("Tesdfdfefef2sdf")

        time.sleep(2)

        text4 = driver.find_element(By.XPATH, "//div[contains(text(),'Passwords must have at least 8 characters with one lowercase, uppercase, number, and special character.')]").text
        self.assertEqual( "Passwords must have at least 8 characters with one lowercase, uppercase, number, and special character.", text4, "Fail")
        driver.close()

    def test5(self):
        driver = master()

        driver.find_element_by_link_text("Signup").click()

        time.sleep(3)

        driver.find_element(By.XPATH,"//b[contains(text(),'Login')]").click()

        time.sleep(2)
        Url = driver.current_url

        self.assertEqual("https://staging-cassette.audiobee.ai/", Url ,"Fail")

        driver.close()

if __name__=="__main__":
    unittest.main()