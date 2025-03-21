# pages/base_page.py
import time
import toml # type: ignore
from typing import List
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc) -> WebElement :
        """found HTML Element
        :param loc:
        :return:
        :rtype: WebElement
        :raises WebDriverException can not found element
        """
        time.sleep(0.1)
        WebDriverWait(self.driver, 90).until(EC.element_to_be_clickable(loc))
        # WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(loc))
        return self.driver.find_element(*loc)
    
    def find_elements(self, *loc) -> List[WebElement] :
        """found HTML Element
        :param loc:
        :return:
        :rtype: List[WebElement]
        :raises WebDriverException can not found element
        """
        time.sleep(0.1)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
        return self.driver.find_elements(*loc)

    def wait_for_element(self, *locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print(f"{self} page can not found {loc} element")

    def switch_frame(self, loc):
        self.driver.switch_to.frame(loc)
    
    def switch_to_frame(self):
        self.driver.switch_to.frame(0)
    
    def move_mouse(self, loc):
        
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(loc))
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element(*loc)).click().perform()



        