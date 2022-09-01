
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver.v2 as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import socket   





if __name__ == '__main__':

    EMAIL = 'indu.uday1993@gmail.com'
    PASSWORD = "Uday@1234"
    SECURITY_QUESTION = 'Kutta'
    PATH = "/Users/saintmantis/Downloads/chromedriver"
    PROXY = '129.226.22.191:80'


    options = Options()
    user_agent = 'Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",

}

    webdriver.DesiredCapabilities.CHROME['acceptSslCerts']=True
    options.add_argument("user-agent="+user_agent)
    options.add_argument('--user-data-dir=/Users/saintmantis/Library/Application Support/Google/Chrome/Profile 1')
    options.add_argument('--proxy-server=%s' % PROXY)
    driver =webdriver.Chrome(PATH,options=options)
    driver.get("https://www.upwork.com/nx/find-work/")
    #driver.get("https://ifconfig.me/")
    time.sleep(4)
    driver.find_element(By.CLASS_NAME, "up-input").send_keys(EMAIL)
    print("Email entered")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,'#login_password_continue').click()
    print('continue btn clicked')
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#login_password").send_keys(PASSWORD)
    print("Password entered")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#login_control_continue").click()
    print("Continue btn clicked 2")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#login_answer").send_keys(SECURITY_QUESTION)
    print("Security question answered")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#login_control_continue").click()
    time.sleep(10)
    driver.quit()
