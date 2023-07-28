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

new_list = []

#print(type(response['item'][0]['customerReviewRank']))



def best_review_books():
    for i in range(len(response['item'])):
        if response['item'][i]['customerReviewRank'] >= 9: 
            new_list.append(response['item'][i])


    return new_list
       

    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(best_review_books())
