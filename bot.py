#!/usr/bin/env python3
#
# DEXT Tools Proxied Traffic Bot
#
import logging
import threading 
from multiprocessing import Process
from seleniumwire import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.proxy import *
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
    TimeoutException,
    WebDriverException,
)

# Proxy Auth URL
PROXY = "USERNAME:PASSWORD@p.webshare.io:80"

PROCESS_COUNT = 1
THREAD_COUNT = 5

# DEXT PAGE WE WANT TO SEND BOT TRAFFIC
URL = "https://www.dextools.io/app/en/ether/pair-explorer/PAIR_ADDRESS"

# Links we want the bot to click on the page
LINKS = [
    "https://etherscan.io/token/TOKEN_ADDRESS",
]

PROXY_OPTIONS = {
    'proxy': {
        'https': f'https://' + PROXY,
        'http': f'http://' + PROXY,
        'verify_ssl': False,
    },
}

# Set up logging
logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)

def wait_for_document_ready(driver, timeout=5):
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )
    except (TimeoutException, WebDriverException) as e:
            logger.critical('Error waiting for site')
            pass


def access_site():
    ua = UserAgent()
    userAgent = ua.random

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless") # Comment this line out to preview bot actions.
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("--disable-setuid-sandbox")

    # Options to control cache and memory usage
    chrome_options.add_argument("--disable-application-cache")
    chrome_options.add_argument("--media-cache-size=1")
    chrome_options.add_argument("--disk-cache-size=1")
    chrome_options.add_argument("--aggressive-cache-discard")

    # Options to control rendering and other visual elements
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-offline-auto-reload")
    chrome_options.add_argument("--disable-offline-auto-reload-visible-only")
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")
    chrome_options.add_argument("--disable-image-loading")
    chrome_options.add_argument(f'user-agent={userAgent}') 

    capabilities = webdriver.DesiredCapabilities.CHROME

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options,
        seleniumwire_options=PROXY_OPTIONS,
        desired_capabilities=capabilities
    )

    try:
        driver.get(URL)
        print('Opened DEXT')
        
        wait_for_document_ready(driver)        
        wait = WebDriverWait(driver, 3)

        # Action 1 - Favorite Coin
        try:
            element = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "app-favorite-button")))
            element.click()
        except (NoSuchElementException, ElementClickInterceptedException, TimeoutException, WebDriverException) as e:
            logger.critical('Error Clicking Favorite')
            pass


        # Action 2 - Open the Links Found in Dext Tools HTML
        for link in LINKS:
            try:
                element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'a[href="{link}"]')))
                element.click()
            except (NoSuchElementException, ElementClickInterceptedException, TimeoutException, WebDriverException) as e:
                logger.critical('Error clicking link')

        # Action 3 - Click Share 
        try:
            element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'fa-share')))
            element.click()
        except (NoSuchElementException, ElementClickInterceptedException, TimeoutException, WebDriverException) as e:
            logger.critical('Error Clicking Share')
            pass

    except WebDriverException as e:
        logger.critical(f"WebDriverException: {e}")
        pass
    except ConnectionError as e:
        logger.critical(f"Connection Error: {e}")
        pass
    except Exception as e:
        logger.critical(f"Error: {e})
        pass
    finally:
        driver.quit()
        print('Closed DEXT')

def access_site_in_threads():
    threads = []
    for _ in range(THREAD_COUNT):
        t = threading.Thread(target=access_site)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

def main():
    while True:
        processes = []
        for _ in range(PROCESS_COUNT):
            p = Process(target=access_site_in_threads)
            p.start()
            processes.append(p)

        for p in processes:
            p.join()

if __name__ == "__main__":
    main()
