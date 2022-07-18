import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pyperclip

#Chorme is opened
resulstList = open('results.txt', "w")

browser = webdriver.Chrome(executable_path=r"C:\Users\elif.kurucay\Selenium\ChromeDriver\chromedriver.exe")
browser.set_window_size(1920, 1080)
browser.maximize_window()

browser.get('https://stagexeonrecui.trendyol.com/#/user/login') #goes to xeon screen
login_name = browser.find_element_by_id('username') #finds where to write username
login_name.click()
login_name.send_keys("elif.kurucay") #writes the username

login_pass = browser.find_element_by_id('password')  #finds where to write password
login_pass.click()
login_pass.send_keys("Hosgeldin1234") #writes the password
browser.find_element_by_id('login').click() #clicks the login button
time.sleep(2)
browser.get('https://stagexeonmembershipui.trendyol.com/#/pages/user') #goes to the xeon authorization screen
time.sleep(1)
newuser = browser.find_element_by_id('newUser') #finds add the new user button
newuser.click()


with open("userList.txt", "r", encoding="utf-8") as userList: #Opens user list with read authorization
#reads the user list sequentially and executes the operations
    for line in userList:
        fullname = browser.find_element_by_id('name') #finds where to write name
        fullname.click()
        fullname.send_keys(line) #write the next user
        time.sleep(1)


        password = browser.find_element_by_id('password') #finds where to write password
        password.click()
        password.send_keys('Abcd1234') #write the password

        passConfirm = browser.find_element_by_id('passwordConfirm') #finds where to write confirm password
        passConfirm.click()
        passConfirm.send_keys('Abcd1234') #Confirm Password
        time.sleep(1)

        #Add Warehouse
        warehouse = browser.find_element_by_css_selector( #The warehouse finds the area to be authorized
            '#userForm > fieldset > div:nth-child(4) > div > ng-select > div > div > div.ng-input > input[type=text]')
        warehouse.click()
        warehouse.send_keys('AKASYA', Keys.ENTER, Keys.TAB) #Writes the warehouse and switch to bottom tab

        #Add Role
        command = browser.find_element_by_css_selector( #Finds the roles field
            '#userForm > fieldset > div:nth-child(5) > div > ng-select > div > div > div.ng-input > input[type=text]')
        command.click()
        command.send_keys('Mal Kabul Kullanıcısı', Keys.ENTER) #Writes the role
        command.send_keys('Paketleme', Keys.ENTER)


        # Writes the generated user list to the file named "resultList".
        browser.find_element_by_css_selector('#username').click()
        act = ActionChains(browser)
        act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
        text = pyperclip.paste()
        resulstList.write(text + '\n')

        browser.find_element_by_id('save-btn').click()
        time.sleep(1)
        browser.find_element_by_id('newUser').click()

browser.close()

