from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = Options()
chrome_options.add_argument("--headless")  # do not show the Chrome window
driver = webdriver.Chrome()
driver.maximize_window()



def get_crunchbase(name):
    driver.get("https://www.crunchbase.com/")
    WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="search-crunchbase"]')))
    
    search = driver.find_element(By.XPATH, '//*[@id="search-crunchbase"]')
    search.send_keys(name)
    time.sleep(5)

    click_name=driver.find_element(By.XPATH, '/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/multi-search-results/page-layout/div/div/div/search-results-section[1]/mat-card/a[1]')
    click_name.click()

    about=driver.find_element(By.XPATH,'//*[@id="mat-tab-nav-panel-0"]/div/full-profile/page-centered-layout[1]/div/row-card/div/div[1]/profile-section/section-card/mat-card/div[2]/description-card/div/span').text
    location=driver.find_element(By.XPATH,'//*[@id="mat-tab-nav-panel-0"]/div/full-profile/page-centered-layout[1]/div/row-card/div/div[1]/profile-section/section-card/mat-card/div[2]/fields-card/ul/li[1]/label-with-icon/span/field-formatter/identifier-multi-formatter/span/a[1]').text

    financials=driver.find_element(By.XPATH,'//*[@id="mat-tab-link-2"]')
    financials.click()

    WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="mat-tab-nav-panel-0"]/div/full-profile/page-centered-layout[1]/div/row-card/div/div[2]/profile-section/section-card/mat-card/div[2]/div/obfuscation-cta/phrase-list-card[1]/obfuscation/obfuscation-cta/markup-block/field-formatter[2]/span/obfuscation-cta/div[2]/div/a')))

    funding=driver.find_element(By.XPATH,'//*[@id="mat-tab-nav-panel-0"]/div/full-profile/page-centered-layout[1]/div/row-card/div/div[2]/profile-section/section-card/mat-card/div[2]/div/obfuscation-cta/phrase-list-card[1]/obfuscation/obfuscation-cta/markup-block/field-formatter[2]/span/obfuscation-cta/div[2]/div/a').text    
    funding_rounds=driver.find_element(By.XPATH,'//*[@id="mat-tab-nav-panel-0"]/div/full-profile/page-centered-layout[1]/div/row-card/div/div[1]/profile-section/section-card/mat-card/div[2]/anchored-values/div[1]/a/div/field-formatter/span').text
    driver.close()
    return {about,location,funding,funding_rounds}