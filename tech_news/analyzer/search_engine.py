from tech_news.database import search_news
from typing import List, Dict


# Requisito 6
def search_by_title(title: str) -> List[Dict]:
    tuple_list = []
    news = search_news({'title': {'$regex': title, '$options': 'si'}})

    for new in news:
        tuple_list.append((new['title'], new['url']))

    return tuple_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
