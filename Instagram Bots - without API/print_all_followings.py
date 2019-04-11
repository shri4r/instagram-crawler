# This app is an instagram crawler that uses your username and password to log In and then it goes to your profile page and scrolls your following list
# and finally it prints all the users you follow.
# You can change the sleep time . If your internet is slow , use big numbers like the default numbers that I used. 
# Developer : Shahriar Hashemi
# LinkedIn page : https://www.linkedin.com/in/shahriar-hashemi/ 
# Email : shriar.ha@gmail.com

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class App:
    def __init__(self,username="Enter your username here",password="Enter your password here"):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome("/Users/Shahriar/Desktop/Selenium and BS projects/chromedriver.exe") #This is the path to webdriver in my PC ,you should change it and give the path of where your webdriver is located.
        self.main_url = "https://www.instagram.com"
        self.driver.get(self.main_url)
        sleep(5)
        self.log_in()
        self.close_notification()
        self.go_to_profile()
        sleep(2)
        self.click_on_following()
        self.scroll_down()
        sleep(0.5)
        self.make_following_list()
        self.driver.close()

    def go_to_profile(self):
        profile_page = self.main_url + "/" + self.username + "/"
        self.driver.get(profile_page)

    def make_following_list(self):
        followings = self.driver.find_elements_by_xpath("//div[@class='d7ByH']/a")
        print([user.get_attribute("title") for user in followings])
    
    def scroll_down(self):
        number_of_following = self.driver.find_element_by_xpath("//a[@href='/shriar.ha/following/']/span").get_attribute("innerHTML")
        number_of_following = int(number_of_following)
        b = 5
        try:
            while True:
                b = str(b)
                self.driver.execute_script("arguments[0].scrollIntoView()",self.driver.find_element_by_xpath("//ul[contains(@class, 'jSC57')]//li["+b+"]"))
                b = int(b)
                b += 5
                sleep(1.5)
        except:
            pass

    def click_on_following(self):
        following_button = self.driver.find_element_by_xpath("//a[@href='/shriar.ha/following/']")
        following_button.click()
        sleep(5)

    def close_notification(self):
        try: 
            sleep(2)
            close_noti_btn = self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")
            close_noti_btn.click()
            sleep(2)
        except:
            pass

    def log_in(self):
        login_button = self.driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        sleep(5)
        username_input = self.driver.find_element_by_xpath("//input[@name='username']")
        username_input.send_keys(self.username)
        password_input = self.driver.find_element_by_xpath("//input[@name='password']")
        password_input.send_keys(self.password)
        password_input.submit()

if __name__ == "__main__":
    app = App()