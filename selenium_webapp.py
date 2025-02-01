from selenium import webdriver
from flask import Falsk, request
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

app = Falsk(__name__)

def download_selenium():
    chrom_options=webdriver.ChromeOptions()
    chrom_options.add_argument('--headless')
    chrom_options.add_argument('--no-sandbox')
    chrom_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.chrome(service=Service(ChromeDriverManager.install()),options=chrom_options)
    driver.get("https://google.com")
    title = driver.title
    language = driver.find_element(By.XPATH, "//div[id='SIvCob']").text
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
    app(debug=True,port=3000)
