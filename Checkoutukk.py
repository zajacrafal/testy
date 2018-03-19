from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium import webdriver

selenium_grid_url = "http://localhost:4444/wd/hub"

# Create a desired capabilities object as a starting point.
capabilities = webdriver.DesiredCapabilities.CHROME.copy()
capabilities["browser"]="Chrome"

# Instantiate an instance of Remote WebDriver with the desired capabilities.
driver = webdriver.Remote(desired_capabilities=capabilities,
                         command_executor=selenium_grid_url)



driver.get("https://zzysh.me/uk/en/shop")
if not "Products" in driver.title:
    raise Exception("Unable to load Zzysh page!")

#Zamkniecie popupa z jezykiem

test1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#redirect_popup > input.close_popup")))
driver = test1.click()

time.sleep(3)

#Zamkniecie popupa z newsletterem

driver.find_element_by_class_name('popup_voucher__close').click()


time.sleep(2)

#Zamkniecie intercomu
driver.find_element_by_xpath('//*[@id="intercom-container"]/div/iframe[2]').click()
driver.find_element_by_xpath('//*[@id="intercom-container"]/div/iframe[2]').click()


time.sleep(2)

driver.find_element_by_css_selector('#product-submit-2183').click()


time.sleep(5)


driver.find_element_by_class_name('go-to-cart').click()


time.sleep(5)

driver.find_element_by_class_name('checkout-button').click()


time.sleep(2)

driver.find_element_by_id('guest-account-checkout').click()


time.sleep(2)

driver.find_element_by_id('billing_email').send_keys('test@test.pl')
driver.find_element_by_id('billing_gender').click()
driver.find_element_by_id('option_1').click()
driver.find_element_by_id('billing_first_name').send_keys('Tester')
driver.find_element_by_id('billing_last_name').send_keys('Testowy')
driver.find_element_by_id('billing_address_1').send_keys('Krakowska 29D')
driver.find_element_by_id('billing_city').send_keys('Wroclaw')
driver.find_element_by_id('billing_state').send_keys('Poland')
driver.find_element_by_id('billing_postcode').send_keys('12345')


time.sleep(5)

driver.find_element_by_class_name('payment-method-gateway-adyen').click()


time.sleep(5)

driver.find_elements_by_css_selector("input[type='radio'][value='adyen']")[1].click()

driver.quit()
