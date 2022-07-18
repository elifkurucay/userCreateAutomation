import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pyperclip

resulstList = open('results.txt', "w")

browser = webdriver.Chrome(executable_path=r"C:\Users\elif.kurucay\Selenium\ChromeDriver\chromedriver.exe")
browser.set_window_size(1920, 1080)
browser.maximize_window()
browser.get('https://xeonrecui.trendyol.com/#/user/login')

login_name = browser.find_element_by_id('username')
login_name.click()
login_name.send_keys("elif.kurucay")

login_pass = browser.find_element_by_id('password')
login_pass.click()
login_pass.send_keys("Abcd1234")
browser.find_element_by_id('login').click()
time.sleep(2)
browser.get('https://xeonmembershipui.trendyol.com/#/pages/user')
time.sleep(1)

newuser = browser.find_element_by_id('newUser')
newuser.click()


with open("userList.txt", "r") as userList:

    for line in userList:
        fullname = browser.find_element_by_id('name')
        fullname.click()
        fullname.send_keys(line)
        time.sleep(1)

        # Kullanıcı için password verilmesi ve confirm edilmesi
        password = browser.find_element_by_id('password')
        password.click()
        password.send_keys('Abcd1234')

        passConfirm = browser.find_element_by_id('passwordConfirm')
        passConfirm.click()
        passConfirm.send_keys('Abcd1234')
        time.sleep(1)

        # Kullanıcıya istenen depo yetkisi verilir.
        warehouse = browser.find_element_by_css_selector(
            '#userForm > fieldset > div:nth-child(4) > div > ng-select > div > div > div.ng-input > input[type=text]')
        warehouse.click()
        warehouse.send_keys('AKASYA', Keys.ENTER, Keys.TAB)

        # Kullanıcıya Fix 3 yetkiyi verir. Rf yoktu stage de eklenemedi.
        command = browser.find_element_by_css_selector(
            '#userForm > fieldset > div:nth-child(5) > div > ng-select > div > div > div.ng-input > input[type=text]')
        command.click()
        command.send_keys('Kaizen Opex - Yönetim', Keys.ENTER)


        # Oluşan kulanıcının çıktı olarak verilmesi.
        browser.find_element_by_css_selector('#username').click()
        act = ActionChains(browser)
        act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        time.sleep(2)
        text = pyperclip.paste()
        resulstList.write(text + '\n')

        browser.find_element_by_id('save-btn').click()
        time.sleep(5)

        time.sleep(3)
        browser.find_element_by_id('newUser').click()

    # browser.close()

