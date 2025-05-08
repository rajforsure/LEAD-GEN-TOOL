from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def extract_leads():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    # Use a real, simple test page with <h2> tags
    url = "https://quotes.toscrape.com/"
    driver.get(url)
    time.sleep(2)

    print("Page loaded.")

    # Try scraping all quote authors (just for test)
    elements = driver.find_elements(By.CLASS_NAME, "author")
    leads = [el.text for el in elements if el.text.strip() != ""]

    driver.quit()
    return leads
