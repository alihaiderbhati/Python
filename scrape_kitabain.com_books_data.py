import requests
from bs4 import BeautifulSoup
import time
import os
import sys
import csv
import json



def get_site_html(url):
    r = requests.get(url)
    if not r.status_code == 200:
        print('Request Error')
        input('Press enter to exit:- ')
        exit()
    s = BeautifulSoup(r.text,'html.parser')
    return s

def get_page_info(page_url):
    page_html = get_site_html(page_url)
    books = page_html.find_all('div',class_="bookimgdiv")
    print(f"Total books :- {len(books)}")
    return books

def get_book_data_csv(book):
    book_url = book.find('a').get('href')
    book_title = book.find('p').find('a').get('title').strip()
    book_author = book.find('p',class_='other_name').text.strip()
    book_price = book.find_all('p')[2].text.strip().replace('(','').replace(')','')
    book_data_csv = [book_url,book_title,book_author,book_price]
    return book_data_csv
    
def get_book_data_json(book):
    book_url = book.find('a').get('href')
    book_title = book.find('p').find('a').get('title').strip()
    book_author = book.find('p',class_='other_name').text.strip()
    book_price = book.find_all('p')[2].text.strip().replace('(','').replace(')','')
    book_data_json = {
        "book_url": book_url,
        "book_title" : book_title,
        "book_author" : book_author,
        "book_price" : book_price
        }
    return book_data_json

    
def save_to_csv(data):
    file = os.path.join(sys.path[0],'kitabain_data.csv')
    with open(file,'w',newline='',encoding='utf-8') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(['Book Link','Book Title','Book Author','Book Price'])
        csvwriter.writerows(data)

def save_to_json(data):
    file = os.path.join(sys.path[0],'kitabain_data.json')
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

        
link = "https://www.kitabain.com/books/all"
site_html = get_site_html(link)
total_pages = int(site_html.find('ul',class_="pagination").find_all('li')[-2].text.strip())
print(f"Total Pages :- {total_pages}")

books_data_json = {
    "books" : []
    }
books_data_csv = []
for page in range(1,3):
    print(f"Scraping Page {page}")
    page_url = f"{link}?page={page}"
    books = get_page_info(page_url)
    for book in books:
        books_data_csv.append(get_book_data_csv(book))
        books_data_json['books'].append(get_book_data_json(book))


save_to_csv(books_data_csv)
save_to_json(books_data_json)
