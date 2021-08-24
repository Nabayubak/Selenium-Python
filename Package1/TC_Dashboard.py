import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

def master():
# Mic allow validation
  opt = Options()
  opt.add_argument("--disable-infobars")
  opt.add_argument("start-maximized")
  opt.add_argument("--disable-extensions")

  # Pass the argument 1 to allow and 2 to block

  opt.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 1})

  driver = webdriver.Chrome(options=opt,
                            executable_path="C:\\Users\\nabay\\Downloads\\chromedriver_win32\\chromedriver.exe")

  driver.get("https://staging-cassette.audiobee.ai/login")
  driver.maximize_window()

  driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("asrlenovo2@yopmail.com")
  driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("Test@123")
  driver.find_element(By.XPATH, "//input[@id='loginForm_rememberMe']").click()

  driver.find_element(By.XPATH, "//button[@variant='primary']").click()
  time.sleep(5)

  return driver



class RecordingTest_p(unittest.TestCase):

    def test1(self):
      driver = master()
      Url = driver.current_url

      self.assertEqual("https://staging-cassette.audiobee.ai/dashboard", Url, "Fail")

      driver.close()

    def test2(self):
      driver = master()

      driver.implicitly_wait(2)

      driver.find_element(By.XPATH, "(//button[@id='btnTogglePlay'])[1]").click()
      time.sleep(4)

      driver.find_element(By.XPATH, "(//button[@id='btnTogglePlay'])[1]").click()
      time.sleep(2)

      driver.close()

    def test3(self):
      driver = master()

      # tooltip action edit and enter icon
      toolTip1 = driver.find_element(By.XPATH, "(//button[@type='button'])[7]")
      ActionChains(driver).move_to_element(toolTip1).perform()
      time.sleep(2)

      tooltipText1 = driver.find_element(By.XPATH, "//div[@class='ant-tooltip-inner']").text
      print(tooltipText1)

      self.assertEqual("Edit Recording Name", tooltipText1, "Fail")

      # enter tooltip
      driver.find_element(By.XPATH, "(//button[@type='button'])[7]").click()
      time.sleep(2)

      toolTip2 = driver.find_element(By.XPATH, "//span[@class='ant-input-suffix']")
      ActionChains(driver).move_to_element(toolTip2).perform()
      time.sleep(0.5)

      tooltipText2 = driver.find_element(By.XPATH, "//div[@class='ant-tooltip-inner']").text
      print(tooltipText2)

      self.assertEqual("Press enter to save", tooltipText2, "Fail")

      # clearing textarea field
      driver.find_element(By.XPATH, "//input[@type='text']").send_keys(Keys.CONTROL, 'a')
      driver.find_element(By.XPATH, "//input[@type='text']").send_keys(Keys.BACKSPACE)
      #
      time.sleep(0.40)
      driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Testsucess")
      time.sleep(2)

      driver.close()

    def test4(self):
      driver = master()

      driver.find_element(By.XPATH, "(//button[@id='btnDelete'])[3]").click()
      time.sleep(3)

      driver.find_element(By.XPATH, "//input[@placeholder = 'Type here']").send_keys("CONFIRM")

      time.sleep(2)
      Ele = driver.find_element(By.XPATH, "//span[contains(text(),'Delete')]")
      Result = Ele.is_enabled()
      self.assertEqual(True, Result, "Fail")
      Ele.click()



if __name__ == "__main__":
          unittest.main()