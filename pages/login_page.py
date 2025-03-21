# pages/login_page.py
import time
import toml # type: ignore
import random
import datetime
import configparser
from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    
    # web element
    username_field = (By.XPATH, "//*[@id='exampleInputEmail1']")
    password_field = ("id", "password_login")
    login_button = ("id", "btnLogin")
    client_locator = (By.XPATH, "//*[@id='Menu1']/li[2]/a")
    select_client_locator  = (By.XPATH, "//*[@id='Menu1']/li[2]/ul/li[2]/a")
    add_client_locator     = (By.XPATH, "//*[@id='addCustomer']")
    gender_locator         = (By.XPATH, "//*[@id='gender']/option[2]")
    firstn_locator         = (By.XPATH, "//*[@id='acc_first_name']")
    lastn_locator          = (By.XPATH, "//*[@id='acc_last_name']")
    email_locator          = (By.XPATH, "//*[@id='email']")
    passw_locator          = (By.XPATH, "//*[@id='password']")
    mobile_locator         = (By.XPATH, "//select[@name='mobile_code']/option[@value='61']")
    mobile_text            = (By.XPATH, "//*[@id='mobile']")
    country_locator        = (By.XPATH, "//*[@id='country']/option[24]")
    national_locator       = (By.XPATH, "//*[@id='ib_Nationality']/option[4]")
    account_type           = (By.XPATH, "//*[@id='mt4_account_type']/option[2]")
    currency_locator       = (By.XPATH, "//*[@id='currency']/option[2]")
    identif_locator        = (By.XPATH, "//*[@id='acc_id_type']/option[3]")
    idnumber_locator       = (By.XPATH, "//*[@id='acc_id_num']")
    submint_locator        = (By.XPATH, "//*[@class = 'pull-right']/button[1]")

    cli_name_locator       = (By.XPATH, "//input[contains(@class, 'bootstrap-table-filter-control-show_name')]")
    search_locator         = (By.XPATH, "//button[@id='query']")
    userid_locator         = (By.XPATH, "//*[@id='table']/tbody/tr[1]/td[2]")
    task_locator           = (By.XPATH, "//*[@id='Menu1']/li[5]/a")
    account_audit_locator  = (By.XPATH, "//*[@id='Menu1']/li[5]/ul/li[6]/a")
    search_option_locator  = (By.XPATH, "//*[@id='searchType']/div")
    search_userid_locator  = (By.XPATH, "//*[@id='toolbar']/div[9]/ul/li[5]/a")
    enter_userid_locator   = (By.XPATH, "//input[@id='userQuery']")
    
    # userinfo
    config = configparser.ConfigParser()
    config.read('/Users/nick.chang/HytechcWeb/pytest.ini')
    user = config['userinfo']['username']
    pw   = config['userinfo']['password']
    cp_pw= config["userinfo"]['cp_pws']
   
    # other
    current_time = datetime.datetime.now().strftime("%m%d_%H%M")
    
    def __init__(self,driver):
        self.driver =driver

    def enter_username(self):
        self.find_element(*self.username_field).send_keys(self.user)

    def enter_password(self):
        self.find_element(*self.password_field).send_keys(self.pw)

    def click_login(self):
        self.find_element(*self.login_button).click()

    def click_client(self):
        self.find_element(*self.client_locator).click()
    
    def select_client(self):
        self.find_element(*self.select_client_locator).click()

    def add_client(self):
        time.sleep(0.5)
        self.find_element(*self.add_client_locator).click()
    
    def gender_field(self):
        time.sleep(0.5)
        self.find_element(*self.gender_locator).click()

    def first_name(self):
        time.sleep(0.5)
        first_name = "testcrm" + self.current_time
        self.find_element(*self.firstn_locator).send_keys(first_name)
        print ("account:",first_name)
        # return first_name
        
    def last_name(self):
        time.sleep(0.5)
        last_name = "testcrm" + self.current_time
        self.find_element(*self.lastn_locator).send_keys(last_name)

    def email_field(self):
        time.sleep(0.5)
        email = "testcrm" + self.current_time + "@mailinator.com"
        self.find_element(*self.email_locator).send_keys(email)
        print ("email:" , email)
        return email

    def passw_filed(self):
        self.find_element(*self.passw_locator).send_keys(self.cp_pw)

    def mobile_field(self):
        nb = ''.join([str(random.randint(1, 10)) for _ in range(4)])
        ph_number = '0000' + nb
        time.sleep(0.5)
        self.find_element(*self.mobile_locator).click()
        self.find_element(*self.mobile_text).send_keys(ph_number)
    
    def country_field(self):
        time.sleep(0.5)
        self.find_element(*self.country_locator).click()

    def national_field(self):
        time.sleep(0.5)
        self.find_element(*self.national_locator).click()

    def account_field(self):
        time.sleep(0.5)
        self.find_element(*self.account_type).click()
    
    def currency_field(self):
        time.sleep(0.5)
        self.find_element(*self.currency_locator).click()
    
    def identification_field(self):
        time.sleep(0.5)
        self.find_element(*self.identif_locator).click()

    def idnumber_field(self):
        time.sleep(0.5)
        nb = ''.join([str(random.randint(1, 10)) for _ in range(11)])
        self.find_element(*self.idnumber_locator).send_keys(nb)
    
    def click_submit(self):
        time.sleep(0.5)
        self.find_element(*self.submint_locator).click()
        # self.find_element(*self.search_locator).click()
        # self.find_element(*self.cli_name_locator).click()
        
        
    def search_button(self):
        time.sleep(1)
        self.wait_for_element(*self.search_locator).click()
        # self.find_element(*self.search_locator).click()

    def userid_value(self):
        time.sleep(1)
        userID = self.find_element(*self.userid_locator).text
        print ("userID:", userID)
        return userID
    
    def click_task(self):
        time.sleep(0.5)
        self.find_element(*self.task_locator).click()

    def click_account_audit(self):
        time.sleep(0.5)
        self.find_element(*self.account_audit_locator).click()

    def click_search_option(self):
        time.sleep(1.5)
        self.find_element(*self.search_option_locator).click()
        time.sleep(0.5)
        self.find_element(*self.search_userid_locator).click()
    
    def input_userid(self):
        time.sleep(0.5)
        userid = self.userid_value()
        print (userid)
        self.find_element(*self.enter_userid_locator).send_keys(userid)
       
        