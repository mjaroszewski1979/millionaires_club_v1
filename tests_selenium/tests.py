from selenium import webdriver
import page
import unittest


class TestBase(unittest.TestCase):


    def setUp(self):
        self.driver =  webdriver.Chrome('chromedriver.exe')
        self.driver.set_window_size(1920, 1080)


    def tearDown(self):
        self.driver.close()


class SeleniumTest(TestBase):
        
    def test_home_page(self):
        self.driver.get('http://127.0.0.1:8000')
        home_page = page.HomePage(self.driver)
        assert home_page.is_title_matches()
        assert home_page.is_form_works_given_invaild_data()
        assert home_page.is_form_works_given_vaild_data()
        assert home_page.is_about_link_works()

    def test_about_page(self):
        self.driver.get('http://127.0.0.1:8000/about')
        about_page = page.AboutPage(self.driver)
        assert about_page.is_title_matches()
        assert about_page.is_countries_link_works()

    def test_countries_page(self):
        self.driver.get('http://127.0.0.1:8000/countries')
        countries_page = page.CountriesPage(self.driver)
        assert countries_page.is_title_matches()
        assert countries_page.is_g5_link_works()
        assert countries_page.is_g5_countries_cpi_is_displayed()
        assert countries_page.is_home_link_works()


        
if __name__ == '__main__':
    unittest.main()




        