from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def index(request):

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    data = []

    for b in range(1, 5):
        URL = "https://etherscan.io/accounts/" + str(b)
        driver.get(URL)

        soup = BeautifulSoup(driver.page_source, "lxml")

        i = 0
        a = 4

        for td in soup.find_all("td"):
            if(i == a):
                data.append(td.get_text())
                a = a + 6
            i = i + 1

    

    context = {
        "data": data
    }

    return render(request, 'chartapp/index.html', context)