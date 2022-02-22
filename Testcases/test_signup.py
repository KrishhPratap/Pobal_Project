from PageObject.Signup import Signup
from PageObject.Landing import Landing
import unittest
import HtmlTestRunner
from selenium import webdriver
import time
import sys



class TestSignup(unittest.TestCase):
    baseURL = "http://d2i4tgribplrd3.cloudfront.net/landing"
    driver = webdriver.Chrome(executable_path="/home/algoworks/Downloads/chromedriver_linux64/chromedriver")
    username = "TestUser"
    emailaddress = "testuser01@zetmail.com"
    countryname = "India (भारत)"
    phonenumber = "7503366790"
    password = "Qwerty@123"
    confirmpassword = "Qwerty@123"

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_signUp(self):
         new_acc = Signup(self.driver)
         create_account = Landing(self.driver)
         create_account.business_ptr_btn()
         time.sleep(2)

         """
         new_acc.setName(self.username)
         time.sleep(1)
         new_acc.setEmailId(self.emailaddress)
         time.sleep(1)
         new_acc.setCountry(self.countryname)
         time.sleep(1)
         new_acc.setPhoneNo(self.phonenumber)
         time.sleep(1)
         new_acc.setPassword(self.password)
         time.sleep(1)
         new_acc.pass_eyeBtn()
         time.sleep(1)
         new_acc.set_confirm_password(self.confirmpassword)
         new_acc.confirm_Pass_eyeBtn()
         time.sleep(1)
         new_acc.terms_condition()
         time.sleep(1)
         self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
         time.sleep(2)
         new_acc.signInbtn()
         time.sleep(1)
         """


         new_acc.signup()
         time.sleep(5)
         self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
         time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/algoworks/PycharmProjects/DemoProject/Reports"))




