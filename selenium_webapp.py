from selenium import webdriver
from flask import Flask, request
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

def download_selenium():
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # Install ChromeDriver
    service = Service(ChromeDriverManager().install())

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # driver = webdriver.chrome(service=Service(ChromeDriverManager.install()),options=chrom_options)
    driver.get("https://google.com")
    title = driver.title
    language = driver.find_element(By.XPATH, "//div[@id='SIvCob']").text
    data = {
        'Page Title':title,
        'Language':language
    }
    return data

@app.route('/',methods=['GET','POST'])
def home():
    if(request.method=='GET'):
        return download_selenium()



if __name__=="__main__":
    app.run(debug=True,port=3000)
