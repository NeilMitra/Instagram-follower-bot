from selenium import webdriver
from time import sleep



class VjayaBot:
    def __init__(self, username, pw, whoeverthetargetuseris): ######### CHANGE HERE
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/input")\
            .send_keys(whoeverthetargetuseris) ########## CHANGE HERE

        sleep(2)
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[2]")\
            .click()
        sleep(1)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        sleep(1)
        #self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[3]/button")\
           #.click()
        # THIS IS THE START OF THE SCROLLING THING
        sleep(3)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        n = 150 #### CHANGE HERE: change this depending on the amount of users the target user is following. Example: a person is following 200 users - then change this value to 200
        while n >= 1:
            sleep(3)
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li[" +str(n)+ "]/div/div[2]/button")\
                .click()
            sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/button[1]")\
                .click()
            n -= 2
            #sleep(3)
            #self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li[" +str(n-1)+ "]/div/div[2]/button")\
             #   .click()
            #sleep(1)
            #self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/button[1]")\
             #  .click()

my_bot = VjayaBot('yourusername', 'yourpassword', 'the user that you want - in order to follow the people that they are following') #### CHANGE HERE