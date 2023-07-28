import requests
from pprint import pprint

def author_other_works(title):
    try:
        URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

        params1 = {
            'ttbkey': 'ttbstarinsky2841146001',
            'Query': title,
            'QueryType': 'Title',
            'MaxResults': 20,
            'start': 1,
            'SearchTarget': 'Book',
            'output': 'js',
            'Version': '20131101'
        }

        response = requests.get(URL, params=params1)
        response1 = response.json()

        # 책 저자 이름 (지은이) 라고 출력되는 것을 이용 
        name = response1['item'][0]['author']
        # (지은이) 인덱스를 찾기
        index = name.find('(지은이)')
        # 인덱스 시작 위치까지 끊으면 저자 이름만 출력 
        title_name = name[:index]

        params2 = {
            'ttbkey': 'ttbstarinsky2841146001',
            # 저자 이름이 Query 안으로 들어옴 
            'Query': title_name,
            'QueryType': 'Author',
            'MaxResults': 5,
            'start': 1,
            'SearchTarget': 'Book',
            'output': 'js',
            'Version': '20131101'
        }
        response2 = requests.get(URL, params=params2).json()
        # 같은 저자의 다른 도서를 넣을 리스트 생성 
        arr = []

        for i in range(len(response2['item'])):
            arr.append(response2['item'][i]['title'])
        
        return arr
    # *을 검색하면 검색결과가 출력되지 않음 -> None 이 출력되게 하기위해 예외처리 
    except IndexError:
        return None

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(author_other_works('베니스의 상인'))
    pprint(author_other_works('개미'))
    pprint(author_other_works('*'))
