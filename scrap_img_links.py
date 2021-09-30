#extract and display all the img links
try:
    import requests
    from bs4 import BeautifulSoup
except Exception as e:
    print(e)
url = input('Enter Url to Get Img Links:- ')  
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(e)
except requests.exceptions.ConnectionError:
    print('Server Not Found')
else:
    doc_body = BeautifulSoup(response.text,'html.parser')
img_links = doc_body.find_all('img')
for img in img_links:
    print(f'Image Link is  : {img.get("src")}')