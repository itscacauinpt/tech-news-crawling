import requests

import time
from parsel import Selector
from bs4 import BeautifulSoup

from .database import create_news


# Requisito 1
def fetch(url) -> str:
    try:
        time.sleep(1)
        headers = {"user-agent": "Fake user-agent"}
        response = requests.get(url, timeout=1, headers=headers)
        stts = response.status_code

        if stts != 200:
            return None
        elif stts == 200:
            return response.text

    except (requests.ReadTimeout, requests.HTTPError):
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    return selector.css('h2.entry-title > a::attr(href)').getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_ref = '/'
    while next_page_ref:
        return selector.css('a.next.page-numbers::attr(href)').get()
    else:
        return None


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)

    return {
        'url': selector.css('head > link[rel~="canonical"]::attr(href)').get(),
        'title': selector.css('h1.entry-title::text').get().strip(),
        'timestamp': selector.css('li.meta-date::text').get(),
        'writer': selector.css('span.author > a::text').get(),
        'tags': selector.css('a[rel=tag]::text').getall(),
        'category': selector.css('a.category-style > span.label::text').get(),
        'comments_count': len(
            selector.css('ol.comment-list > li').getall()) or 0,
        'summary': BeautifulSoup(
            selector.css('.entry-content p').get(), 'html.parser'
        ).get_text().strip(),
    }


# Requisito 5
def get_tech_news(amount):
    url_page = 'https://blog.betrybe.com/'

    news_amount_to_create = []
    list_news_url = []

    while len(news_amount_to_create) <= amount:
        content = fetch(url_page)
        list_news_url = scrape_updates(content)

        for news_url in list_news_url:
            news_content = fetch(news_url)
            data_dict = scrape_news(news_content)
            news_amount_to_create.append(data_dict)

        url_page = scrape_next_page_link(content)

    create_news(news_amount_to_create[:amount])
    return news_amount_to_create[:amount]
