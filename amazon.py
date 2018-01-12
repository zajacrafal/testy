from selenium import webdriver



driver = webdriver.Chrome(executable_path='/Users/rafal/Downloads/chromedriver')


driver.get("https://zzysh.me/uk/en/shop/")
if not "Zzysh" in driver.title:
    raise Exception("Unable to load Zzysh page!")
assert "Zzysh" in driver.title
windows = driver.window_handles



#Zamkniecie popupa z jezykiem
driver.find_element_by_css_selector('#redirect_popup > input.close_popup').click()


import time
time.sleep(2)

#Zamkniecie popupa z newsletterem
driver.find_element_by_css_selector('#popup_voucher > div').click()

import time
time.sleep(2)

#Zamkniecie intercomu
driver.find_element_by_xpath('//*[@id="intercom-container"]/div/iframe[2]').click()
driver.find_element_by_xpath('//*[@id="intercom-container"]/div/iframe[2]').click()

import time
time.sleep(2)

liczba_elementow = len(driver.find_elements_by_class_name('product-list-start'))
print('Liczba produktów =', liczba_elementow)

bledy = []

x = 1

while x <= 10:



    amazon = driver.find_element_by_css_selector('#sort-me > li:nth-child('+str(x)+')')
    tytul = amazon.find_element_by_css_selector('div > div > label').get_attribute('innerText').replace("\n", " ")
    amazon.find_element_by_class_name('button_shop_page').click()
    tytul = tytul[7:]

    windows = driver.window_handles

    print(tytul)
    int(x)
    x += 1
    amazon.find_element_by_css_selector('a').get_attribute('href')
    print('sprawdzam produkt', amazon.find_element_by_css_selector('a').get_attribute('href'))


    import time
    time.sleep(4)

    driver.switch_to.window(windows[1])

    tytul_amazon = driver.find_element_by_class_name('centerColAlign')
    tytul_amazon1 = tytul_amazon.find_element_by_id('titleSection').get_attribute('innerText')

    print(tytul_amazon1)

    if tytul.lower().find(tytul_amazon1):
        print("Link się zgadza")
    else:
        bledy.append(str(tytul))
        print("Link nie działa")

    driver.close()
    driver.switch_to.window(windows[0])

    import time
    time.sleep(2)

if len(bledy) == 0:
    print("Wszystkie linki działają poprawnie")
else:
    print("Blędne linkowanie w:", bledy)


driver.quit()