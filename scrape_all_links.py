#scrap all links from site
try:
    import requests
    from bs4 import BeautifulSoup
except Exception as e:
    print(e)
url = input('Enter Url to Get all Links:- ')  
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(e)
except requests.exceptions.ConnectionError:
    print('Server Not Found')
else:
    doc_body = BeautifulSoup(response.text,'html.parser')
all_links = doc_body.find_all('a',href=True)
for link in all_links:
    print(f'Link is  : {link.get("href")}')
