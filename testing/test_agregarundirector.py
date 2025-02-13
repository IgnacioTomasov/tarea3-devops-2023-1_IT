# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAgregarundirector():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_agregarundirector(self):
    self.driver.get("http://localhost:8001/")
    self.driver.set_window_size(1296, 728)
    self.driver.find_element(By.ID, ":r1:-tab-1").click()
    self.driver.find_element(By.CSS_SELECTOR, "#add-director-btn .w-16").click()
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("Sydney Lumet")
    self.driver.find_element(By.CSS_SELECTOR, ".h-min > .flex").click()
  
