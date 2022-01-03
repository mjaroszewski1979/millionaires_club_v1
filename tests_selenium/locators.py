from selenium.webdriver.common.by import By

class HomePageLocators(object):

   
    ABOUT_LINK = (By.CLASS_NAME, 'about-link')
    COUNTRY = (By.NAME, 'country')
    SUBMIT = (By.CLASS_NAME, 'submit-button')
    RESULT = (By.CLASS_NAME, 'cpi-result')
    ERROR_MSG = (By.CLASS_NAME, 'error-msg')
   

class AboutPageLocators(object):

    COUNTRIES_LINK = (By.CLASS_NAME, 'countries-link')

class CountriesPageLocators(object):

    G5_LINK = (By.CLASS_NAME, 'g5-link')
    COUNTRIES = (By.CLASS_NAME, 'countries')
    HOME_LINK = (By.CLASS_NAME, 'home-link')



