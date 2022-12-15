#web1.py

from bs4 import BeautifulSoup

#페이지 로딩
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체
soup = BeautifulSoup(page,"html.parser")
#전체페이지 보기
#print(soup.prettify())


print("--- <p>태그 ---")
#<p>태그 전부 검색
# print(soup.find_all("p"))

#첫번째 <p>태그
# print(soup.find("p"))

#검색의 조건: <p class='outer-text'>
#파이썬의 키워드 class제공(이름충돌): class_
# print(soup.find_all("p", class_="outer-text"))

#컨텐츠만
for item in soup.find_all("p"):
    title = item.text.strip()
    title = title.replace("\n", "")
    print(title)

    