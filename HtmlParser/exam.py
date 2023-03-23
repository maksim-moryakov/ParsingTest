from bs4 import BeautifulSoup

with open("d:/Dev/ParsingTest/HtmlParser/blank/index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, 'html.parser')

title = soup.title  # Получение данных по тегу

page_h1 = soup.find('h1')

user_name = soup.find('div', class_='user__name')
find_all_user_info = soup.find_all(class_='user__info')
print(find_all_user_info)


#with open('d:/Dev/ParsingTest/HtmlParser/blank/test.txt', 'a+') as file:
    #file.write(title.text)
    #file.write('\n')
    #file.write(page_h1.text)
    #file.write('\n')
    #file.write(user_name.text)
    #file.write('\n')
    

