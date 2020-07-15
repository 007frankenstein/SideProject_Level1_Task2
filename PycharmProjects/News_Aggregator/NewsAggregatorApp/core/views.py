from django.shortcuts import render

# Create your views here.

import requests
from bs4 import BeautifulSoup

def home(request):

    toi_page = requests.get("https://timesofindia.indiatimes.com/topic/Coronavirus-India")

    toi_soup = BeautifulSoup(toi_page.content, 'html.parser')
    toi_news_content = toi_soup.find_all('div', class_ = 'content')
    toi_news = []
    for news1 in toi_news_content:
        toi_news.append(news1.text)
    #print(toi_news)

    tie_page = requests.get("https://indianexpress.com/article/india/coronavirus-india-live-updates-lockdown-latest-news-covid-19-vaccine-covid-19-tracker-corona-cases-in-india-today-news-update-6502632/")

    tie_soup = BeautifulSoup(tie_page.content, 'html.parser')
    tie_news_content = tie_soup.find_all('div', class_='comment-body-live')
    tie_news = []
    for news2 in tie_news_content:
        tie_news.append(news2.text)


    return render(request, 'core/home.html', {'toi_news' : toi_news, 'tie_news' : tie_news})
