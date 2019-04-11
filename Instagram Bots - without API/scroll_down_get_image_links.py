# this app is an instagram crawler that uses your username and password to log In and then it goes to the target username that you give to the program.
# Then it scrolls down and prints the links of all images.
# The target username is sepehr.akbarzadeh by default but you can change it.
# Developer : Shahriar Hashemi
# LinkedIn page : https://www.linkedin.com/in/shahriar-hashemi/ 
# Email : shriar.ha@gmail.com

from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

class App:
    def __init__(self,username="Enter your username here",password="Enter your password here",target_username="sepehr.akbarzadeh"):
        self.username = username
        self.password = password
        self.target_username = target_username
        self.driver = webdriver.Chrome("/Users/Shahriar/Desktop/Selenium and BS projects/chromedriver.exe") #This is the path to webdriver in my PC ,you should change it and give the path of where your webdriver is located.
        self.main_url = "https://www.instagram.com"
        self.driver.get(self.main_url)
        sleep(5)
        self.log_in()
        self.close_notification()
        self.go_to_target_profile()
        sleep(3)
        self.scroll_down()
        sleep(15)
        self.get_images_links()

    def close_notification(self):
        try: 
            sleep(3)
            close_noti_btn = self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")
            close_noti_btn.click()
            sleep(2)
        except:
            pass

    def get_images_links(self): #only gives 40 links beacuse of instagram limits
        soup = BeautifulSoup(self.driver.page_source, "lxml")
        all_images = soup.find_all("img")
        for image in all_images:
            print(image["src"])

    def go_to_target_profile(self):
        target_profile_url = self.main_url + "/" + self.target_username + "/"
        self.driver.get(target_profile_url)

    def scroll_down(self):
        number_of_posts = self.driver.find_element_by_xpath("//span[@class='g47SY ']")
        number_of_posts = str(number_of_posts.text).replace(",","")
        number_of_posts = int(number_of_posts)
        if number_of_posts > 12:
            number_of_scrolls = (number_of_posts / 12)+3
            for i in range(int(number_of_scrolls)):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(2)
        
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