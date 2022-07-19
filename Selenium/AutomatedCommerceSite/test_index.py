import os, sys, unittest, time
from webbrowser import BaseBrowser
from selenium import webdriver 
import config as cfg
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class test_index(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global browser
        chrome_options= Options()
        chrome_options.add_argument("--headless")
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

    def test_index_001(self):
        '''
        '''