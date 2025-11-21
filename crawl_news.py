import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

# 1. 디렉토리 생성
os.makedirs('docs', exist_ok=True)

# 2. 크롤링 대상 URL
URL = "https://m.etnews.com/news/hot_content_list.html"
res = requests.get(URL)
soup = BeautifulSoup(res.text, 'html.parser')

# 3. "SW 많이 본 뉴스" 상위 5개 추출..
topnews_section= soup.select_one("section.textthumb")
most_viewed = topnews_section.select('ul li strong a')[:10]

now = datetime.now().strftime('%Y-%m-%d')
with open('docs/index.md', 'w', encoding='utf-8') as f:
    f.write(f"# 📅 {now} SW 많이 본 뉴스 (전자신문)\n\n")
    for i, article in enumerate(most_viewed, 1):
        title = article.text.strip()
        link = "https://m.etnews.com" + article['href']
        f.write(f"{i}. [{title}]({link})\n")
