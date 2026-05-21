from bs4 import BeautifulSoup
import requests


# ======================== Local website ==================== 
# with open("19_beautifulsoup/website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# # print(soup)
# # print(soup.prettify())
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)

# # print(soup.find_all(name="p"))
# all_anchor_tags = soup.find_all(name="a")
# # for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# # print(heading.string)

# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.string)

# company_url = soup.select_one(selector="p a")
# print(company_url)

# ======================== live website ==================== 

response = requests.get("https://news.ycombinator.com/newest")
response.raise_for_status()

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title.string)

articles = soup.select(selector=".titleline > a")
article_links = [ tag.get("href") for tag in articles ]
article_texts = [ tag.getText() for tag in articles ]
article_scores = [int(score.getText().split()[0]) for score in soup.select(selector=".subtext > .subline > .score")]

print(max(article_scores))
print(article_texts[article_scores.index(max(article_scores))])
print(article_links[article_scores.index(max(article_scores))])
