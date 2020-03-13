
import time
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import keyboard
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# driver = webdriver.Chrome(chrome_options=options ,executable_path=r'D:\Python\chromedriver.exe')
SEID='(628)089-7272'
fp = webdriver.FirefoxProfile(profile_directory="C:\\Users\\veeresh.m\\AppData\\Roaming\\Mozilla\\Firefox\Profiles\\rted5jtu.Test_Py")
fp.set_preference("webdriver_assume_untrusted_issuer", False)
fp.set_preference("webdriver_accept_untrusted_certs", True)
fp.accept_untrusted_certs = True
fp.update_preferences()
driver = webdriver.Firefox(firefox_profile=fp, executable_path='D:\Python\geckodriver.exe')
# driver = webdriver.Firefox(executable_path='D:\Python\geckodriver.exe')
# driver = webdriver.Firefox(firefox_profile=profile ,executable_path='D:\Python\geckodriver.exe')

# capabilities = webdriver.DesiredCapabilities().INTERNETEXPLORER
# capabilities['acceptInsecureCerts'] = True
# driver = webdriver.Ie(executable_path=r'D:\Python\IEDriverServer.exe', capabilities=capabilities)

# capabilities = webdriver.DesiredCapabilities().FIREFOX
# capabilities['acceptInsecureCerts'] = True
# driver = webdriver.Firefox(executable_path='D:\Python\Driveres\geckodriver.exe' , capabilities=desired_capabilities)
#

# driver = webdriver.Ie(executable_path=r'D:\Python\IEDriverServer.exe')
# driver = webdriver.Chrome(executable_path=r'D:\Python\chromedriver.exe')
# driver.get("https://10.133.91.85:4511/slamon/home.jsf")

time.sleep(10)

driver.get("https://ui-svha.gl.avaya.com/salui")
driver.maximize_window()
driver.find_element_by_id("homeForm:autoCompleteSEID").send_keys(SEID)
time.sleep(10)
driver.find_element_by_id("homeForm:go").click()
time.sleep(10)
# window_before = driver.window_handles[0]
# print(window_before)
# driver.switch_to.window("4")
# time.sleep(10)
driver.find_element_by_id("detailsDialogform:connectiontypes:1:j_idt163").click()
time.sleep(10)
driver.find_element_by_id("dialogform:submitBtn").click()
# time.sleep(10)
# window_before = driver.window_handles[0]
# print(window_before)
# driver.switch_to.window("4")
time.sleep(20)

keyboard.press_and_release('tab')
time.sleep(3)
keyboard.press_and_release('tab')
time.sleep(3)
keyboard.press_and_release('enter')
time.sleep(3)
import os
import subprocess
os.startfile(f"C:/Users/veeresh.m/Downloads/SALNxG-{SEID}.jnlp")
time.sleep(30)
keyboard.press_and_release('enter')
time.sleep(3)
keyboard.press_and_release('enter')
time.sleep(5)
pid = subprocess.Popen("C:/Program Files/PuTTY/putty.exe root@localhost -pw cms09").pid




# alert=driver.switch_to.alert
# alert.accept()

# driver.implicitly_wait(3800)
# driver.maximize_window()


#SALMON SCrip
# driver.find_element_by_id("j_username").send_keys("root")
# driver.find_element_by_id("j_password").send_keys("Avaya123$")
# driver.find_element_by_name("submit").click()
# driver.find_element_by_name("noticeForm:continueBtn").click()
# Titile=driver.title
# assert Titile=='SLA Monitor'
