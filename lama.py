from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options


import time

selenium_grid_url = "http://127.0.0.1:4444/wd/hub"

# Create a desired capabilities object as a starting point.
capabilities = webdriver.DesiredCapabilities.CHROME.copy()
capabilities["browser"]="Chrome"

# Instantiate an instance of Remote WebDriver with the desired capabilities.
driver = webdriver.Remote(desired_capabilities=capabilities,
                         command_executor=selenium_grid_url)

#driver.set_window_size(1920, 1080)


driver.get("https://www.lama-media.com/career")
driver.implicitly_wait(5)

if "Lama Media" not in driver.title:
   raise Exception("Nie udało się załadować strony")

try:
   cookies = driver.find_element_by_xpath('/html/body/section[2]/div/a').click()
except Exception:
   print('Brak komunikatu o plikach cookies lub zmienił się xpath')

a = '1'
b = 1
tablica_ofert = []

while True:
   try:
       # znalezienie naglowka oferty
       #selector = driver.find_element_by_css_selector('div.row.job-offers__wrapper > div:nth-child('+a+') > div > h2')
       czy_ostatni = selector.get_attribute('innerText')
       # sprawdzenie czy naglówek nie jest ostatnim elementem
       if (czy_ostatni == 'No match for you?'):
           break
       button = driver.find_element_by_css_selector('div.row.job-offers__wrapper > div:nth-child('+a+') > div > a')
       button.location_once_scrolled_into_view
       driver.execute_script("window.scrollBy(0,150);")
       print('sprawdzam ofertę', selector.get_attribute('innerText'))
       tablica_ofert.append(str(selector.get_attribute('innerText')))
       time.sleep(1)
       button.click()
       time.sleep(1)
       naglowek = driver.find_element_by_css_selector('div.col-sm-12.col-md-8.col-lg-9 > header > h1').get_attribute('innerText')
       if (str(naglowek) == tablica_ofert[b-1]):
           print('naglowki zgodne')
       else:
           print('niezgodne naglowki w ofercie', tablica_ofert[b-1])
           break
       try:
           driver.find_element_by_css_selector('div.col-sm-12.col-md-4.col-lg-3 > div > a').location_once_scrolled_into_view
           driver.execute_script("window.scrollBy(0,150);")
           driver.find_element_by_css_selector('div.col-sm-12.col-md-4.col-lg-3 > div > a').click()
           print('Popup się otwiera')
           time.sleep(1)
           try:
               driver.find_element_by_css_selector('div.popup-modal__send-btn-wrapper > input').location_once_scrolled_into_view
               driver.execute_script("window.scrollBy(0,150);")
               driver.find_element_by_css_selector('div.popup-modal__send-btn-wrapper > input').click()
               print('Button Send klikalny')
               time.sleep(1)
           except Exception:
               print('Brak buttona Send')
           try:
               driver.find_element_by_css_selector('div.popup-modal__top-bar > div').click()
               print('Popup się zamyka')
               time.sleep(1)
           except Exception:
               print('Brak popupa w ofercie', tablica_ofert[b-1])
               break
       except Exception:
           print('Nieaktywny button aplikacji w ofercie', tablica_ofert[b-1])
           break

       driver.find_element_by_xpath('/html/body/main/section[2]/div/div/div[1]/div/a').click()

       time.sleep(1)
       b += 1
       a = str(b)
       print('')
   except Exception:
       print('Błąd sprawdzania')
       break

driver.quit()
