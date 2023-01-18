from tech_news.database import find_news

from typing import List, Dict
from operator import itemgetter
from collections import Counter


# Requisito 10
def top_5_news() -> List[Dict]:
    news = find_news()

    news_sorted = sorted(
        news, key=itemgetter('comments_count', 'title'), reverse=True
    )

    tuple_list = []
    for new in news_sorted:
        tuple_list.append((new['title'], new['url']))

    return tuple_list[:5]


# Requisito 11
def top_5_categories() -> List[Dict]:
    news = find_news()

    categories = []
    for new in news:
        categories.append(new['category'])

    category_amount = Counter(sorted(categories)).most_common(5)

    categories_most_common = []
    for categoty_tuple in category_amount:
        categories_most_common.append(categoty_tuple[0])

    return categories_most_common
