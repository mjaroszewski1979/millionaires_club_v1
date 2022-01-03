from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from locators import AboutPageLocators, CountriesPageLocators, HomePageLocators



class BasePage(object):


    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_clear(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()

    def do_send_keys(self, locator, text):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_elements(self, locator):
        elements = W(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def get_element_text(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def do_submit(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()


class HomePage(BasePage):

    def is_title_matches(self):
        return "Millionaires Club - Home" in self.driver.title

    def is_about_link_works(self):
        self.do_click(HomePageLocators.ABOUT_LINK)
        return "Millionaires Club - About" in self.driver.title

    def is_form_works_given_vaild_data(self):
        self.do_clear(HomePageLocators.COUNTRY)
        self.do_send_keys(HomePageLocators.COUNTRY, 'poland')
        self.do_click(HomePageLocators.SUBMIT)
        cpi_result = self.get_element_text(HomePageLocators.RESULT)
        return 'THE LATEST CPI READING FOR POLAND IS' in cpi_result

    def is_form_works_given_invaild_data(self):
        self.do_clear(HomePageLocators.COUNTRY)
        self.do_send_keys(HomePageLocators.COUNTRY, 'somecountry')
        self.do_click(HomePageLocators.SUBMIT)
        error_msg = self.get_element_text(HomePageLocators.ERROR_MSG)
        return 'PLEASE TRY A DIFFERENT COUNTRY!' in error_msg





class AboutPage(BasePage):

    def is_title_matches(self):
        return "Millionaires Club - About" in self.driver.title

    def is_countries_link_works(self):
        self.do_click(AboutPageLocators.COUNTRIES_LINK)
        return "Millionaires Club - G5 Members" in self.driver.title

class CountriesPage(BasePage):

    def is_title_matches(self):
        return "Millionaires Club - G5 Members" in self.driver.title

    def is_g5_link_works(self):
        self.do_click(CountriesPageLocators.G5_LINK)
        return "Millionaires Club - G5 CPI" in self.driver.title

    def is_g5_countries_cpi_is_displayed(self):
        countries = self.get_elements(CountriesPageLocators.COUNTRIES)
        return (countries[0].text) == 'CHINA'

    def is_home_link_works(self):
        self.do_click(CountriesPageLocators.HOME_LINK)
        return "Millionaires Club - Home" in self.driver.title











   