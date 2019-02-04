# =====================================================
#               Coded By IM_API
#     All Rights Reserved For (c) IM_API TEAM
#
#
#        Instagram Auto-Like And Comment
#
# =====================================================
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import comments
import hashtags
import settings
import getpass
import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class instagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    # "//a[@href'accounts/login']"
    # "//input[@name='username']"
    # "//input[@name='password']"
    def login(self):
        driver = self.driver
        driver.get('https://instagram.com')
        time.sleep(3)
        login_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
        login_button.click()
        time.sleep(2)
        username_elem = driver.find_element_by_xpath('//input[@name="username"]')
        username_elem.clear()
        username_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath('//input[@name="password"]')
        password_elem.clear()
        password_elem.send_keys(self.password)
        submit_btn = driver.find_element_by_xpath(
            '/html/body/span/section/main/div/article/div/div[1]/div/form/div[3]/button')
        submit_btn.click()

    def endOfProccess(self, text):
        self.driver.get(text)

    def addComment(self):
        driver_c = self.driver
        comment_inp = driver_c.find_element_by_xpath(
            '/html/body/span/section/main/div/div/article/div[2]/section[3]/div/form/textarea')
        comment_inp.click()
        comment_inp = driver_c.find_element_by_xpath(
            '/html/body/span/section/main/div/div/article/div[2]/section[3]/div/form/textarea')
        comment_inp.clear()
        comment = random.choice(comments.comments_array)
        comment_inp.send_keys(comment)
        comment_inp.send_keys(Keys.ENTER)
        return comment

    def like_photos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(3)
        # for i in range(1, 1):
        #   driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        #   time.sleep(3)
        # searching for pics
        time.sleep(3)
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        pic_hrefs = [href for href in pic_hrefs if '/p/' in href]
        print(hashtag + 'Photos: ' + str(len(pic_hrefs)))
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
            print(bcolors.OKBLUE + '======================================' + bcolors.ENDC)
            try:
                print(bcolors.WARNING + 'Trying To Like Post ...' + bcolors.ENDC)
                time.sleep(3)

                like_area = driver.find_element_by_class_name('fr66n')
                like_span = like_area.find_element_by_tag_name('span')
                if like_span.get_attribute('aria-label') == 'Unlike':
                    print(bcolors.HEADER + 'Post is Already liked' + bcolors.ENDC)
                else:
                    like_btn = driver.find_element_by_class_name('fr66n')
                    like_btn.click()
                    print(bcolors.OKGREEN + 'It must be liked now!' + bcolors.ENDC)
                    if random.choice(settings.send_comment) == 1:
                        print(self.addComment())
                        print(bcolors.OKGREEN + 'Commented On post! - Waiting until 18 secs ends' + bcolors.ENDC)
                    else:
                        print(bcolors.HEADER + 'It Wont Send Comment Cuz of Python Picked 0' + bcolors.ENDC)
                    time.sleep(18)
            except Exception as e:
                print(bcolors.FAIL + 'Problem With Like' + bcolors.ENDC)
                time.sleep(2)
            print(bcolors.OKBLUE + '======================================' + bcolors.ENDC)


os.system('clear')
username = input(bcolors.OKGREEN + 'Enter The Username : ' + bcolors.ENDC)
password = getpass.getpass(bcolors.OKGREEN + 'Enter The Password : ' + bcolors.ENDC)
repeat_time = int(input(bcolors.OKGREEN + 'How Many Times You Want Repeat all of like process again : ' + bcolors.ENDC))
x = 0
while x < repeat_time:
    account = instagramBot(username, password)
    account.login()
    time.sleep(3)
    [account.like_photos(tag) for tag in hashtags.hashtags]
    account.closeBrowser()
    print('Process Successfully Done!')
    x += 1
