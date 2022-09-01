
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver.v2 as uc
from selenium.common.exceptions import NoSuchElementException


if __name__ == '__main__': 

    EMAIL = 'indu.uday1993@gmail.com'
    PASSWORD = "Uday@1234"
    SECURITY_QUESTION = 'Kutta'
    PATH = "/Users/saintmantis/Downloads/chromedriver"
    PROXY_SERVER = '14.140.131.82'


    options = uc.ChromeOptions()
    driver = uc.Chrome(executable_path=PATH, options=options) 
    driver.get("https://www.upwork.com/nx/find-work/")
    time.sleep(3)
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



    maindiv = driver.find_element(By.CSS_SELECTOR, "div[data-test='job-tile-list']")
    print("maindiv triggered")
    jobs = maindiv.find_elements(By.CSS_SELECTOR, "section.up-card-section.up-card-list-section.up-card-hover")
    
    expertise_level_num = 1
    description_num = 5
    posted_time_num = 1

    for job in jobs:
        
        try:
            #job_title = job.find_element(By.CSS_SELECTOR, "div.row.my-10 > div.col > h4")
            job_title = job.find_element(By.CSS_SELECTOR, "section h4[class='my-0 p-sm-right job-tile-title']")
            print(job_title.text)
        except NoSuchElementException:
            pass
        
        try:
            #rate = job.find_element(By.CSS_SELECTOR, "div.mb-10 > div:nth-child(1) > small > strong")
            rate = job.find_element(By.CSS_SELECTOR, "section div strong[data-test='job-type']")
            print(rate.text)
        except NoSuchElementException:
            pass
    
        try:
            #expertise_level = job.find_element(By.CSS_SELECTOR, "div.mb-10 > div:nth-child(1) > small > span:nth-child(2) > span")
            expertise_level = job.find_element(By.CSS_SELECTOR, f"body > div:nth-child(3) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > section:nth-child({expertise_level_num}) > div:nth-child(2) > div:nth-child(1) > small:nth-child(1) > span:nth-child(2) > span:nth-child(1)")
            print(expertise_level.text)
        except NoSuchElementException:
            pass


        try:
            time = job.find_element(By.CSS_SELECTOR, f"body > div:nth-child(3) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > section:nth-child({expertise_level_num}) > div:nth-child(2) > div:nth-child(1) > small:nth-child(1) > span:nth-child(3) > span:nth-child(1) > span:nth-child(2)")
            print(time.text)
        except NoSuchElementException:
            pass

        try:
           
            posted_time = job.find_element(By.CSS_SELECTOR, "div.mb-10 > div:nth-child(1) > small > span:nth-child(4) > span")
            print(posted_time.text)
        except NoSuchElementException:
            pass

        try:
            description = job.find_element(By.CLASS_NAME, f"up-line-clamp-v2.clamped")
            #description = job.find_element(By.CSS_SELECTOR, f"#up-line-clamp-v2-{description_num} > span")
            print(description.text)
        except NoSuchElementException:
            pass

        try:
            skills = job.find_element(By.CSS_SELECTOR, "section div[class='up-skill-wrapper']")
            print(skills.text)
        except NoSuchElementException:
            pass

        try:
            payment = job.find_element(By.CSS_SELECTOR, "div.mb-10 > div.badge-line.mt-10 > small.d-inline-flex > strong")
            print(payment.text)
        except NoSuchElementException:
            pass

        try:
            stars = job.find_element(By.CSS_SELECTOR, "div.mb-10 > div.badge-line.mt-10 > span.d-none.d-md-inline-block.mb-0.vertical-align-top")
            print(stars.text)
        except NoSuchElementException:
            pass

  
        try:
            spent_amount = job.find_element(By.CSS_SELECTOR, "div.mb-10 > div.badge-line.mt-10 > small.d-inline-block > strong")
            print(spent_amount.text)
        except NoSuchElementException:
            pass


        try:
            required_connection = job.find_element(By.CSS_SELECTOR, "div.mb-10 > div.badge-line.mt-10 > small.d-none.d-lg-inline-flex.d-md-inline-flex.text-muted > strong")
            print(required_connection.text)
        except NoSuchElementException:
            pass

        try:
            location = job.find_element(By.CLASS_NAME, "d-none.d-lg-inline-flex.text-muted")
            print(location.text)
        except NoSuchElementException:
            pass

        print("--------------------------------------------------------------------------------------------------------------------")


        expertise_level_num+=1
        description_num+=1
        posted_time_num+=1
print("--------------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------------")
        
