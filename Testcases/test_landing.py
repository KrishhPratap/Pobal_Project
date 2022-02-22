from PageObject.Landing import Landing
import unittest
from selenium import webdriver
import time
import HtmlTestRunner


class Test_landing(unittest.TestCase):
    baseURL = "http://d2i4tgribplrd3.cloudfront.net/landing"
    driver = webdriver.Chrome(executable_path="C:/Users/Algoworks/Downloads/chromedriver_win32/chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_landing(self):
        landing_page = Landing(self.driver)
        landing_page.feature_btn()
        # self.driver.execute_script("window.scrollBy(266, 1500)","")
        # for handling the scroll bar at specific position
        # self.driver.execute_script("arguments[0].scrollIntoView();", landing_page.terms_cond_btn())
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(3)
        landing_page.terms_cond_btn()
        # parent_window = self.driver.current_window_handle
        # child_window = self.driver.window_handles  # returns all the handles value of the opened browser
        # print(parent_window)
        # print(child_window)
        # for parent_window in child_window:
        #     if(parent_window!=child_window):
        #         self.driver.switch_to.window(parent_window)
        #         break
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,-100000)")   # scroll from top to down
        time.sleep(1)
        landing_page.back_btn_terms()
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(1)
        landing_page.privacy_btn()
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,-100000)")
        time.sleep(1)
        landing_page.back_btn_policy()
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(1)
        landing_page.business_ptr_btn2()
        self.assertEqual("PobalWebPanel", self.driver.title, "Title not matched")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Algoworks/PycharmProjects/Pobal_Project/Reports"))
