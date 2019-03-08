from selenium import webdriver
import selenium

USER = "YourID"
PASS = "YourPassword"

def intoStudyroom():
    browser.execute_script("goStudy()")

options = webdriver.ChromeOptions()

browser = webdriver.Chrome('/Users/hyojun/Downloads/chromedriver', chrome_options=options)

url_login = "http://www.ebslang.co.kr/main.ebs"
browser.get(url_login)
#browser.implicitly_wait(1)
e = browser.find_element_by_id("mainUserId")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("mainUserPw")
e.clear()
e.send_keys(PASS)

browser.execute_script("fnMainLogin();")
while True:
    if browser.execute_script("return document.readyState") == "complete":
        browser.implicitly_wait(4)
        intoStudyroom()
        break
