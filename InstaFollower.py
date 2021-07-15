# 1. Create a class called InstaFollower

# 2. In the init() method, create the Selenium driver .

# 3. Create three methods - login() and find_followers() and follow().

# 4. Outside of the class, initialise the object and call the three methods in order.
import time
from selenium import webdriver
from selenium.webdriver.common import keys

CHROME_DRIVER_PATH = "/Users/prog/VScode/Github/chromedriver"
# "/Users/prog/VScode/python/webdev/chromedriver"
INTERESTED_TAG = "interior design"
ig_id = "billy@polishedconcrete.com.hk"
ig_password = "abcde12345"


class InstaFollower:

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        print("in login function")

    def find_followers(self):
        print("find followers function")

    def follow(self):
        print("in follow function")


ig = InstaFollower()
ig.login()
ig.find_followers()
ig.follow()
