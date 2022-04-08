#Implementation of Selenium test automation for this Selenium Python Tutorial
import pytest
from selenium import webdriver
import sys
from os.path import abspath
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

browser = None

def setup_module(module):
    global browser
    browser = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    browser.get('http://localhost:8282/')
    browser.maximize_window()

def teardown_module(module):
    browser.close()

def test_login_fail():
    username_field = browser.find_element(By.CSS_SELECTOR, 'input[name="username"]')
    username_field.clear()
    username_field.send_keys("unauthorized");
    password_field = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')
    password_field.clear()
    password_field.send_keys("password123");
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    sleep(3)
    assert browser.find_element(By.ID,"login").is_displayed()
    assert not browser.find_element(By.ID,"greeting").is_displayed()

def test_login_success():
    username_field = browser.find_element(By.CSS_SELECTOR, 'input[name="username"]')
    username_field.clear()
    username_field.send_keys("unauthorized");
    password_field = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')
    password_field.clear()
    password_field.send_keys("password123");
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    sleep(3)
    assert browser.find_element(By.ID,"login").is_displayed()
    assert not browser.find_element(By.ID,"greeting").is_displayed()

    username_field = browser.find_element(By.CSS_SELECTOR, 'input[name="username"]')
    username_field.clear()
    username_field.send_keys("authorized");
    password_field = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')
    password_field.clear()
    password_field.send_keys("password123");
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.ID,"greeting")))
    assert not browser.find_element(By.ID,"login").is_displayed()
    assert browser.find_element(By.ID,"greeting").is_displayed()
