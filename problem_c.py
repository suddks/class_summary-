import requests
from pprint import pprint

URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

params = {
    'ttbkey' : 'ttbstarinsky2841146001',
    'Query' : '파울로 코엘료',
    'QueryType' : 'Author',
    'MaxResults' : 20,
    'start' : 1,
    'SearchTarget' : 'Book',
    'output' : 'js',
    'Version' : '20131101'
}

response = requests.get(URL, params = params)
response = response.json()
#print(type(response['item'][0]['salesPoint']))


new_list = []

def sorted_salesPoint():
    for i in range(len(response['item'])):
        result = response['item'][i]['salesPoint']
        new_list.append(result)
        sorted_list = sorted(new_list, reverse = True)
        top_5_sales = sorted_list[:5]

    return top_5_sales

answer_list = []

def bestseller_book():
    ls = sorted_salesPoint()

    for item in response['item']:
        
        if item['salesPoint'] in ls:
            answer_list.append(item['title'])

    return answer_list            
            


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(bestseller_book())

