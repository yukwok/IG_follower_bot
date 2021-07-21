import time
from selenium import webdriver
from selenium.webdriver.common import keys

CHROME_DRIVER_PATH = "/Users/prog/VScode/Github/chromedriver"
# "/Users/prog/VScode/python/webdev/chromedriver"
INTERESTED_TAG = "interior design"
ig_id = "billy@polishedconcrete.com.hk"
ig_password = "abcde12345"


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        ig_url = "https://www.instagram.com/accounts/login/"
        self.driver.get(ig_url)
        time.sleep(5)

        email = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.send_keys(ig_id)

        password = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(ig_password)
        password.send_keys(keys.Keys.ENTER)

        print("in login function")

    def find_followers(self):
        print("find followers function")

    def follow(self):
        print("in follow function")


ig = InstaFollower()
ig.login()
# ig.find_followers()
# ig.follow()
