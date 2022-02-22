from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


class Landing:
    # Locator of all the element on Landing
    Home_xpath = "//*[@class='homeLink']"
    Feature_xpath = "//a[contains(text(),'Feature')]"
    Business_ptr_xpath = "//*[@class='anchorBtn']"
    Business_ptr_btn2_xpath = "//*[@class='btn businessBtn mt-5']"
    Terms_condition_xpath = \
        "//a[contains(text(),'Terms & Conditions')]"
    Privacy_xpath = "//a[contains(text(),'Privacy Policy')]"
    About_xpath = "//a[contains(text(),'About Us')]"
    Support_xpath = "//a[contains(text(),'Support')]"
    Contact_xpath = "//a[contains(text(),'Contact Us')]"
    terms_cond_back_xpath = "//img[@src='assets/auth-img/Group 154.png']" # for image that doesn't contain any tag like class,id, title.
    policy_back_xpath = "//img[@src='assets/auth-img/Group 154.png']"
    terms_heading_text = "//h3[text() = 'END USER LICENSE AGREEMENT ']"
    privacy_heading_text = "//h3[text() = 'Privacy Policy']"
    about_heading_text = "//h3[text() = 'About Us']"


    def __init__(self, driver):
        self.driver = driver

    def home_btn(self):
        self.driver.find_element(By.XPATH, self.Home_xpath).click()

    def feature_btn(self):
        self.driver.find_element(By.XPATH, self.Feature_xpath).click()

    def business_ptr_btn(self):
        self.driver.find_element(By.XPATH, self.Business_ptr_xpath).click()

    def business_ptr_btn2(self):
        self.driver.find_element(By.XPATH, self.Business_ptr_btn2_xpath).click()

    def terms_cond_btn(self):
        btn = self.driver.find_element(By.XPATH, self.Terms_condition_xpath)
        action = ActionChains(self.driver)
        action.move_to_element(btn).click().perform()
        time.sleep(10)
        terms_heading1 = self.driver.find_element(By.XPATH, self.terms_heading_text)
        print(terms_heading1.text)
        try:
            assert terms_heading1.text == 'END USER LICENSE AGREEMENT'
        except AssertionError:
            print("Assertion failed Terms and condition Heading doesn't match")


    def privacy_btn(self):
        self.driver.find_element(By.XPATH, self.Privacy_xpath).click()
        privacy_heading1 = self.driver.find_element(By.XPATH, self.privacy_heading_text)
        print(privacy_heading1.text)
        try:
            assert privacy_heading1.text == 'Privacy Policy'
        except AssertionError:
            print("Assertion failed Privacy Heading doesn't match")

    def about_btn(self):
        self.driver.find_element(By.XPATH, self.About_xpath).click()
        about_heading1 = self.driver.find_element(By.XPATH, self.about_heading_text)
        print(about_heading1.text)
        try:
            assert about_heading1.text == 'About Us'
        except AssertionError:
            print("Assertion failed About Us Heading doesn't match")

    # def support_btn(self):
    #     self.driver.find_element(By.XPATH, self.Support_xpath).click()
    #
    # def contact_btn(self):
    #     self.driver.find_element(By.XPATH, self.Contact_xpath).click()

    def back_btn_terms(self):
        self.driver.find_element(By.XPATH, self.terms_cond_back_xpath).click()

    def back_btn_policy(self):
        self.driver.find_element(By.XPATH, self.policy_back_xpath).click()
