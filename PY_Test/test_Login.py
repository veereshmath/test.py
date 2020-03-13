from selenium import webdriver
import pytest

@pytest.fixture
def test_setup():
    global driver
    driver = webdriver.Firefox(executable_path='D:\Python\geckodriver.exe')
    yield
    driver.close()
    driver.quit()


def test_login(test_setup):
    #SALMON SCrip
    driver.get("https://10.133.91.85:4511/slamon/home.jsf")
    driver.find_element_by_id("j_username").send_keys("root")
    driver.find_element_by_id("j_password").send_keys("Avaya123$")
    driver.find_element_by_name("submit").click()
    driver.find_element_by_name("noticeForm:continueBtn").click()
    Titile=driver.title
    assert Titile=='SLA Monito'

# def test_teardown():
#     driver.close()
#     driver.quit()

