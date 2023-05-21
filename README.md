# DEXT Tools Proxied Traffic Bot

This is a Python script for a proxied traffic bot that interacts with the DEXT Tools website. The bot uses Selenium and SeleniumWire libraries to automate browser actions and simulate user traffic. The purpose of this bot is to perform specific actions on the DEXT Tools website and click on links provided.

### This is demo code for educational purposes / proof of concept only, botting websites without permission is illegal. 

## Prerequisites

- Python 3.x
- SeleniumWire library
- Fake User-Agent library
- Chrome browser

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Install the required Python libraries by running the following command: `pip install seleniumwire fake_useragent webdriver_manager`
3. Ensure that you have Google Chrome installed on your machine.

## Usage

1. Open the script in a text editor.
2. Customize the following variables according to your requirements:

- `PROXY`: The proxy URL in the format `USERNAME:PASSWORD@p.webshare.io:80`.
- `PROCESS_COUNT`: The number of processes to run concurrently.
- `THREAD_COUNT`: The number of threads to run concurrently within each process.
- `URL`: The URL of the DEXT Tools page you want to send traffic to.
- `LINKS`: A list of links you want the bot to click on the page.

3. Save the script after making the necessary modifications.
4. Open a terminal or command prompt and navigate to the directory containing the script.
5. Run the script using the following command: `python3 bot.py`


## Explanation

- The script utilizes multithreading and multiprocessing to achieve concurrent execution and increase performance.
- The `access_site` function is responsible for automating the browser actions. It uses Selenium and SeleniumWire to control the Chrome browser and interact with the web page.
- The function sets up the Chrome browser with specific options, including a headless mode for running without a visible browser window.
- It opens the specified DEXT Tools page, waits for the page to finish loading, and then performs the desired actions on the page.
- The actions include clicking on a favorite button, clicking on specified links, and clicking on a share button.
- The `access_site_in_threads` function is used to run multiple instances of the `access_site` function concurrently within separate threads.
- The `main` function creates multiple processes and assigns each process a certain number of threads to run the `access_site_in_threads` function.
- The script continuously runs in an infinite loop to keep sending traffic to the DEXT Tools page.

### Please ensure that you have the necessary permissions and legal rights to use such a traffic bot. It is illegal to run botted traffic on any website without the webmaster / website owner explicit permission. 
