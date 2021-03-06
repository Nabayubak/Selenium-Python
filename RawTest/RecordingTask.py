import unittest
import time



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains



class RecordingTask(unittest.TestCase):

    # def setUp(self):
    #   # Mic allow validation
    #   opt = Options()
    #   opt.add_argument("--disable-infobars")
    #   opt.add_argument("start-maximized")
    #   opt.add_argument("--disable-extensions")
    #
    #   # Pass the argument 1 to allow and 2 to block
    #
    #   opt.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 2})
    #
    #   driver = webdriver.Chrome(options=opt,
    #                             executable_path="C:\\Users\\nabay\\Downloads\\chromedriver_win32\\chromedriver.exe")
    #
    #   driver.get("https://staging-cassette.audiobee.ai/")
    #   driver.maximize_window()
    #
    #   driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("asrlenovo1@yopmail.com")
    #   driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("Test@1234")
    #   # driver.find_element(By.XPATH, "//input[@id='loginForm_rememberMe']").click()
    #
    #   driver.find_element(By.XPATH, "//button[@variant='primary']").click()


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

      driver.get("https://staging-cassette.audiobee.ai/")
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

      driver.refresh()

      micdisable = driver.find_element(By.XPATH, "//img[@class='ant-scroll-number-custom-component']").get_attribute("src")
      print(micdisable)

#Veriying mic allow and block icon
      self.assertEqual("https://staging-cassette.audiobee.ai/static/media/error-status.12f0a1b1.svg",micdisable,"Fail")
      time.sleep(3)

      driver.close()



    def test2(self):
      # mic allow
      opt = Options()
      opt.add_argument("--disable-infobars")
      opt.add_argument("start-maximized")
      opt.add_argument("--disable-extensions")

      # Pass the argument 1 to allow and 2 to block

      opt.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 1})

      driver = webdriver.Chrome(options=opt, executable_path="C:\\Users\\nabay\\Downloads\\chromedriver_win32\\chromedriver.exe")

      driver.get("https://staging-cassette.audiobee.ai/")
      driver.maximize_window()

      driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("asrlenovo1@yopmail.com")
      driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("Test@1234")
      driver.find_element(By.XPATH, "//input[@id='loginForm_rememberMe']").click()

      driver.find_element(By.XPATH, "//button[@variant='primary']").click()
      time.sleep(5)

      driver.implicitly_wait(5)

      driver.find_element(By.XPATH,"//img[@alt='Record audio']").click()
      time.sleep(2)

      micenable = driver.find_element(By.XPATH, "//img[@class='ant-scroll-number-custom-component']").get_attribute("src")

      print(micenable)

      self.assertEqual("https://staging-cassette.audiobee.ai/static/media/success-status.2c0e2132.svg", micenable,"Fail")

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
      time.sleep(10)

#for pausing recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(5)

#start playing and redo from icon
      driver.find_element(By.ID, "play1").click()
      time.sleep(12)


      driver.find_element(By.ID,"redo1").click()
      time.sleep(4)

      driver.find_element(By.ID, "micBtn").click()
      time.sleep(8)

      driver.find_element(By.ID, "micBtn").click()
      time.sleep(5)
#close playing and redo from icon

#playing recorded audio clicking play button
      driver.find_element(By.XPATH,"//button[@variant='success']").click()
      time.sleep(11)


# playing recorded audio clicking play button2nd time
      driver.find_element(By.XPATH, "//button[@variant='success']").click()
      time.sleep(3)

#pausing played recording
      driver.find_element(By.XPATH, "//button[@variant='success']").click()
      time.sleep(3)

#recording another
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(8)

#stopping recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(2)



#retry recording
      driver.find_element(By.XPATH, "//button[@variant='danger']").click()
      time.sleep(2)

#start recording again
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(15)

#stop recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(2)



#complete recording
      driver.find_element(By.XPATH, "//button[@variant='primary']").click()
      time.sleep(2)
#
      # start playing and redo from icon
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

#start recording again
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(6)

# stop recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(10)

      # start playing and redo from icon
      driver.find_element(By.ID, "play2").click()
      time.sleep(6)

      driver.find_element(By.ID, "puase2").click()
      time.sleep(2)

      driver.find_element(By.ID, "redo1").click()
      time.sleep(2)

      driver.find_element(By.ID, "micBtn").click()
      time.sleep(10)

      driver.find_element(By.ID, "micBtn").click()
      time.sleep(2)
      # close playing and redo from icon

#Deleting action
      driver.find_element(By.XPATH,"(//button[@type='button'])[13]").click()
      time.sleep(4)

      driver.find_element(By.XPATH,"//span[contains(text(),'Confirm')]").click()
      time.sleep(2)



# complete recording
      driver.find_element(By.XPATH, "//button[@variant='primary']").click()
      time.sleep(10)

#Publishing
      driver.find_element(By.XPATH, "//button[@variant='primary']").click()
      time.sleep(10)

      Url = driver.current_url

      self.assertEqual("https://staging-cassette.audiobee.ai/dashboard", Url, "Fail")

      text = driver.find_element(By.XPATH, "//div[contains(text(),'Published')]").text

      self.assertEqual("Published", text, "Fail")

      driver.close()



    def test3(self):
      # mic allow
      opt = Options()
      opt.add_argument("--disable-infobars")
      opt.add_argument("start-maximized")
      opt.add_argument("--disable-extensions")

      # Pass the argument 1 to allow and 2 to block

      opt.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 1})

      driver = webdriver.Chrome(options=opt,
                                executable_path="C:\\Users\\nabay\\Downloads\\chromedriver_win32\\chromedriver.exe")

      driver.get("https://staging-cassette.audiobee.ai/")
      driver.maximize_window()

      driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("asrlenovo1@yopmail.com")
      driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("Test@1234")
      driver.find_element(By.XPATH, "//input[@id='loginForm_rememberMe']").click()

      driver.find_element(By.XPATH, "//button[@variant='primary']").click()
      time.sleep(5)

      driver.implicitly_wait(6)

      driver.find_element(By.XPATH, "//img[@alt='Record audio']").click()
      time.sleep(2)



      # for starting recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)

      # for pausing recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)
      # for starting recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)

      # for pausing recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)

      # for starting recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)

      # for pausing recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)

      # for starting recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)

      # for pausing recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)

      # for starting recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)

      # for pausing recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)
      # for starting recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)

      # for pausing recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)
      # for starting recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)

      # for pausing recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)
      # for starting recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)

      # for pausing recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)
      # for starting recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)

      # for pausing recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)
      # for starting recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)

      # for pausing recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)
      # for starting recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)

      # for pausing recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)
      # for starting recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)

      # for pausing recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)
      # for starting recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)

      # for pausing recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)
      # for starting recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)

      # for pausing recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)
      # for starting recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)

      # for pausing recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)
      # for starting recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)

      # for pausing recording
      driver.find_element(By.ID, "micBtn").click()
      time.sleep(1)

      # complete recording
      driver.find_element(By.XPATH, "//button[@variant='primary']").click()
      time.sleep(5)

      # Publishing
      driver.find_element(By.XPATH, "//button[@variant='primary']").click()
      time.sleep(5)

      Url = driver.current_url

      self.assertEqual("https://staging-cassette.audiobee.ai/dashboard", Url, "Fail")

      text = driver.find_element(By.XPATH, "//div[contains(text(),'Published')]").text

      self.assertEqual("Published",text, "Fail")

      driver.close()



if __name__ == "__main__":
      unittest.main()