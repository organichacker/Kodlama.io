from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class SaucedemoTest:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.saucedemo.com/")

    
    def bos(self):
        self.driver.find_element(By.ID, 'login-button').click()
        hataMesaji = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3').text
        print(hataMesaji)
    
    def sadeceSifre(self):
        self.driver.find_element(By.ID, "user-name").send_keys("username")
        self.driver.find_element(By.ID, "login-button").click() 
        hataMesaji = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3').text
        print(hataMesaji)

    def ikisideYanlis(self):
        self.driver.find_element(By.ID, 'user-name').send_keys('locked_out_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()
        hataMesaji = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3').text
        print(hataMesaji)

    def giris(self):
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()
    
    


test = SaucedemoTest()
test.bos()
test.sadeceSifre()
test.ikisideYanlis()
test.giris()
