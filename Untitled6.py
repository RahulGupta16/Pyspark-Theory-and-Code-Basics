import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


serv_path = Service(executable_path= r"C:\Users\Rahul\Desktop\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_path)
website = r'https://data.cosmic.ucar.edu/gnss-ro/cosmic2/nrt/'

def main(driver, website):
    driver.get(website)
    driver.find_element(By.LINK_TEXT,'level2/').click()
    years = [i.text for i in driver.find_elements(By.TAG_NAME,'a')][1:]
    for year in years:
        driver.find_element(By.LINK_TEXT,year).click()
        versions = [i.text for i in driver.find_elements(By.TAG_NAME,'a')][1:]
        for version in versions:
            driver.find_element(By.LINK_TEXT,version).click()
            files = [i.text for i in driver.find_elements(By.TAG_NAME,'a') if str(i.text).startswith('wetPf2')]
            if(len(files)>0):
                #driver.find_element(By.LINK_TEXT,files[0]).click()
                pass
            driver.back()
        driver.back()

    driver.close()


if __name__=='__main__':
    main(driver,website)