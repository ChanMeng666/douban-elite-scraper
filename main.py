from scraper import DoubanScraper
import requests
from bs4 import BeautifulSoup
import time

def main():
    # 需要跳过的帖子标题列表
    skip_titles = [
        "够用就好2"
    ]
    
    scraper = DoubanScraper()
    base_url = "https://www.douban.com/group/662976/?type=elite#topics"
    
    response = requests.get(base_url, headers=scraper.headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 获取所有精华帖子链接
    table = soup.find('table', class_='olt')
    if not table:
        print("无法获取帖子列表，可能需要登录或者遇到反爬限制")
        return
        
    rows = table.find_all('tr')[1:]  # 跳过表头行
    
    for row in rows:
        # 获取标题和链接
        title_cell = row.find('td', class_='title')
        if not title_cell:
            continue
            
        link = title_cell.find('a')
        if not link:
            continue
            
        title = link.text.strip()
        
        # 检查是否需要跳过这个帖子
        if any(skip_title in title for skip_title in skip_titles):
            print(f"跳过帖子: {title}")
            continue
            
        url = link['href']
        
        # 获取作者
        author_cell = row.find('td', attrs={'nowrap': 'nowrap'})
        if author_cell and author_cell.find('a'):
            author = author_cell.find('a').text
        else:
            author = "未知作者"
        
        print(f"Processing: {title} by {author}")
        
        content, images = scraper.get_post_content(url)
        if content:
            scraper.save_post(title, author, content, images, url)
            
        # 避免请求过快
        time.sleep(2)

if __name__ == "__main__":
    main() 