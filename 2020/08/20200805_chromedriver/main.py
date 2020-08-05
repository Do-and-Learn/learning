from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)  # prevent close the browser when program ends
    chrome_options.add_extension("buster_captcha_solver_for_humans-1.0.1-chrome.zip")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get('http://www.google.com.tw')
