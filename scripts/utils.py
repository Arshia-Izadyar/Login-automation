from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def wiat_to_find(driver, by, path):
    
    return WebDriverWait(driver, 5).until(EC.presence_of_element_located((by, path)))