from tech_news.database import search_news

from typing import List, Dict
from datetime import datetime


def return_tuple_list(news: str) -> List[Dict]:
    tuple_list = []
    for new in news:
        tuple_list.append((new['title'], new['url']))

    return tuple_list


# Requisito 6
def search_by_title(title: str) -> List[Dict]:
    news = search_news({'title': {'$regex': title, '$options': 'si'}})

    return return_tuple_list(news)


# Requisito 7
def search_by_date(date: str) -> List[Dict]:
    try:
        date_formated = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        news = search_news({'timestamp': {'$eq': date_formated}})

        return return_tuple_list(news)
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
