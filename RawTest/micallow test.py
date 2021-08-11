from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
  })

driver = webdriver.Chrome(options= opt, executable_path="C:\\Users\\nabay\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get('https://mictests.com/')

time.sleep(10)
driver.find_element(By.ID,"mic-launcher").click()

