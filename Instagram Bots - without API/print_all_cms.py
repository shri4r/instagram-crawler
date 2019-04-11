# this app is an instagram crawler that uses your username and password to log In and then it goes to the target username that you give to the program.
# Then it clicks on one post and prints all the comments of that post.
# The target username is google by default but you can change it.
# Developer : Shahriar Hashemi
# LinkedIn page : https://www.linkedin.com/in/shahriar-hashemi/ 
# Email : shriar.ha@gmail.com

from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

class App:
    def __init__(self,username="Enter your username here",password="Enter your password here",target_username="google"):
        self.username = username
        self.password = password
        self.target_username = target_username
        self.driver = webdriver.Chrome("/Users/Shahriar/Desktop/Selenium and BS projects/chromedriver.exe") #This is the path to webdriver in my PC ,you should change it and give the path of where your webdriver is located.
        self.main_url = "https://www.instagram.com"
        self.driver.get(self.main_url)
        sleep(8)
        self.log_in()
        self.close_notification()
        self.go_to_target_profile()
        sleep(3)
        self.click_post()
        sleep(5)
        self.load_more_comments()
        sleep(15)
        self.get_cms()

    def click_post(self):
        post_url = self.driver.find_element_by_xpath("//a[@href='/p/Bumq_SSB0z_/']") # You should give the href of the post you want to be clicked. (This href is for a post in google's instagram page)
        post_url.click()

    def load_more_comments(self):
        more_cm_button = self.driver.find_element_by_xpath("//li/div[@style='min-height: 40px;']/button")
        while True:
            try:
                more_cm_button = self.driver.find_element_by_xpath("//li/div[@style='min-height: 40px;']/button")
                more_cm_button.click()
                sleep(2)
            except:
                break

    def close_notification(self):
        try: 
            sleep(3)
            close_noti_btn = self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")
            close_noti_btn.click()
            sleep(2)
        except:
            pass

    def get_cms(self): 
        soup = BeautifulSoup(self.driver.page_source, "lxml")
        all_cm_containers = soup.find_all("h3",attrs={"class":"_6lAjh"})
        for item in all_cm_containers:
            print(item.next_sibling.text)

    def go_to_target_profile(self):
        target_profile_url = self.main_url + "/" + self.target_username + "/"
        self.driver.get(target_profile_url)
        
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