import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.implicitly_wait(10)
driver.get('https://ecp.sgcc.com.cn/ecp2.0/portal/#/list/list-com/2018032600289606_1_2018060501171111')

n = 0
while True:
    n += 1
    el = driver.find_element_by_css_selector('.btn-page[_ngcontent-c11]:nth-last-child(2)')
    print(el.get_attribute('disabled'))
    if (el.get_attribute('disabled')):
        break
    else:
        el.click()

print("total:{}".format(n))
driver.quit()