from PageObject.login import Login
from PageObject.Signup import Signup
from PageObject.Landing import Landing
from PageObject.Addstore import Createstore
from PageObject.Adddeals import Createdeal
from PageObject.Setting import Setting_Option
from PageObject.Support import Support
import unittest
import HtmlTestRunner
from selenium import webdriver
import time



class Dashboard(unittest.TestCase):
    baseURL = "http://d2i4tgribplrd3.cloudfront.net/landing"
    driver = webdriver.Chrome(executable_path="C:\\Users\\Algoworks\\Downloads\\chromedriver_win32\\chromedriver.exe")
    # for login
    emailid = 'testuser01@zetmail.com'
    con_name = "India (भारत)"
    phone = "7503366790"
    login_pass = 'Qwerty@12345'
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
        cls.driver.get(cls.baseURL)
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
        self.log_screen.login_with_email(self.emailid, self.login_pass)
        self.newstore.add_store(self.sname, self.semail, self.sURL, self.sphone, self.saddress, self.scity, self.sstate, self.scountry, self.szip, self.suploadImage, self.sdescription)
        time.sleep(4)
        self.newdeal.create_deals()
        time.sleep(4)
        self.driver.execute_script("window.scrollBy(0,-100000)")
        time.sleep(4)
        self.support_screen.support_message()
        time.sleep(4)
        self.driver.execute_script("window.scrollBy(0,-100000)")
        time.sleep(4)
        self.settingscreen.changePass()
        time.sleep(4)
        self.settingscreen.about_us()
        time.sleep(4)
        self.settingscreen.privacy_policy()
        time.sleep(4)
        self.settingscreen.terms_condition()
        time.sleep(4)
        self.settingscreen.faqs()
        time.sleep(4)
        self.newdeal.editdeals(self.udeal_name, self.ustart_date, self.uend_date, self.udescription)
        time.sleep(4)
        self.newdeal.delete_deals()


        # adding_deals.add_deals_error()
        # # identify actual error message
        # self.act = self.driver.find_element(By.XPATH, self.Deal_name_error).text
        # # expected error text String
        # self.expected_message = "Please enter Deal Name"
        # # verify error message
        # self.assertEqual(self.expected_message, self.act)



        time.sleep(2)
        self.log_screen.logout()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\Algoworks\\PycharmProjects\\Pobal_Project_POM\\report"))
