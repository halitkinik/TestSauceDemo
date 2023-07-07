from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
import openpyxl

class Test_SauceDemo:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()
    
    def getData():
        excelFile = openpyxl.load_workbook("data/success_login.xlsx") 
        selectedSheet = excelFile["Sayfa1"]

        totalRows = selectedSheet.max_row
        data = []
        for i in range(2,totalRows):
            username = selectedSheet.cell(i,1).value
            password = selectedSheet.cell(i,2).value
            tupleData = (username,password)
            data.append(tupleData)
        
        return data


    #başarılı giriş
    @pytest.mark.parametrize("username,password",getData())
    def test_valid_login(self,username,password):

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


    #username dogru password yanlıs olduğunda
    @pytest.mark.parametrize("username,password",[("standard_user","123456789")])
    def test_false_password(self,username,password):

        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        usernameInput.send_keys(username)

        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        passwordInput.send_keys(password)

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3") 
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"    
        sleep(2)
    

    #username yanlış password doğru olduğunda
    @pytest.mark.parametrize("username,password",[("standard_userr","secret_sauce")])
    def test_false_username(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        usernameInput.send_keys(username)

        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        passwordInput.send_keys(password)

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3") 
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"    
        sleep(2)
    
    #ikisi de yanlış olduğunda
    @pytest.mark.parametrize("username,password",[("standard_userrr","secret_sauceee")])
    def test_false_both(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        usernameInput.send_keys(username)

        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        passwordInput.send_keys(password)

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3") 
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"    
        sleep(2)


    #ikisi de boş geçildiğinde 
    @pytest.mark.parametrize("username,password",[("","")])
    def test_empty_username_password(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID,"user-name")
        usernameInput.send_keys(username)

        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID,"password")
        passwordInput.send_keys(password)

        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()

        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3") 
        assert errorMessage.text == "Epic sadface: Username is required"    
        sleep(2)

    def waitForElementVisible(self,locator,timeout=10):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))
    