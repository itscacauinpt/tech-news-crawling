from tech_news.database import search_news

from typing import List, Dict
from datetime import datetime


def return_tuple_list(query: str) -> List[Dict]:
    tuple_list = []
    news = search_news(query)
    for new in news:
        tuple_list.append((new['title'], new['url']))

    return tuple_list


# Requisito 6
def search_by_title(title: str) -> List[Dict]:
    query = {'title': {'$regex': title, '$options': 'si'}}

    return return_tuple_list(query)


# Requisito 7
def search_by_date(date: str) -> List[Dict]:
    try:
        date_formated = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        query = {'timestamp': {'$eq': date_formated}}

        return return_tuple_list(query)
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_tag(tag: str) -> List[Dict]:
    query = {'tags': {'$regex': tag, '$options': 'si'}}

    return return_tuple_list(query)


# Requisito 9
def search_by_category(category: str) -> List[Dict]:
    query = {'category': {'$regex': category, '$options': 'si'}}

    return return_tuple_list(query)
