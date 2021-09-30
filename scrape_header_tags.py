#extract and display all the header tags 
try:
    import requests
    from bs4 import BeautifulSoup
except Exception as e:
    print(e)
url = input('Enter Url to Get Header tags:- ')  
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(e)
except requests.exceptions.ConnectionError:
    print('Server Not Found')
else:
    doc_body = BeautifulSoup(response.text,'html.parser')
header_tag = doc_body.find_all(['h1','h2','h3','h4','h5','h6'])
for header in header_tag:
    print(f'Header Tag is  : {header.text}')