# imports
from selenium import webdriver 
from selenium.webdriver.common import By
from selenium.webdriver.common.action_chains import actionChains
import time
# set driver

# functions

# test1: dupla kattintás után szerepel-e az "animation" class
def test1():
    elementOne = driver.find_element(By.ID,value = element-one)
    elementOne.click() 
time.sleep(1)
# ha rámegy az egér, utána létezik-e box-shadow
def test2():
    def test1():
    elementOne = driver.find_element(By.ID,value = element-two)
    assert "box-shadow" in elementTwo.get_attribute("style")

time.sleep(1)
# kattintás után eltűnik-e
def test3():
    def test1():
    elementOne = driver.find_element(By.ID,value = element-three)
    assert "hidden" in elementTwo.get_attribute("style")
    elementOne.click() 

time.sleep(1)
# kattintás után a háttere zöld lesz-e
def test4():
    def test1():
    elementOne = driver.find_element(By.ID,value = element-four)
    assert "green" in elementTwo.get_attribute("style")
    elementOne.click() 

time.sleep(1)
# ha a 4. elemre egeret viszünk, hogy néz ki? (screenshot kell csak!)
def test5():
    def test1():
    elementOne = driver.find_element(By.ID,value = element-five)
    driver.save_screenshot("test5.jpg")
    elementOne.click() 