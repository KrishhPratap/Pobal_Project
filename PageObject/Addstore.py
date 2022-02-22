import time
import unittest

import pytest as pytest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Createstore:

    # Add Store
    My_store_btn = "//*[@id='sideMenu']/app-side-menu/nav/ul/li[3]/a/label"
    Add_store_btn = "//button[@class='btn addBtn']"
    Store_name = "//*[@formcontrolname='name']"
    Store_Email_Address = "//*[@placeholder='Email']"
    Store_emailid = "//*[@id='content']/div[2]/app-edit-profile/div[3]/div/form/div[1]/div[2]/div/input"
    Store_URL = "//*[@formcontrolname='website_url']"
    Store_Phone = "//*[@placeholder='Phone number']"
    Deal_Store_Address = "//*[@formcontrolname='address']"
    Store_City_name = "//*[@formcontrolname='city']"
    Store_State_name = "//*[@formcontrolname='state']"
    Store_Country_name = "//*[@formcontrolname='country']"
    Store_Zip_code = "//*[@formcontrolname='zip']"
    Store_Description = "//*[@formcontrolname='description']"
    Store_Upload_Image = "//*[@placeholder='No File Chosen']"
    Hamburger_btn = "//button[@class='btn threedots-img']//img[@src='assets/auth-img/threedots.png']"
    Save_btn = "//button[@class='btn btn-primary btnColor save ng-star-inserted']"
    Close_btn = "//*[@class='btn btn-primary btnColor cancel']"
    cdropdown = "//div[@class='iti__selected-flag dropdown-toggle']"
    coption ="//span[@class='iti__country-name']"
    my_deal = "//label[contains(text(),'My Deals')]"

    def __init__(self, driver):
        self.driver = driver


    def add_store(self, sname, semail, sURL, sphone, saddress, scity, sstate, scountry, szip, suploadImage, sdescription):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.Hamburger_btn).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.My_store_btn).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.Add_store_btn).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.Store_name).send_keys(sname)
        time.sleep(1)
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.Store_emailid)))
            element.send_keys(semail)
        except TimeoutException:
            print ("Loading took too much time!")

        self.driver.find_element(By.XPATH, self.Store_URL).send_keys(sURL)
        self.driver.find_element(By.XPATH, self.Store_Phone).send_keys(sphone)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.Deal_Store_Address).send_keys(saddress)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.Store_City_name).send_keys(scity)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.Store_State_name).send_keys(sstate)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.Store_Country_name).send_keys(scountry)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.Store_Zip_code).send_keys(szip)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.Store_Upload_Image).send_keys(suploadImage)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Store_Description).send_keys(sdescription)
        # try:
        #     save_btn = WebDriverWait(self.driver, 15).until(
        #         EC.element_to_be_clickable((By.XPATH, self.Save_btn)))
        #     save_btn.click()
        # except TimeoutException:
        #     print ("Loading took too much time!")
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(1)
        deals_done_btn = self.driver.find_element(By.XPATH, self.Save_btn).click()
        deals_closed_btn = self.driver.find_element(By.XPATH, self.Close_btn).click()
        if deals_done_btn.is_enabled():
            deals_done_btn.click()
            time.sleep(3)
        else:
            deals_closed_btn.click()
            time.sleep(3)

        self.driver.find_element(By.XPATH, self.Hamburger_btn).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.my_deal).click()
        time.sleep(1)

