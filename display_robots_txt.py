try:
    import requests
except Exception as e:
    print(e)
url = input('Enter Url to display robots.txt:- ')+'/robots.txt'
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(e)
except requests.exceptions.ConnectionError:
    print('Server Not Found')
else:
    text = response.text
print(f'Robots.txt for {url}\n ----------------------------------------- \n{text}')
