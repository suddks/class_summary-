import requests
from pprint import pprint

URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

def get_book_info_by_title(title):
    params = {
        'ttbkey': 'ttbstarinsky2841146001',
        'Query': title,
        'QueryType': 'Title',
        'MaxResults': 1,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(URL, params=params)
    response_data = response.json()

    return response_data

def author_other_works(title):
    response_data = get_book_info_by_title(title)

    if 'item' not in response_data or not response_data['item']:
        print('해당 도서 정보를 찾을 수 없습니다.')
        return

    author_name = response_data['item'][0]['author']
    print(f'작가: {author_name}')

    params = {
        'ttbkey': 'ttbstarinsky2841146001',
        'Query': author_name,
        'QueryType': 'Author',
        'MaxResults': 5,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(URL, params=params)
    response_data = response.json()

    if 'item' not in response_data or not response_data['item']:
        print('작가의 다른 작품 정보를 찾을 수 없습니다.')
        return

    print('작가의 다른 작품:')
    for item in response_data['item']:
        print(item['title'])

if __name__ == '__main__':
    book_titles = ['베니스의 상인', '개미', '*']
    for title in book_titles:
        print(f'검색 도서 제목: {title}')
        author_other_works(title)
        print('-' * 50)
