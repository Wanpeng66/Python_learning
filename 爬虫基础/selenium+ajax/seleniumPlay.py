import time

from selenium import webdriver
from selenium.webdriver import ActionChains

if __name__ == '__main__':
    driver_path = "D:/ep/uploads/driver/chromedriver.exe"
    chrome = webdriver.Chrome(executable_path=driver_path)
    chrome.get("https://www.bilibili.com/")
    # 等待5秒钟 
    chrome.implicitly_wait(5)
    kwInput = chrome.find_element_by_class_name("nav-search-keyword")
    submitBtn = chrome.find_element_by_class_name("nav-search-submit")

    # ActionChains鼠标行为链类 将一系列操作整合在一起 然后分步执行
    search = ActionChains(chrome)
    search.send_keys_to_element(kwInput,"芦荟胶")
    search.click(submitBtn)
    search.perform()
    # chrome.quit()