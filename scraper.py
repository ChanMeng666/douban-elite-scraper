import requests
from bs4 import BeautifulSoup
import os
import time
import re
from urllib.parse import urljoin
import hashlib

class DoubanScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
    def sanitize_filename(self, filename):
        # 移除非法文件名字符
        sanitized = re.sub(r'[<>:"/\\|?*]', '', filename)
        # 生成短的hash值作为唯一标识符
        hash_suffix = hashlib.md5(filename.encode()).hexdigest()[:6]
        # 截取前30个字符并添加hash值
        if len(sanitized) > 30:
            sanitized = sanitized[:30] + f"_{hash_suffix}"
        return sanitized
    
    def get_post_content(self, url):
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 获取帖子内容
        content = soup.find('div', class_='topic-content')
        if not content:
            return None, []
            
        # 获取图片
        images = []
        for img in content.find_all('img'):
            img_url = img.get('src')
            if img_url:
                images.append(urljoin(url, img_url))
                
        return content.text.strip(), images
    
    def save_post(self, title, author, content, images, base_url):
        # 使用处理过的标题作为文件夹名
        folder_name = self.sanitize_filename(title)
        
        try:
            # 创建文件夹
            os.makedirs(folder_name, exist_ok=True)
            
            # 保存图片
            image_paths = []
            for i, img_url in enumerate(images):
                img_path = f"{folder_name}/image_{i+1}.jpg"
                try:
                    img_data = requests.get(img_url, headers=self.headers).content
                    with open(img_path, 'wb') as f:
                        f.write(img_data)
                    image_paths.append(img_path)
                except Exception as e:
                    print(f"保存图片失败: {e}")
                    continue
                    
            # 创建markdown文件
            md_content = f"""# {title}

作者: {author}
来源: {base_url}

## 内容
{content}

## 图片
"""
            
            for img_path in image_paths:
                md_content += f"![Image]({img_path})\n"
                
            with open(f"{folder_name}/post.md", 'w', encoding='utf-8') as f:
                f.write(md_content)
                
            print(f"成功保存帖子到文件夹: {folder_name}")
                
        except Exception as e:
            print(f"保存帖子失败: {e}")