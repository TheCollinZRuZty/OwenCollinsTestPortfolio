import os, sys, unittest, time
from webbrowser import BaseBrowser
from selenium import webdriver 
import config as cfg
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class test_twitter_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global browser
        chrome_options= Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--diasble-dev-shm-usage")
        chrome_options.add_argument("window-size=1920,1080")
        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.get(cfg.url)
    
    @classmethod
    def tearDownClass(cls):
        browser.quit
    
    def tearDown(self):
        browser.switch_to.default_content()

    # def test_twitter_login_001(self):
    #     """Verify Twitter logo appears as expected. 
    #     """
    #     wait=WebDriverWait(browser,30)
    #     wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/svg/g/path')))
    #     self.assertTrue(browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/svg/g/path'),'The Twitter logo does not appear as expected.')
        
    def test_twitter_login_002(self):
        """Verify "Happening now" Label appears.
        """
        wait=WebDriverWait(browser,30)
        wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Happening now')]")))
        self.assertTrue(browser.find_element_by_xpath("//span[contains(text(),'Happening now')]"),'The "Happening now" Label does not appear as expected.')

    def test_twitter_login_003(self):
        """Verify "Join Twitter today." Label appears.
        """
        wait=WebDriverWait(browser,30)
        wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Join Twitter today.')]")))
        self.assertTrue(browser.find_element_by_xpath("//span[contains(text(),'Join Twitter today.')]"),'The "Join Twitter today." Label does not appear as expected.')

    def test_twitter_login_004(self):
        """Verify "Sign up with Google" Button appears. 
        """
        wait=WebDriverWait(browser,30)
        wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Sign up with Google')]")))
        self.assertTrue(browser.find_element_by_xpath("//span[contains(text(),'Sign up with Google')]"),'The "Sign up with Google" Button does not appear as expected.')
    
    def test_twitter_login_005(self):
        """Verify "Sign up with Apple" Button appears.
        """
        wait=WebDriverWait(browser,30)
        wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Sign up with Apple')]")))
        self.assertTrue(browser.find_element_by_xpath("//span[contains(text(),'Sign up with Apple')]"),'The "Sign up with Apple" Button does not appear as expected.')

    def test_twitter_login_006(self):
        """Verify "Sign up with phone or email" Button appears..
        """
        wait=WebDriverWait(browser,30)
        wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Sign up with phone or email')]")))
        self.assertTrue(browser.find_element_by_xpath("//span[contains(text(),'Sign up with phone or email')]"),'The  "Sign up with phone or email" Button does not appear as expected.')

    def test_twitter_login_007(self):
        """Verify "Already have an account" string appears.
        """
        wait=WebDriverWait(browser,30)
        wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Already have an account?')]")))
        self.assertTrue(browser.find_element_by_xpath(browser.find_element_by_xpath("//span[contains(text(),'Already have an account?')]")),'The "Sign up with Apple" Button does not appear as expected.')
    
    def test_twitter_login_008(self):
        """Verify "Sign in" Button appears.
        """
        wait=WebDriverWait(browser,30)
        wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Sign in')]")))
        self.assertTrue(browser.find_element_by_xpath("//span[contains(text(),'Sign in')]"),'The "Sign in" Button does not appear as expected.')

    def test_twitter_login_009(self):
        """Verify "Sign up with Sign In" Accepts login.
        """
        wait=WebDriverWait(browser,30)
        wait.until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Sign in')]")))
        browser.find_element_by_xpath("//span[contains(text(),'Sign in')]").click()
        wait.until(EC.presence_of_element_located({By.XPATH,"//span[contains(text(),'Sign in to Twitter')]"}))
        browser.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(cfg.twitter_user_name)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[6]/div[1]")))
        browser.find_element_by_xpath("//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[6]/div[1]").click()
        wait.until(EC.presence_of_element_located((By.XPATH,"//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[6]/div[1]")))
        browser.find_element_by_xpath("//body/div[@id='react-root']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/label[1]/div[1]/div[2]/div[1]/input[1]").send_keys(cfg.twitter_password)
        self.assertTrue(browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div'),'The "Sign in" Button does not appear as expected.')
