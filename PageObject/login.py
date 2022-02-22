import time

from selenium.webdriver.common.by import By
from Utilities.readProperty import ReadConfig
from selenium.webdriver.support.ui import Select


class Login:
    # login page locator
    email_xpath = "//input[@type='text']"
    Country_name_xpath = "//li[@class='iti__country iti__standard']"
    country_dropdown_xpath = "//div[@class='iti__selected-flag dropdown-toggle']"
    PhoneNo_SignIn_xpath = "//input[@id='adsasd']"
    SignIn_password_field = "//input[@id ='password']"
    eye_signIn_xpath = "//em[@class='fa pastogle3 fa-eye-slash']"
    Sign_xpath = "//div[@class='btnDiv text-center mb-5']"
    confirm_yes_btn = "//*[@class='swal2-confirm swal2-styled']"
    cancel_logout_btn = "//*[@class='swal2-cancel swal2-styled']"
    Hamburger_btn = "//button[@class='btn threedots-img']"
    Logout = "//label[contains(text(),'Logout')]"

    def __init__(self, driver):
        self.driver = driver

    def login_with_email(self):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(ReadConfig.getEmailid())
        self.driver.find_element(By.XPATH, self.SignIn_password_field).send_keys(ReadConfig.getPassword())
        self.driver.find_element(By.XPATH, self.Sign_xpath).click()
        time.sleep(2)

    def login_with_phone(self):
        self.driver.find_element(By.XPATH, self.country_dropdown_xpath).click()
        time.sleep(1)
        cont_name = self.driver.find_elements(By.XPATH, self.Country_name_xpath)
        # print(len(cname))
        for i in cont_name:
            # print(i.text)
            if i.text == ReadConfig.getCounty_name():
                i.click()
                break
        self.driver.find_element(By.XPATH, self.PhoneNo_SignIn_xpath).send_keys(ReadConfig.getPhone())
        self.driver.find_element(By.XPATH, self.SignIn_password_field).send_keys(ReadConfig.getPassword())
        self.driver.find_element(By.XPATH, self.Sign_xpath).click()
        time.sleep(2)

    def logout(self):
        self.driver.find_element(By.XPATH, self.Hamburger_btn).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.Logout).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.confirm_yes_btn).click()

