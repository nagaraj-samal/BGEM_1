from selenium import webdriver


# service_obj=Service()
# webdriver.chrome(service=)
# executable_path = "E:\BrowseDrivers\chromedriver.exe"
from selenium.webdriver.chrome.service import Service

service_obj = Service("E:\BrowseDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
#
driver.get("https://www.google.co.in")

