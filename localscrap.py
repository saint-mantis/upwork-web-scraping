from cgitb import text
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By


if __name__ == '__main__': 

    PATH = "/Users/saintmantis/Downloads/chromedriver"
    driver = uc.Chrome(executable_path=PATH) 
    driver.get("http://127.0.0.1:5500/up.html")
    #my-0 p-sm-right job-tile-title
    maindiv = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div/div/div/div[2]/div/div[1]')
    print(maindiv)
    jobs = maindiv.find_elements(By.CSS_SELECTOR, "*")
    #print(jobs)
    print(f'{len(jobs)} jobs found')
    heading = jobs[0]
    print(heading.text)

        

        

'''/html/body/div[3]/div/span/div/div/main/div/div[2]/div/div/div/div/div[2]/div/div[1]/section[1]/div[1]
/html/body/div[3]/div/span/div/div/main/div/div[2]/div/div/div/div/div[2]/div/div[1]/section[1]/div[2]

/html/body/div[3]/div/span/div/div/main/div/div[2]/div/div/div/div/div[2]/div/div[1]/section[2]/div[1]
#job-1565030848808615936 > div.row.my-10
#job-1565030848808615936'''