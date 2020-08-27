from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
from webdriver_manager.chrome import ChromeDriverManager




#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver= webdriver.Chrome("chromedriver.exe")

chrome_options = webdriver.ChromeOptions()
#pentru a nu mai aparea popup-urile default deoarece nu o sa mai functioneze butoanele din cauza lor
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=chrome_options)



class PostOnFacebook():
        def post_on_facebook(self, user, pwd):
            self.user = user
            self.pwd = pwd
            print(self.user, self.pwd)
            #driver = webdriver.Chrome()
            driver.get('https://www.facebook.com')

            email = driver.find_element_by_xpath('//*[@id="email"]')
            email.send_keys(self.user)
            print("email entered...")
            password = driver.find_element_by_xpath('//*[@id="pass"]')
            password.send_keys(self.pwd)
            print("Password entered...")
            time.sleep(1)


            button = driver.find_element_by_xpath('//*[@id="u_0_d"]')
            button.click()


            time.sleep(5)

            driver.get('https://www.facebook.com/fb-page/')
            time.sleep(5)

            status = driver.find_element_by_tag_name("textarea")
            status.send_keys("text")

            driver.implicitly_wait(10)

            print("Status trying")
            button = driver.find_element_by_xpath('//*[@class="_1mf7 _4jy0 _4jy3 _4jy1 _51sy selected _42ft"]')
            time.sleep(5)
            button.click()



text_file = open("text.txt", "r")
lines = text_file.read().split()
print(lines)
print(len(lines))
text_file.close()

account = PostOnFacebook()

i = 0

while i < len(lines):
    user = lines[i]
    pwd = lines[i+1]
    account.post_on_facebook(user, pwd)
    print(user, pwd)
    i+=2
