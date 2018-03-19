from selenium import webdriver

selenium_grid_url = "http://127.0.0.1:4444/wd/hub"

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
driver.find_element_by_css_selector('#redirect_popup > input.close_popup').click()

import time
time.sleep(3)

#Zamkniecie popupa z newsletterem
driver.find_element_by_class_name('popup_voucher__close').click()

import time
time.sleep(2)

#Zamkniecie intercomu
driver.find_element_by_xpath('//*[@id="intercom-container"]/div/iframe[2]').click()
driver.find_element_by_xpath('//*[@id="intercom-container"]/div/iframe[2]').click()

import time
time.sleep(2)

driver.find_element_by_css_selector('#product-submit-2183').click()

import time
time.sleep(5)


driver.find_element_by_class_name('go-to-cart').click()

import time
time.sleep(5)

driver.find_element_by_class_name('checkout-button').click()

import time
time.sleep(2)

driver.find_element_by_id('guest-account-checkout').click()

import time
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

import time
time.sleep(5)

driver.find_element_by_class_name('payment-method-gateway-adyen').click()

import time
time.sleep(5)

driver.find_elements_by_css_selector("input[type='radio'][value='adyen']")[1].click()


#import time
#time.sleep(25)

#driver.find_element_by_class_name('checkbox-new').click()


#import time
#time.sleep(10)

#driver.find_element_by_css_selector('#place_order').click()

#import time
#time.sleep(5)

driver.quit()
