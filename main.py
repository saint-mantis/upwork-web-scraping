
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver.v2 as uc
from selenium.common.exceptions import NoSuchElementException
import pandas as pd



if __name__ == '__main__': 

    LINK = "https://www.upwork.com/nx/find-work/"
    PATH_TO_OUTPUT_CSV_FILE = 'sample_output.csv'
    EMAIL = 'indu.uday1993@gmail.com'
    PASSWORD = "Uday@1234"
    SECURITY_QUESTION = 'Kutta'
    PATH_TO_CHROMEDRIVER = "/Users/saintmantis/Documents/GitHub/upwork-web-scraping/chromedriver"
    PROXY_SERVER = '14.140.131.82'


    options = uc.ChromeOptions()
    driver = uc.Chrome(executable_path=PATH_TO_CHROMEDRIVER, options=options) 
    driver.get(LINK)
    time.sleep(5)
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
    time.sleep(2)



    maindiv = driver.find_element(By.CSS_SELECTOR, "div[data-test='job-tile-list']")
    jobs = maindiv.find_elements(By.CSS_SELECTOR, "section.up-card-section.up-card-list-section.up-card-hover")


    indexfnnum = 0
    expertise_level_num = 1
    description_num = 5
    posted_time_num = 1

    
    df3 = pd.DataFrame(columns = ["Project",'Rate','Expertise_Level','Time','Posted_time','Description','Skills','Payment','Stars','Spent_amount','Required_connection','Location'])
    
    for job in jobs:

        
        try:
            job_title = job.find_element(By.CSS_SELECTOR, "section h4[class='my-0 p-sm-right job-tile-title']")
            print(job_title.text)
            df3.loc[indexfnnum,'Project']= job_title.text
        except NoSuchElementException:
            df3.loc[indexfnnum,'Project']= "None"

            pass
        
        try:
            
            
            rate = job.find_element(By.CSS_SELECTOR, "section div strong[data-test='job-type']")
            print(rate.text)
            df3.loc[indexfnnum,'Rate']= rate.text
        except NoSuchElementException:
            df3.loc[indexfnnum,'Rate']= "None"
            pass
    
        try:
            
            
            expertise_level = job.find_element(By.CSS_SELECTOR, f"body > div:nth-child(3) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > section:nth-child({expertise_level_num}) > div:nth-child(2) > div:nth-child(1) > small:nth-child(1) > span:nth-child(2) > span:nth-child(1)")
            print(expertise_level.text)
            df3.loc[indexfnnum,'Expertise_Level']= expertise_level.text
        except NoSuchElementException:
            df3.loc[indexfnnum,'Expertise_Level']= "None"
            pass


        try:
            
            timee = job.find_element(By.CSS_SELECTOR, f"body > div:nth-child(3) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > section:nth-child({expertise_level_num}) > div:nth-child(2) > div:nth-child(1) > small:nth-child(1) > span:nth-child(3) > span:nth-child(1) > span:nth-child(2)")
            print(timee.text)
            df3.loc[indexfnnum,'Time']= timee.text
        except NoSuchElementException:
            df3.loc[indexfnnum,'Time']= "None"
            pass

        try:
            posted_time = job.find_element(By.CSS_SELECTOR, "div.mb-10 > div:nth-child(1) > small > span:nth-child(4) > span")
            print(posted_time.text)
            df3.loc[indexfnnum,'Posted_time']= posted_time.text
        except NoSuchElementException:
            df3.loc[indexfnnum,'Posted_time']= "None"
            pass

        try:
            
            description = job.find_element(By.CLASS_NAME, f"up-line-clamp-v2.clamped")
            print(description.text)
            df3.loc[indexfnnum,'Description']= description.text
        except NoSuchElementException:
            df3.loc[indexfnnum,'Description']= "None"
            pass

        try:
            skills = job.find_element(By.CSS_SELECTOR, "section div[class='up-skill-wrapper']")
            print(skills.text)
            df3.loc[indexfnnum,'Skills']= skills.text
        except NoSuchElementException:
            df3.loc[indexfnnum,'Skills']= "None"
            pass

        try:
            payment = job.find_element(By.CSS_SELECTOR, "div.mb-10 > div.badge-line.mt-10 > small.d-inline-flex > strong")
            print(payment.text)
            df3.loc[indexfnnum,'Payment']= payment.text

        except NoSuchElementException:
            df3.loc[indexfnnum,'Payment']= "None"
            pass

        try:
            stars = job.find_element(By.CSS_SELECTOR, "div.mb-10 > div.badge-line.mt-10 > span.d-none.d-md-inline-block.mb-0.vertical-align-top")
            print(stars.text)
            df3.loc[indexfnnum,'Stars']= stars.text
        except NoSuchElementException:
            df3.loc[indexfnnum,'Stars']= "None"
            pass

  
        try:
            spent_amount = job.find_element(By.CSS_SELECTOR, "div.mb-10 > div.badge-line.mt-10 > small.d-inline-block > strong")
            print(spent_amount.text)
            df3.loc[indexfnnum,'Spent_amount']= spent_amount.text
        except NoSuchElementException:
            df3.loc[indexfnnum,'Spent_amount']= "None"
            pass


        try:
            required_connection = job.find_element(By.CSS_SELECTOR, "div.mb-10 > div.badge-line.mt-10 > small.d-none.d-lg-inline-flex.d-md-inline-flex.text-muted > strong")
            print(required_connection.text)
            df3.loc[indexfnnum,'Required_connection']= required_connection.text
        except NoSuchElementException:
            df3.loc[indexfnnum,'Required_connection']= "None"
            pass

        try:
            location = job.find_element(By.CLASS_NAME, "d-none.d-lg-inline-flex.text-muted")
            print(location.text)
            df3.loc[indexfnnum,'Location']= location.text
        except NoSuchElementException:
            df3.loc[indexfnnum,'Location']= "None"
            pass

        print("--------------------------------------------------------------------------------------------------------------------")

        indexfnnum += 1
        expertise_level_num+=1
        description_num+=1
        posted_time_num+=1

    print(df3)
    df3.to_csv(PATH_TO_OUTPUT_CSV_FILE)

        
print("--------------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------------")
        
