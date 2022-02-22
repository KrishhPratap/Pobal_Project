from selenium.webdriver.common.by import By
import time


class Setting_Option:

    # Options
    setting_btn = "//label[contains(text(),'Settings')]"
    Change_pass_Btn = "//button[@class = 'btn change-btn']"
    cross_btn = "//span[@class='close fa-4x']"
    old_pass = "//input[@ng-reflect-name='old_password']"
    # eye_old_hide = "(//em)[1]"
    # eye_new_hide ="//em[@class ='fa pastogle5 fa-eye-slash']"
    # eye_conf_hide = "//em[@class ='fa pastogle6 fa-eye-slash']"
    # eye_old_pass_show = "//em[@class ='fa pastogle4 fa-eye']"
    # eye_new_pass = "//em[@class ='fa pastogle5 fa-eye']"
    # eye_conf_pass = "//em[@class ='fa pastogle6 fa-eye']"
    new_pass = "//input[@ng-reflect-name='password']"
    conf_pass = "//input[@ng-reflect-name='confirmPassword']"
    confm_btn = "//button[@class = 'btn submitBtn']"
    About_Us = "//button[@ng-reflect-router-link='/static-content/about-us']//img[@src = 'assets/auth-img/arrow1.png']"
    Privacy_Policy = "//button[@ng-reflect-router-link='/static-content/privacy-policy']//img[@src = 'assets/auth-img/arrow1.png']"
    TC = "//button[@ng-reflect-router-link='/static-content/term-and-condi']//img[@src = 'assets/auth-img/arrow1.png']"
    Faqs = "//button[@ng-reflect-router-link='/static-content/faq']//img[@src = 'assets/auth-img/arrow1.png']"
    Hamburger_btn = "//button[@class='btn threedots-img']//img[@src='assets/auth-img/threedots.png']"
    Logout = "//label[contains(text(),'Logout')]"
    back_button = "//img[@src='assets/auth-img/Group 154.png']"

    def __init__(self, driver):
        self.driver = driver

    def changePass(self):
        self.driver.find_element(By.XPATH, self.Hamburger_btn).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.setting_btn).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Change_pass_Btn).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.cross_btn).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Change_pass_Btn).click()
        time.sleep(2)
        # old Password Field
        self.driver.find_element(By.XPATH, self.old_pass).send_keys('Qwerty@12345')
        time.sleep(5)
        # self.driver.find_element(By.XPATH, self.eye_old_hide).click()
        # time.sleep(5)
        # self.driver.find_element(By.CSS_SELECTOR, self.eye_old_hide).click()
        # time.sleep(30)
        # # new Password Field
        self.driver.find_element(By.XPATH, self.new_pass).send_keys('Qwerty@123')
        time.sleep(1)
        # self.driver.find_element(By.XPATH, self.eye_new_hide).click()
        # time.sleep(5)
        # self.driver.find_element(By.XPATH, self.eye_new_hide).click()
        # time.sleep(30)
        # # Confirm Password
        self.driver.find_element(By.XPATH, self.conf_pass).send_keys('Qwerty@123')
        time.sleep(1)
        # self.driver.find_element(By.XPATH, self.eye_conf_hide).click()
        # time.sleep(1)
        # self.driver.find_element(By.XPATH, self.eye_conf_hide).click()
        # time.sleep(1)
        # # Confirm button
        self.driver.find_element(By.XPATH, self.confm_btn).click()
        time.sleep(1)

    def about_us(self):
        self.driver.find_element(By.XPATH, self.About_Us).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.back_button).click()
        time.sleep(2)

    def privacy_policy(self):
        self.driver.find_element(By.XPATH, self.Privacy_Policy).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.back_button).click()
        time.sleep(2)

    def terms_condition(self):
        self.driver.find_element(By.XPATH, self.TC).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.back_button).click()
        time.sleep(2)

    def faqs(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Faqs).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.back_button).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,-100000)")
        time.sleep(2)