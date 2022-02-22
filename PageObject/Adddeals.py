from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Createdeal:

    # Add deal flow
    Add_Deal_btn = "//button[@class ='btn addBtn']"
    Deal_name_field = "//*[@placeholder='Deal Name']"
    Status_dropdown = "//*[@formcontrolname='status']"
    Deal_category_dropdown = "//*[@formcontrolname='category']"
    Recurrence_dropdown = "//*[@formcontrolname='recurrence']"
    Usage_Limit_dropdown = "//*[@formcontrolname='usage_limit']"
    Start_datetime_field = "//*[@formcontrolname='start_date_time']"
    End_datetime_field = "//*[@formcontrolname='end_date_time']"
    Save_btn_Add_deals = "//button[@class ='btn btn-primary btnColor save ng-star-inserted']"
    Description_field = "//*[@formcontrolname='description']"
    Deal_Add_store_btn_ = "//div[@class ='form-group']//button[@class ='btn addBtn']"
    Set_store_dropdown = "//*[@class ='ng-input']"
    str_option = "//span[@class= 'ng-option-label ng-star-inserted']"
    outside = "//div[@class = 'center-item']"
    Cross_icon = "//img[@src='assets/auth-img/cross.png']"
    Close_btn = "//button[@class='btn btn-primary btnColor cancel']"
    more_options = "(//img[@src='assets/auth-img/Group.png'])[3]"
    edit_btn = "(//a[@class = 'cursor-pointer']//img[@src='assets/auth-img/pen.png'])[3]"
    delete_btn = "(//a[@class = 'cursor-pointer']//img[@src='assets/auth-img/bin.png'])[3]"
    my_deal = "//label[contains(text(),'My Deals')]"
    Hamburger_btn = "//button[@class='btn threedots-img']//img[@src='assets/auth-img/threedots.png']"
    # edit deals screens
    editdeals_back_btn = "//button[@class ='btn-circle']//img[@src = 'assets/auth-img/arrow.png']"
    update_button = "//button[@class ='btn btn-primary btnColor save ng-star-inserted']"



    # delete confirmation prompt
    delete_bttn ="//button[@class ='swal2-confirm swal2-styled']"
    cancel_bttn = "//button[@class ='swal2-cancel swal2-styled']"


    def __init__(self, driver):
        self.driver = driver

    # def add_deals_error(self):
    #     self.driver.find_element(By.XPATH, self.Add_Deal_btn).click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, self.Deal_name_field).click()
    #     self.driver.find_element(By.XPATH, self.outside).click()

     # To handle multiple dropdowns
    def select_values(self, element, values):
        select = Select(element)
        select.select_by_visible_text(values)

    def create_deals(self):
        self.driver.find_element(By.XPATH, self.Add_Deal_btn).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Deal_name_field).send_keys("Cookies")
        time.sleep(3)

        status = self.driver.find_element(By.XPATH, self.Status_dropdown)
        deal = self.driver.find_element(By.XPATH, self.Deal_category_dropdown)
        Recurr = self.driver.find_element(By.XPATH, self.Recurrence_dropdown)
        Usage = self.driver.find_element(By.XPATH, self.Usage_Limit_dropdown)

        # dropdowns
        self.select_values(status, 'Inactive')
        self.select_values(deal, 'Food')
        self.select_values(Recurr, 'Weekly')
        self.select_values(Usage, 'Daily')

        # other way to select from dropdown is Usage Limit
        # Usage = self.driver.find_element(By.XPATH, self.Usage_Limit_dropdown)
        # Usage_option = Select(Usage)
        # Usage_option.select_by_visible_text("Daily")

        # Start Date-Time
        self.driver.find_element(By.XPATH, self.Start_datetime_field).send_keys("01/30/2022, 6:00 AM")
        # End Date-Time
        self.driver.find_element(By.XPATH, self.End_datetime_field).clear()
        self.driver.find_element(By.XPATH, self.End_datetime_field).send_keys("6/3/2022, 6:00 AM")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Description_field).send_keys("Find best restaurants in Delhi offering discounts on food & drinks, check out menu, reviews and also book a table through dineout for free.")
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Deal_Add_store_btn_).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(3)

        self.driver.find_element(By.XPATH, self.Set_store_dropdown).click()
        time.sleep(3)
        Store_option = self.driver.find_elements(By.XPATH, self.str_option)
        for options in Store_option:
            print(options.text)
            if options.text == 'Mini-Mart.':
                options.click()
                break
        time.sleep(3)
        done_btn = self.driver.find_element(By.XPATH, self.Save_btn_Add_deals)
        close_btn = self.driver.find_element(By.XPATH, self.Close_btn)

        if done_btn.is_enabled():
            print(done_btn)
            done_btn.click()
        else:
            close_btn.click()

        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,-100000)")  # scroll from down to top
        time.sleep(3)

    def editdeals(self, udealsname, ustart_date, uend_date, udescription):
        self.driver.find_element(By.XPATH, self.Hamburger_btn).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.my_deal).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.more_options).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.edit_btn).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Deal_name_field).clear()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Deal_name_field).send_keys(udealsname)
        time.sleep(3)

        status = self.driver.find_element(By.XPATH, self.Status_dropdown)
        deal = self.driver.find_element(By.XPATH, self.Deal_category_dropdown)
        Recurr = self.driver.find_element(By.XPATH, self.Recurrence_dropdown)
        Usage = self.driver.find_element(By.XPATH, self.Usage_Limit_dropdown)

        # dropdowns
        self.select_values(status, 'Active')
        self.select_values(deal, 'Drinks')
        self.select_values(Recurr, 'Daily')
        self.select_values(Usage, 'Unlimited')

        # update Start Date-Time
        self.driver.find_element(By.XPATH, self.Start_datetime_field).clear()
        self.driver.find_element(By.XPATH, self.Start_datetime_field).send_keys(ustart_date)
        # update End Date-Time
        self.driver.find_element(By.XPATH, self.End_datetime_field).clear()
        self.driver.find_element(By.XPATH, self.End_datetime_field).send_keys(uend_date)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Description_field).clear()
        self.driver.find_element(By.XPATH, self.Description_field).send_keys(udescription)
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(3)
        #update button
        self.driver.find_element(By.XPATH, self.Set_store_dropdown).click()
        time.sleep(3)
        Store_option = self.driver.find_elements(By.XPATH, self.str_option)
        for options in Store_option:
            print(options.text)
            if options.text == 'Cartmax':
                options.click()
                break
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(3)
        update_btn = self.driver.find_element(By.XPATH, self.update_button)
        close_btn1 = self.driver.find_element(By.XPATH, self.Close_btn)

        if update_btn.is_enabled():
            try:
                assert update_btn.click()
            except AssertionError:
                print("Assertion failed. Element not clickable")

        else:
            close_btn1.click()
        time.sleep(3)


    def delete_deals(self):
        self.driver.execute_script("window.scrollBy(0,-100000)")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Hamburger_btn).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.my_deal).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.more_options).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.delete_btn).click()
        time.sleep(3)
        delete_button = self.driver.find_element(By.XPATH, self.delete_bttn)
        cancel_btn = self.driver.find_element(By.XPATH, self.cancel_bttn).click()
        if delete_button.is_enabled():
            delete_button.click()
            time.sleep(3)

        else:
            cancel_btn.click()
            time.sleep(3)











