<div align="center">
 <h1> 🔍 Douban Elite Scraper</h1>
 <p>Archive elite posts from Douban groups with style</p>

 <img src="https://img.shields.io/badge/python-v3.7+-blue?style=flat&logo=python&logoColor=white"/>
 <img src="https://img.shields.io/badge/beautifulsoup4-latest-green?style=flat"/>
 <img src="https://img.shields.io/badge/License-MIT-brightgreen?style=flat"/>
 <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=flat"/>
</div>

## ✨ Features

### 🎯 Smart Content Extraction
Intelligently scrapes elite posts while respecting Douban's access patterns and rate limits.

### 📸 Complete Media Preservation
Downloads and organizes all images associated with each post, maintaining the original content integrity.

### 📝 Clean Markdown Generation
Converts posts into well-structured Markdown files, perfect for offline reading and archival.

### 🔒 Robust Error Handling
Comprehensive error management for network issues, missing content, and file system operations.

### 🚦 Rate Limiting Protection
Built-in delays and smart request handling to avoid overwhelming Douban's servers.

### 📊 Metadata Preservation
Retains important post information including author details and source URLs.

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/ChanMeng666/douban-elite-scraper.git
cd douban-elite-scraper
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Run the scraper:
```bash
python main.py
```

2. Configure target groups by editing `main.py`:
```python
# Skip specific posts by title
skip_titles = ["够用就好2"]

# Target group URL
base_url = "https://www.douban.com/group/662976/?type=elite#topics"
```

## 📁 Project Structure

```
douban-elite-scraper/
├── main.py          # Main script and entry point
├── scraper.py       # Core scraping functionality
└── requirements.txt # Project dependencies
```

## 📦 Output Format

Each scraped post creates:
```
Post_Title_123abc/
├── post.md
├── image_1.jpg
├── image_2.jpg
└── image_3.jpg
```

The `post.md` file contains:
- Post title
- Author information
- Original URL
- Post content
- Image references

## ⚙️ Configuration

The scraper includes several configurable options in the `DoubanScraper` class:
- User-Agent headers
- File naming patterns
- Rate limiting delays
- Output formatting

## 🛡️ Rate Limiting

The scraper implements a 2-second delay between requests by default. Adjust in `main.py`:
```python
time.sleep(2)  # Adjust delay as needed
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ⚠️ Legal Notice

This tool is for educational purposes only. Please ensure compliance with Douban's terms of service and implement appropriate rate limiting. The user is responsible for how they use this tool.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

<details>
<summary>
  🔧 Advanced Configuration
</summary>

The `DoubanScraper` class provides additional configuration options:

```python
scraper = DoubanScraper(
    headers={'User-Agent': 'your-custom-user-agent'},
    delay=3,  # Custom delay between requests
    output_format='markdown'  # Output format
)
```

See `scraper.py` for more configuration options.

</details>

## 🙋‍♀ Author

Created and maintained by [Chan Meng](https://github.com/ChanMeng666).
