# import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

# получаем исходный код страницы
inner_html_code = str(urlopen('https://thecode.media/parsing/').read(),'utf-8')

# отправляем исходный код страницы на обработку в библиотеку
inner_soup = BeautifulSoup(inner_html_code, "html.parser")

# оставляем только блок с содержимым статьи
inner_soup_1 = inner_soup.find('div', {"class": 'article-content'})

def delete_div(code, tag, arg):
    for div in code.find_all(tag, arg):
        div.decompose()

# удаляем титры
delete_div(inner_soup_1, 'div', {'class': 'wp-block-lazyblock-titry'})

# выводим содержимое страницы
print(inner_soup.get_text())