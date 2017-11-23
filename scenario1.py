from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


class scenario1():

    def test1 (self):
        url = "https://github.com/"
        driver = webdriver.Chrome("C:\\Users\\basia\\Desktop\\Ecercise\\chromedriver_win32\\chromedriver.exe")
        driver.maximize_window()
        driver.get(url)
        driver.implicitly_wait(10)


        login = driver.find_element(By.LINK_TEXT, "Sign in")
        login.click()
        username = driver.find_element(By.NAME, "login")
        username.send_keys("basieq85")
        password = driver.find_element(By.NAME, "password")
        password.send_keys("test12345")
        submit = driver.find_element(By.NAME, "commit")
        submit.click()
        select = driver.find_element(By.LINK_TEXT, "New repository")
        select.click()
        repository_name = ("Repo" + str(random.randint(0,100)))
        repo_name = driver.find_element(By.NAME, "repository[name]")
        repo_name.send_keys(repository_name)
        description = driver.find_element(By.NAME, "repository[description]")
        description.send_keys("test")
        create = driver.find_element(By.XPATH, "//button[@type='submit'] and conains(text(),'Create repository')")
        print(create)
        time.sleep(3)
        create.click()


        time.sleep(3)
        driver.quit()


ff = scenario1()
ff.test1()