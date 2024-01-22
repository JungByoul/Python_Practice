import time

import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import Select

# Chrome WebDriver 경로 설정
chrome_driver_path = '/Users/Star1/Downloads/chromedriver-mac-x64/chromedriver'

# Chrome WebDriver 서비스 초기화
service = Service(chrome_driver_path)

# Chrome WebDriver 초기화
driver = webdriver.Chrome()
driver = webdriver.Chrome(service=service)

# 웹 페이지로 이동
url = 'https://www.nongsaro.go.kr/portal/ps/psa/psab/psabe/openApiSoilVrifyLst.ps?menuId=PS03329'
driver.get(url)

dae_gyung = ["27", "41"]

fruit_place = driver.find_element(By.XPATH, '//*[@id="exam_type_radio5"]')
fruit_place.click()

time.sleep(2)
do_place = driver.find_element(By.ID, 'siDoLst')
select = Select(do_place)

options = select.options

# 각 Option의 값을 출력
for option in options:
    print(option.get_attribute('value'))


#do_place.click()
print(do_place)



for option in options:
    if option.get_attribute('value') == dae_gyung[0]:
        option.click()
        print('sss')
        time.sleep(3)
        break

si_goon_goo = driver.find_element(By.ID, 'siGunGuLst')
select_si = Select(si_goon_goo)
si_options = select_si.options

# 각 Option의 값을 출력
for option in si_options:
    print(option.get_attribute('value'))


# try:

# except:

eup_myeon = driver.find_element(By.ID, "townMyeonDongLst")
select_eup = Select(eup_myeon)

