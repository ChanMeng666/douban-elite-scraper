# Douban Elite Scraper

A lightweight Python tool designed to scrape and archive elite posts from Douban groups. This scraper automatically collects post content, downloads associated images, and organizes everything into well-structured Markdown files for easy reading and archiving.

## Features

- 🔍 Scrapes elite posts from specified Douban groups
- 📥 Downloads and saves all images from posts
- 📝 Generates clean Markdown files with post content
- 🚦 Implements rate limiting to avoid server overload
- 🔒 Handles file naming conflicts with smart sanitization
- 📊 Preserves post metadata (author, source URL)

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ChanMeng666/Douban-elite-scraper.git
cd Douban-elite-scraper
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. The scraper can be run directly using Python:
```bash
python main.py
```

2. By default, it will scrape elite posts from the specified Douban group. To modify target groups or configure scraping behavior, edit the following variables in `main.py`:
```python
# Skip specific posts by title
skip_titles = ["够用就好2"]

# Target group URL
base_url = "https://www.douban.com/group/662976/?type=elite#topics"
```

## Project Structure

```
douban-elite-scraper/
├── main.py          # Main script and entry point
├── scraper.py       # Core scraping functionality
└── requirements.txt # Project dependencies
```

## Output Format

For each scraped post, the script creates:

1. A new directory named after the post (sanitized)
2. A `post.md` file containing:
   - Post title
   - Author information
   - Original URL
   - Post content
   - Image references
3. Downloaded images in the same directory

Example output structure:
```
Post_Title_123abc/
├── post.md
├── image_1.jpg
├── image_2.jpg
└── image_3.jpg
```

## Configuration

The scraper includes several configurable options in the `DoubanScraper` class:

- User-Agent headers
- File naming patterns
- Rate limiting delays
- Output formatting

## Rate Limiting

To be respectful to Douban's servers, the scraper implements a 2-second delay between requests. This can be adjusted in `main.py`:

```python
time.sleep(2)  # Adjust delay as needed
```

## Error Handling

The scraper includes robust error handling for:
- Network connectivity issues
- Invalid URLs
- Missing content
- File system operations
- Image download failures

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Legal Notice

This tool is for educational purposes only. Please ensure compliance with Douban's terms of service and implement appropriate rate limiting. The user is responsible for how they use this tool.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
