from testeselenium2 import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriveManager

service= Service("/path/to/chromedriver")
driver = webdriver.Chrome(service=service(ChromeDriverManager().install()))

driver.get("https://www.google.com/")