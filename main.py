import csv
import crawler

articles = crawler.ArticleFetcher()

with open("crawler.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["title", "emoji", "content", "image"])
    for article in articles.fetch():
        writer.writerow([article.title, article.emoji, article.content, article.image])







