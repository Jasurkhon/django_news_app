from django.shortcuts import render
from bs4 import BeautifulSoup
from requests import request
import requests



hacknews = "https://thehackernews.com/"
sillicon = "https://www.siliconvalley.com/"
rasp = "https://hackspace.raspberrypi.com/articles"


hack_list = []
hackspace_news = []
silicon_news = []

def get_hacknews():
    r = requests.get(hacknews).text
    soup = BeautifulSoup(r, 'lxml')
    posts = soup.find_all('div', class_='body-post clear')
    for post in posts:
        title = post.find('h2', class_='home-title').text
        url = post.find('a').get('href')
        data = {'title':title,
                'url':url}
        hack_list.append(data)


def get_silicon_news():
    r = requests.get(sillicon).text
    soup = BeautifulSoup(r, "lxml")
    posts = soup.find_all("article")
    for post in posts:
        title = post.find("a", class_="article-title").get('title')
        url = post.find("a", class_="article-title").get("href")

        data = {'title': title,
                'url': url,
                }

        silicon_news.append(data)

def get_hspace_news():
    r = requests.get(rasp).text
    soup = BeautifulSoup(r, "lxml")
    posts = soup.find_all("article")
    for post in posts:
        title = post.find("p", class_="o-type-sub-heading u-weight-bold rspec-article-card--heading").text
        url = post.find("a").get("href")

        data = {'title': title,
                'url': url,
                }

        hackspace_news.append(data)

get_hacknews()
get_silicon_news()
get_hspace_news()



# Create your views here.

def home(requests):
    context = {
        'hacknews_list':hack_list,
        'hackspace_news':hackspace_news,
        'silicon_news':silicon_news,
    }
    return render(requests, 'news_collect_app/index.html', context)
