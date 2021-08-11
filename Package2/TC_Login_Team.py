import xlutils
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginTest_T(unittest.TestCase):


#Blank field
    def test1(self):

        driver = webdriver.Chrome("C:\\Users\\nabay\\Downloads\\chromedriver_win32\\chromedriver.exe")

        driver.get("https://staging-cassette.audiobee.ai/")
        driver.maximize_window()

        driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("")
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("")
        driver.find_element(By.XPATH, "//input[@id='loginForm_rememberMe']")

        driver.find_element(By.XPATH, "//button[@variant='primary']").click()

        time.sleep(5)

        Text1 = driver.find_element(By.XPATH, "//div[contains(text(),'Email is required')]").text
        Text2 = driver.find_element(By.XPATH, "//div[contains(text(),'Password is required.')]").text


        self.assertEqual("Email is required.", Text1, "Fail")
        self.assertEqual("Password is required.",Text2, "Fail")

        driver.close()


#unregistered mail and invalid email
    def test2(self):
        driver = webdriver.Chrome("C:\\Users\\nabay\\Downloads\\chromedriver_win32\\chromedriver.exe")

        driver.get("https://staging-cassette.audiobee.ai/")
        driver.maximize_window()

        driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("Nabayubak@gmail.com")
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("Test@123")
        driver.find_element(By.XPATH, "//input[@id='loginForm_rememberMe']").click()

        driver.find_element(By.XPATH, "//button[@variant='primary']").click()

        time.sleep(5)

        text1= driver.find_element(By.XPATH, "//div[contains(text(),'Invalid Email or Password!')]").text


        self.assertEqual("Invalid Email or Password!", text1, "Fail")

        driver.refresh()

        driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("Naasdfasdfasdf")
        driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("Test@123")
        driver.find_element(By.XPATH, "//input[@id='loginForm_rememberMe']").click()

        driver.find_element(By.XPATH, "//button[@variant='primary']").click()

        time.sleep(5)

        text2= driver.find_element(By.XPATH, "//div[contains(text(),'Please enter a valid email address.')]").text


        self.assertEqual("Please enter a valid email address.", text2, "Fail")

        driver.close()

#Forgot password
    def test3(self):
        driver = webdriver.Chrome("C:\\Users\\nabay\\Downloads\\chromedriver_win32\\chromedriver.exe")

        driver.get("https://staging-cassette.audiobee.ai/")
        driver.maximize_window()

        driver.find_element(By.XPATH, "//a[contains(text(),'Forgot Password?')]").click()

        time.sleep(2)

        if driver.current_url == "https://staging-cassette.audiobee.ai/forgot-password":
            print("Pass")

            # Blank field
            time.sleep(4)

            driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("")
            driver.find_element(By.XPATH, "//button[@variant ='primary']").click()

            time.sleep(1)

            text1 = driver.find_element(By.XPATH, "//div[contains(text(),'Email is required.')]").text

            self.assertEqual("Email is required.", text1, "Fail")

            driver.refresh()

            # entered invalid mail
            driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("Naasdfasdfasdf")
            driver.find_element(By.XPATH, "//button[@variant ='primary']").click()

            time.sleep(1)

            text2 = driver.find_element(By.XPATH, "//div[contains(text(),'Please enter a valid email address.')]").text

            self.assertEqual("Please enter a valid email address.", text2, "Fail")

            driver.refresh()

            # Unregister email

            driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("Nabayubak@gmail.com")
            driver.find_element(By.XPATH, "//button[@variant ='primary']").click()

            time.sleep(1)
            text3 = driver.find_element(By.XPATH, "//div[contains(text(),'User with email:')]").text

            self.assertEqual("User with email: Nabayubak@gmail.com not found.", text3, "Fail")

            driver.refresh()

            # Valid email and register email

            driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys(
                "asrlenovo1@yopmail.com")
            driver.find_element(By.XPATH, "//button[@variant ='primary']").click()

            time.sleep(1)
            text4 = driver.find_element(By.XPATH, "//div[contains(text(),'Reset password link has been sent')]").text

            self.assertEqual(
                "Reset password link has been sent to your email. Please check it and reset your password.", text4,
                "Fail")

            time.sleep(0.7)

            # onclick login link
            driver.find_element(By.XPATH, "//b[contains(text(),'Login')]").click()

            time.sleep(2)
            Url = driver.current_url
            self.assertEqual("https://staging-cassette.audiobee.ai/", Url, "Fail")

            driver.close()

        else:
            print("Fail")

            driver.close()

# onclick signup link
    def test4(self):
        driver = webdriver.Chrome("C:\\Users\\nabay\\Downloads\\chromedriver_win32\\chromedriver.exe")

        driver.get("https://staging-cassette.audiobee.ai/")

        time.sleep(2)

        driver.maximize_window()

        driver.find_element(By.XPATH,"//b[contains(text(),'Signup')]").click()

        time.sleep(2)

        Url = driver.current_url

        self.assertEqual("https://staging-cassette.audiobee.ai/sign-up", Url, "Fail")

        driver.close()


def test6(self):
  driver = webdriver.Chrome("C:\\Users\\nabay\\Downloads\\chromedriver_win32\\chromedriver.exe")

  driver.get("https://staging-cassette.audiobee.ai/")
  driver.maximize_window()

  # Finding element from login page and data entering to field

  driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("asrlenovo2@yopmail.com")
  driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("Test@123")
  driver.find_element(By.XPATH, "//input[@id='loginForm_rememberMe']").click()

  driver.find_element(By.XPATH, "//button[@variant='primary']").click()
  driver.close()

if __name__=="__main__":
    unittest.main()