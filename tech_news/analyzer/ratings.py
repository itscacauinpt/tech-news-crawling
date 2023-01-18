from tech_news.database import find_news

from typing import List, Dict
from operator import itemgetter


# Requisito 10
def top_5_news() -> List[Dict]:
    news = find_news()

    news_sorted = sorted(
        news, key=itemgetter('comments_count', 'title'), reverse=True)

    tuple_list = []
    for new in news_sorted:
        tuple_list.append((new['title'], new['url']))

    return tuple_list[:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
