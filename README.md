from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import openpyxl

class Test_SauceDemo:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
    
    def teardown_method(self):
        self.driver.quit()
    
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_sauceDemo(self,username,password):
        
        self.waitForElementVisible((By.ID,"user-name"))
        userNameInput = self.driver.find_element(By.ID,"user-name")
        userNameInput.send_keys(username)

        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        passwordInput.send_keys(password)
        logInBtn = self.driver.find_element(By.ID,"login-button")
        logInBtn.click()

        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/span/select"))
        filtrele = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/span/select")
        filtrele.click()

        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/span/select/option[4]"))
        yuksekFiyat = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/span/select/option[4]")
        yuksekFiyat.click()

        self.waitForElementVisible((By.ID,"add-to-cart-sauce-labs-fleece-jacket"))
        addToCart = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket")
        addToCart.click()

        self.waitForElementVisible((By.ID,"add-to-cart-sauce-labs-backpack"))
        addToCart = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        addToCart.click()

        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[3]/a"))
        goToBasket = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[3]/a")
        goToBasket.click()

        self.waitForElementVisible((By.ID,"checkout"))
        checkout = self.driver.find_element(By.ID,"checkout")
        checkout.click()
        
        self.waitForElementVisible((By.ID,"first-name"))
        firstName = self.driver.find_element(By.ID,"first-name")
        firstName.send_keys("halit")
        lastName = self.driver.find_element(By.ID,"last-name")
        lastName.send_keys("kinik")
        postalCode = self.driver.find_element(By.ID,"postal-code")
        postalCode.send_keys("12345")

        continueBasket = self.driver.find_element(By.ID,"continue") 
        continueBasket.click()
        
        self.waitForElementVisible((By.ID,"finish"))
        finish = self.driver.find_element(By.ID,"finish")
        finish.click()

        self.waitForElementVisible((By.ID,"back-to-products"))
        backToHome = self.driver.find_element(By.ID,"back-to-products")
        backToHome.click()

        self.waitForElementVisible((By.ID,"react-burger-menu-btn"))
        menuBtn = self.driver.find_element(By.ID,"react-burger-menu-btn")
        menuBtn.click()

        self.waitForElementVisible((By.ID,"logout_sidebar_link"))
        logOut = self.driver.find_element(By.ID,"logout_sidebar_link")
        logOut.click()
        sleep(2)

    def waitForElementVisible(self,locator,timeout=15):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
