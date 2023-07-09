from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException


from .conf import DIGIKALA_USER_NAME, DIGIKALA_PASSWORD

from .utils import wiat_to_find

def digikala_login():
    pas = DIGIKALA_PASSWORD
    usr = DIGIKALA_USER_NAME
    
    if pas == '' and usr == '':
        usr = str(input('type your digikala username : '))
        pas = str(input('type your digikala password : '))
        
        
    driver = webdriver.Chrome()
    driver.delete_all_cookies()
    driver.headless = True
    driver.get('https://www.digikala.com/')
    
    
    
    try:
    
        login = wiat_to_find(driver, By.XPATH, '//*[@id="base_layout_desktop_fixed_header"]/header/div[2]/div/div/div[2]/a/button/div[2]')
                                            
        login.click()
        username_field = wiat_to_find(driver, By.XPATH, '//*[@id="__next"]/main/div[2]/div[2]/form/label/div/div/input')
        username_field.clear()
        username_field.send_keys(usr)
        username_field.send_keys(Keys.ENTER)
        driver.implicitly_wait(5)
        
        pass_field = wiat_to_find(driver, By.XPATH, '/html/body/div[1]/main/div[2]/div[2]/form/label/div/div[1]/input')
        pass_field.clear()
        pass_field.send_keys(pas)
        pass_field.send_keys(Keys.ENTER)
        
        driver.quit()

        
    except (TimeoutException, WebDriverException, NoSuchElementException) as e:
        print('Error occured %s' %e)
    
    
    sleep(5)
    
    