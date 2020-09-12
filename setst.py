import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException

options = Options()
# options.add_argument('--no-sandbox')
# options.add_argument('--headless')
driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.implicitly_wait(5)
driver.get('https://ecp.sgcc.com.cn/ecp2.0/portal/#/list/list-com/2018032600289606_1_2018060501171111')

nattach = 0
amount = 0

while True:
    elements = driver.find_elements_by_css_selector('tr[_ngcontent-c8]')
    n = len(elements)

    for i in range(n):
        elements[i].click()
        amount += 1
        try:
            # driver.find_element_by_css_selector('a[_ngcontent-c13]')
            driver.find_element_by_css_selector('a[_ngcontent-c13]')
            nattach += 1
        except NoSuchElementException:
            pass
        finally:
            print(driver.current_url)
            driver.back()
            elements = driver.find_elements_by_css_selector('tr[_ngcontent-c8]')

    np = driver.find_element_by_css_selector('.btn-page[_ngcontent-c11]:nth-last-child(2)')
    if (np.get_attribute('disabled')):
        break
    else:
        np.click()
        print(driver.find_element_by_css_selector('a.lh_36[_ngcontent-c11]').text)


print("total: {}. attach: {}".format(amount, nattach))

driver.quit()