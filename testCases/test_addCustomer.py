import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.addcustomer = AddCustomer(self.driver)
        self.addcustomer.clickOnCustomersMenu()
        time.sleep(3)
        self.addcustomer.clickOnCustomersMenuItem()
        time.sleep(5)
        self.addcustomer.clickOnAddnew()

        self.logger.info("************* Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        self.addcustomer.setEmail(self.email)
        self.addcustomer.setPassword("test123")
        self.addcustomer.setFirstName("Pavan")
        self.addcustomer.setLastName("Kumar")
        self.addcustomer.setGender("Male")
        self.addcustomer.setDob("7/05/1985")  # Format: D / MM / YYY
        self.addcustomer.setCompanyName("busyQA")
        self.addcustomer.setCustomerRoles("Guests")
        self.addcustomer.setManagerOfVendor("Vendor 2")


        self.addcustomer.setAdminContent("This is for testing.........")
        self.addcustomer.clickOnSave()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))