import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class RecordingTask(unittest.TestCase):

  def test2(self):
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

    driver.find_element(By.XPATH, "//input[@placeholder='Enter your email']").send_keys("asrlenovo2@yopmail.com")
    driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys("Test@123")
    driver.find_element(By.XPATH, "//input[@id='loginForm_rememberMe']").click()

    driver.find_element(By.XPATH, "//button[@variant='primary']").click()
    time.sleep(5)

    driver.implicitly_wait(6)

    driver.find_element(By.ID, "btnRecordNewAudio").click()
    time.sleep(3)

    # for starting recording
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)

    # for pausing recording
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)
    # for starting recording
    driver.find_element(By.XPATH, "//button[@variant='success']").click()
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)

    # for pausing recording
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)

    # for starting recording
    driver.find_element(By.XPATH, "//button[@variant='success']").click()
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)

    # for pausing recording
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)

    # for starting recording
    driver.find_element(By.XPATH, "//button[@variant='success']").click()
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)

    # for pausing recording
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)

    # for starting recording
    driver.find_element(By.XPATH, "//button[@variant='success']").click()
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)

    # for pausing recording
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)
    # for starting recording
    driver.find_element(By.XPATH, "//button[@variant='success']").click()
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)

    # for pausing recording
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)
    # for starting recording
    driver.find_element(By.XPATH, "//button[@variant='success']").click()
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)

    # for pausing recording
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)
    # for starting recording
    driver.find_element(By.XPATH, "//button[@variant='success']").click()
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)

    # for pausing recording
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)
    # for starting recording
    driver.find_element(By.XPATH, "//button[@variant='success']").click()
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)

    # for pausing recording
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)
    # for starting recording
    driver.find_element(By.XPATH, "//button[@variant='success']").click()
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)

    # for pausing recording
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)
    # for starting recording
    driver.find_element(By.XPATH, "//button[@variant='success']").click()
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)

    # for pausing recording
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)
    # for starting recording
    driver.find_element(By.XPATH, "//button[@variant='success']").click()
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)

    # for pausing recording
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)
    # for starting recording
    driver.find_element(By.XPATH, "//button[@variant='success']").click()
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)

    # for pausing recording
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)
    # for starting recording
    driver.find_element(By.XPATH, "//button[@variant='success']").click()
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)

    # for pausing recording
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)
    # for starting recording
    driver.find_element(By.XPATH, "//button[@variant='success']").click()
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)

    # for pausing recording
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)
    # for starting recording
    driver.find_element(By.XPATH, "//button[@variant='success']").click()
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)

    # for pausing recording
    driver.find_element(By.ID, "micBtn").click()
    time.sleep(1)

    # complete recording
    driver.find_element(By.XPATH, "(//button[@variant='primary'])[2]").click()
    time.sleep(5)

    # Publishing
    driver.find_element(By.XPATH, "//button[@variant='primary']").click()
    time.sleep(5)

    Url = driver.current_url
    print(Url)
    self.assertEqual("https://staging-cassette.audiobee.ai/dashboard", Url, "Fail")

    # text = driver.find_element(By.XPATH, "//div[contains(text(),'Published')]").text
    # print(text)
    # self.assertEqual("Published", text, "Fail")

    driver.close()

if __name__ == "__main__":
      unittest.main()