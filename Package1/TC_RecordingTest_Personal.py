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
      # Mic allow validation
      opt = Options()
      opt.add_argument("--disable-infobars")
      opt.add_argument("start-maximized")
      opt.add_argument("--disable-extensions")

      # Pass the argument 1 to allow and 2 to block

      opt.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 2})

      driver = webdriver.Chrome(options=opt,
                                executable_path="C:\\Users\\nabay\\Downloads\\chromedriver_win32\\chromedriver.exe")

      driver.get("https://staging-cassette.audiobee.ai/login")
      driver.maximize_window()

      driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("asrlenovo1@yopmail.com")
      driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("Test@1234")

      driver.find_element(By.XPATH, "//button[@variant='primary']").click()
      time.sleep(5)

      driver.find_element(By.ID, "btnRecordNewAudio").click()
      time.sleep(5)

      driver.implicitly_wait(5)

      text1 = driver.find_element(By.XPATH, "//div[contains(text(),'You have blocked the microphone access. Please allow it to record audio.')]").text

      self.assertEqual("You have blocked the microphone access. Please allow it to record audio.", text1, "Fail")



      driver.close()

    def test2(self):
      driver = master()

      driver.implicitly_wait(5)

      driver.find_element(By.ID, "btnRecordNewAudio").click()
      time.sleep(2)

      # tooltip action edit and enter icon
      toolTip1 = driver.find_element(By.XPATH, "//button[@type='button']")
      ActionChains(driver).move_to_element(toolTip1).perform()
      time.sleep(2)

      tooltipText1 = driver.find_element(By.XPATH, "//div[@class='ant-tooltip-inner']").text
      print(tooltipText1)

      self.assertEqual("Edit Recording Name", tooltipText1, "Fail")

      # enter tooltip
      driver.find_element(By.XPATH, "//button[@type='button']").click()
      time.sleep(2)

      toolTip2 = driver.find_element(By.XPATH, "//span[@class='ant-input-suffix']")
      ActionChains(driver).move_to_element(toolTip2).perform()
      time.sleep(0.5)

      tooltipText2 = driver.find_element(By.XPATH, "//div[@class='ant-tooltip-inner']").text
      print(tooltipText2)

      self.assertEqual("Press enter to save", tooltipText2, "Fail")

#clearing textarea field
      driver.find_element(By.XPATH, "//input[@type='text']").send_keys(Keys.CONTROL, 'a')
      driver.find_element(By.XPATH, "//input[@type='text']").send_keys(Keys.BACKSPACE)
#
      time.sleep(0.40)
      driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Testsucess")
      time.sleep(2)

#for starting recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(12)

      count = 1
      while (count <= 5):
        count = count + 1

        # for pausing recording
        driver.find_element(By.ID, "micBtn").click()
        time.sleep(5)

        driver.implicitly_wait(5)
        # for starting recording
        driver.find_element(By.XPATH, "//button[@variant='success']").click()
        driver.find_element(By.ID, "micBtn").click()
        time.sleep(5)

        if (count == 2):
          count = count +1

          # for pausing recording
          driver.find_element(By.ID, "micBtn").click()
          time.sleep(5)

          # clicking retry button
          driver.find_element(By.XPATH, "(//button[@variant = 'danger'])[1]").click()
          time.sleep(2)

          # clicking undoretry button
          driver.find_element(By.XPATH, "(//button[@variant='danger'])[1]").click()
          time.sleep(2)

          # start playing and redo from icon
          driver.find_element(By.ID, "play2").click()
          time.sleep(3)

          driver.find_element(By.ID, "puase2").click()
          time.sleep(3)

          driver.find_element(By.ID, "redo2").click()
          time.sleep(4)

          driver.find_element(By.XPATH, "(//button[@variant='danger'])[1]").click()
          time.sleep(2)

        # close playing and redo from icon

          # start playing and redo from icon / record
          driver.find_element(By.ID, "play1").click()
          time.sleep(7)

          driver.find_element(By.ID, "puase1").click()
          time.sleep(3)
          #
          driver.find_element(By.ID, "redo1").click()
          time.sleep(2)

          driver.find_element(By.ID, "micBtn").click()
          time.sleep(2)

          driver.find_element(By.ID, "micBtn").click()
          time.sleep(2)
          # close playing and redo from icon

          driver.find_element(By.ID, "micBtn").click()
          time.sleep(8)

        if (count == 5):
          count = count + 1

          # for pausing recording
          driver.find_element(By.ID, "micBtn").click()
          time.sleep(5)

          driver.find_element(By.XPATH,"(//button[@type='button'])[3]").click()
          time.sleep(4)

          driver.find_element(By.XPATH, "(//button[@type='button'])[3]").click()
          time.sleep(4)

    #Deleting action
          driver.find_element(By.XPATH,"(//button[@type='button'])[13]").click()
          time.sleep(5)

          driver.find_element(By.XPATH,"//span[contains(text(),'Confirm')]").click()
          time.sleep(2)



    # complete recording
          driver.find_element(By.XPATH, "(//button[@variant='primary'])[2]").click()
          time.sleep(10)

    #Publishing
          driver.find_element(By.XPATH, "//button[@variant='primary']").click()
          time.sleep(2)

          Url = driver.current_url

          self.assertEqual("https://staging-cassette.audiobee.ai/dashboard", Url, "Fail")


          text = driver.find_element(By.XPATH, "//div[@class='ant-notification-notice-message']").text

          self.assertEqual("Published", text, "Fail")

      driver.close()

    def test3(self):

      driver = master()

      driver.implicitly_wait(6)

      driver.find_element(By.ID, "btnRecordNewAudio").click()
      time.sleep(3)


      # for starting recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)

      count = 1
      while (count <= 100):
          count = count + 1

          # for pausing recording
          driver.find_element(By.ID, "micBtn").click()
          time.sleep(1)

          driver.implicitly_wait(5)
          # for starting recording
          driver.find_element(By.XPATH, "//button[@variant='success']").click()
          driver.find_element(By.ID, "micBtn").click()
          time.sleep(1)

          if (count == 100):
            count = count + 1
            # for pausing recording
            driver.find_element(By.ID, "micBtn").click()
            time.sleep(1)

            # complete recording / save as draft
            driver.find_element(By.XPATH, "(//button[@variant='primary'])[2]").click()
            time.sleep(5)

            # Publishing
            driver.find_element(By.XPATH, "//button[@variant='primary']").click()
            time.sleep(2)

            Url = driver.current_url
            print (Url)
            self.assertEqual("https://staging-cassette.audiobee.ai/dashboard", Url, "Fail")
            text = driver.find_element(By.XPATH, "//div[@class='ant-notification-notice-message']").text
            print (text)
            self.assertEqual("Published",text, "Fail")

            driver.close()

    def test4(self):

      driver = master()

      driver.implicitly_wait(6)

      driver.find_element(By.ID, "btnRecordNewAudio").click()
      time.sleep(9)

      # for starting recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(4)

      count = 1
      while (count <= 5):
        count = count + 1

        # for pausing recording
        driver.find_element(By.ID, "micBtn").click()
        time.sleep(1)

        driver.implicitly_wait(5)
        # for starting recording
        driver.find_element(By.XPATH, "//button[@variant='success']").click()
        driver.find_element(By.ID, "micBtn").click()
        time.sleep(1)

        if (count == 5):
          count = count + 1
          # for pausing recording
          driver.find_element(By.ID, "micBtn").click()
          time.sleep(1)




          # complete recording
          driver.find_element(By.XPATH, "(//button[@variant='primary'])[2]").click()
          time.sleep(5)

          driver.find_element(By.XPATH, "//span[contains(text(),'Delete all segments')]").click()
          time.sleep(3)

          driver.find_element(By.XPATH, "//input[@placeholder = 'Type here']").send_keys("sdfsadfasdf")
          Ele = driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-dangerous']")
          Result = Ele.is_enabled()

          print(Result)

          self.assertEqual(False, Result, "Fail")

          driver.find_element(By.XPATH, "//span[contains(text(),'Cancel')]").click()
          time.sleep(2)

          driver.find_element(By.XPATH, "//span[contains(text(),'Delete all segments')]").click()
          time.sleep(3)

          driver.find_element(By.XPATH, "//span[@role='img']").click()
          time.sleep(2)

          driver.find_element(By.XPATH, "//span[contains(text(),'Delete all segments')]").click()
          time.sleep(3)

          driver.find_element(By.XPATH, "//input[@placeholder = 'Type here']").send_keys("CONFIRM")

          Ele = driver.find_element(By.XPATH, "(//span[contains(text(),'Delete')])[2]")
          Result = Ele.is_enabled()
          self.assertEqual(True, Result, "Fail")
          Ele.click()

          sucessmsg = driver.find_element(By.XPATH,"//span[contains(text(),'All segments deleted successfully.')]").text
          self.assertEqual("All segments deleted successfully.", sucessmsg, "Fail")
          time.sleep(2)

          driver.close()



if __name__ == "__main__":
      unittest.main()