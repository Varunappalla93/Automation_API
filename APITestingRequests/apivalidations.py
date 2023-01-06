import requests
import json

# params take in dict format
getbookresp = requests.get('http://216.10.245.166/Library/GetBook.php', params={'AuthorName': 'Rahul Shetty2'}, )

# get api response
print(getbookresp.text)
# [{"book_name":"Devops","isbn":"bnid34","aisle":"128"},{"book_name":"Devops","isbn":"bnid34","aisle":"129"}]

print(type(getbookresp.text))  # <class 'str'>

# print and validate status codes
print(getbookresp.status_code)  # 200
assert getbookresp.status_code == 200

# print headers
print(getbookresp.headers)
# {'Date': 'Thu, 15 Jul 2021 07:02:27 GMT', 'Server': 'Apache', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'POST', 'Access-Control-Max-Age': '3600', 'Access-Control-Allow-Headers': 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With', 'Keep-Alive': 'timeout=5, max=100', 'Connection': 'Keep-Alive', 'Transfer-Encoding': 'chunked', 'Content-Type': 'application/json;charset=UTF-8'}

# validate headers
assert getbookresp.headers['Content-Type'] == 'application/json;charset=UTF-8'

# get cookies
print(getbookresp.cookies)  # <RequestsCookieJar[]>

# convert string to dict using loads, if its in list format, it will be in list only.
getbookdict = json.loads(getbookresp.text)
print(getbookdict)
# [{'book_name': 'Devops', 'isbn': 'bnid34', 'aisle': '75'}, {'book_name': 'Devops', 'isbn': 'abcd', 'aisle': '75'}]

print(type(getbookdict))  # <class 'list'>

print(getbookdict[1]['isbn'])  # abcd

# or use json() directly instead of using loads for converting to dict and
# then check type if its list which cannot be converted to dict.

getbookjsonresp = getbookresp.json()
print(type(getbookjsonresp))  # <class 'list'>
print(getbookjsonresp)
# [{'book_name': 'Devops', 'isbn': 'bnid34', 'aisle': '75'}, {'book_name': 'Devops', 'isbn': 'abcd', 'aisle': '75'}]

print(getbookjsonresp[0]['isbn'])  # bnid34

# get books details based in isbn with abcd
for act_book in getbookjsonresp:
    # print(type(book)) # dict
    if act_book['aisle'] == '75':
        print(act_book['book_name'])
        print(act_book)
        break

print(act_book)

expectedbook = {'book_name': 'Devops', 'isbn': 'bnid34', 'aisle': '75'}


# compare two dicts
assert actbook == expectedbook

# Devops
# {'book_name': 'Devops', 'isbn': 'bnid34', 'aisle': '75'}
