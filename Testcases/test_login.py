import sys

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Utilities.readProperty import ReadConfig
from PageObject.Signup import Signup
from PageObject.Landing import Landing
from PageObject.login import Login
from PageObject.Addstore import Createstore
from PageObject.Adddeals import Createdeal
from PageObject.Setting import Setting_Option
from PageObject.Support import Support
import unittest
import HtmlTestRunner
from selenium import webdriver
import time

sys.path.append("/")


class Dashboard(unittest.TestCase):

    baseURL = "http://d2i4tgribplrd3.cloudfront.net/landing"
    driver = webdriver.Chrome(executable_path="C:\\Users\\Algoworks\\Downloads\\chromedriver_win32\\chromedriver.exe")
    # for deals screen
    Deal_name_error = "//*[@id='content']/div[2]/app-add-edit-deal/div[2]/div/form/div[1]/div[1]/div/div/span"
    # for store screen
    sname = "Grofers."
    semail = "grofers@getnada.com"
    sURL = "www.grofers.com"
    sphone = "+91 9812913393"
    saddress = "47687888 Coburn Hollow Road"
    scity =  "Atlanta"
    sstate =  "Georgia"
    scountry = "United States"
    szip = "61534"
    suploadImage = "/home/algoworks/Downloads/Image/istockphoto-1180542165-612x612.jpg"
    sdescription = "A product description is the marketing copy that explains what a product is and why it’s worth " \
                   "purchasing."

    # for edit deals
    udeal_name = "Acer Laptops"
    ustart_date = "01/30/2022, 6:00 AM"
    uend_date = "6/3/2022, 6:00 AM"
    udescription = "Acer Aspire 7 Gaming Laptop Intel Core i5 10th Gen A715-75G with 39.6cm"

    @classmethod
    def setUpClass(cls):
        cls.driver.get(ReadConfig.getURL())
        cls.driver.maximize_window()

    def test_dashboard_functionality(self):

        self.new_acc = Signup(self.driver)
        self.Startup_page = Landing(self.driver)
        self.log_screen = Login(self.driver)
        self.newdeal = Createdeal(self.driver)
        self.newstore = Createstore(self.driver)
        self.support_screen = Support(self.driver)
        self.settingscreen = Setting_Option(self.driver)


        self.Startup_page.business_ptr_btn()
        time.sleep(4)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(4)
        self.new_acc.signInbtn()
        time.sleep(4)
        self.log_screen.login_with_email()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\Algoworks\\PycharmProjects\\Pobal_Project_POM\\report"))

