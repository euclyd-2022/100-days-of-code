import requests
from bs4 import BeautifulSoup
response = requests.get("http://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
#print(yc_web_page)
#print(soup.title)

#print storylink class

# titlelink = soup.find_all(name="a", class_="titlelink")
# for title in titlelink:
#     print(title.getText())


#Print the title, link and points of the 1st item
article = soup.find(name="a", class_="titlelink")
print(article.getText())

print(article.get("href"))

#article_upvote = soup.find(name="span", class_="score").getText()
# OR
article_upvote = soup.select_one(".score").getText()

print(article_upvote)

#get all text, links and upvotes
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

largest = max(article_upvotes)
largest_index = article_upvotes.index(largest)

print(article_texts[largest_index])
print(article_links[largest_index])





