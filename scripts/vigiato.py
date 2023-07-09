from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException

from .utils import wiat_to_find

from .conf import VIGIATO_PASSWORD, VIGIATO_USER_NAME

def login_vigiato():
    pas = VIGIATO_PASSWORD
    usr = VIGIATO_USER_NAME
    if pas == '' and usr == '':
        usr = str(input('type your digikala username : '))
        pas = str(input('type your digikala password : '))
                
    driver = webdriver.Chrome()
    driver.delete_all_cookies()
    driver.headless = True
    driver.get('https://vigiato.net')
    
    try:
    
        login = wiat_to_find(driver, By.XPATH, '//*[@id="header"]/div[3]/div/nav/div[2]/div/a[1]')
        login.click()
                                            
        username_field = wiat_to_find(driver, By.XPATH, '//*[@id="user_login"]')
        username_field.clear()                  
        username_field.send_keys(usr)
        driver.implicitly_wait(3)
        
        pass_field = wiat_to_find(driver, By.XPATH, '//*[@id="user_pass"]')
        pass_field.clear()
        pass_field.send_keys(pas)
        pass_field.send_keys(Keys.ENTER)

        driver.quit()
    except (TimeoutException, WebDriverException, NoSuchElementException) as e:
        print('Error occured %s' %e)
    