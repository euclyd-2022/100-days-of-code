from bs4 import BeautifulSoup


with open("../Day 44/cv/index.html") as f:
    contents = f.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.title)

print(soup.title.string)

#print(soup.prettify())

#find all 'a' tags
all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.getText())

