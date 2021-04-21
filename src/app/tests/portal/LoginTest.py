import unittest
from app.configuration.Configuration import Configuration
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LoginTest(unittest.TestCase):
    '''
    def test_login_mobile(self):
        driver.get(configurationSingleton.mobile_url+'/PA/')
        print(configurationSingleton.portal_url)
        usernameField = driver.find_element_by_name("main:username_input")
        usernameField.clear()
        usernameField.send_keys("sis")
        passwordField = driver.find_element_by_name("main:password_input")
        passwordField.clear()
        passwordField.send_keys("123")
        buttonLogin = driver.find_element_by_name("main:loginBtn")
        buttonLogin.click()

        self.assertEqual(driver.title, 'Portal Aduanero')
        print("El login Mobile funciona correctamente")
    '''

    def test_login_portal(self):
        config = Configuration()
        config.driver.get(config.portal_url+'/')
        buttonDialogo = config.driver.find_element_by_name("principal:login")
        buttonDialogo.click()
        config.driver.implicitly_wait(2000)
        usernameField = config.driver.find_element_by_name("username")
        # usernameField.clear()
        usernameField.send_keys("sis")
        passwordField = config.driver.find_element_by_name("password")
        # passwordField.clear()
        passwordField.send_keys("123")
        buttonLogin = config.driver.find_element_by_name("j_idt145")
        buttonLogin.click()
        self.assertEqual(config.driver.title, 'Portal Aduanero')
