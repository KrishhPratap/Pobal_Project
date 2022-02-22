from selenium.webdriver.common.by import By
import time


class Support:

    Message_field = "//textarea[@id ='Message']"
    support_submit_btn = "//div[@class = 'SubmitBtnDiv']//button[@class = 'btn supportBtn']"
    Hamburger_btn = "//img[@src='assets/auth-img/threedots.png']"
    support_btn = "//label[contains(text(),'Support')]"

    def __init__(self, driver):
        self.driver = driver

    def support_message(self):
        self.driver.find_element(By.XPATH, self.Hamburger_btn).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.support_btn).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Message_field).send_keys('Sample Message')
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.support_submit_btn).click()
        time.sleep(3)
