#Sends health stats to user at specified time intervals 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://connect.garmin.com/signin")

sleep_total_time = driver.find_element_by_class_name('sleep-total-time')

print(sleep_total_time)
