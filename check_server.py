#This script is used to check the server 
try:
    import requests
except Exception as e:
    print(e)
   
try:
    response = requests.get('https://www.abdelkhk.com')
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(e)
except requests.exceptions.ConnectionError:
    print('Server Not Found')
else:
    print(response.status_code)
