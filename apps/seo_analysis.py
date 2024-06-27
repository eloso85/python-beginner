import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import time
import json

def main(url: str) -> dict:
    """
    Perform advanced SEO analysis on the given website URL using Beautiful Soup.

    Parameters:
    - url (str): The URL of the website to analyze.

    Returns:
    - dict: A dictionary containing advanced SEO analysis results including title length,
      number of headings, presence of meta description, meta tags, text-to-HTML ratio,
      canonical link, keyword density, mobile friendliness, and link health.
    """
    try:
        # Start timing the request
        start_time = time.time()

        # Send a GET request to the URL
        response = requests.get(url)
        # Calculate the loading time
        loading_time = time.time() - start_time

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # SEO analysis
        seo_analysis = {}

        # Get the title of the page and its length
        title = soup.find("title").text if soup.find("title") else "No title found"
        seo_analysis["title"] = title
        seo_analysis["title_length"] = len(title)

        # Count the number of headings (h1, h2, h3, h4, h5, h6)
        headings = {f"h{i}": len(soup.find_all(f"h{i}")) for i in range(1, 7)}
        seo_analysis["headings_count"] = headings

        # Check for meta description
        meta_description = soup.find("meta", attrs={"name": "description"})
        seo_analysis["meta_description"] = (
            meta_description["content"]
            if meta_description
            else "No meta description found"
        )

        # Additional meta tags
        meta_robots = soup.find('meta', attrs={'name': 'robots'})
        seo_analysis['meta_robots'] = meta_robots['content'] if meta_robots else 'No robots meta tag'

        # Canonical link
        canonical_link = soup.find('link', rel='canonical')
        seo_analysis['canonical_link'] = canonical_link['href'] if canonical_link else 'No canonical link'

        # Text to HTML Ratio
        text_length = len(soup.get_text())
        html_length = len(response.text)
        seo_analysis['text_to_html_ratio'] = text_length / html_length if html_length > 0 else 0

        # Keyword Density (Example: assuming 'example_keyword' is the keyword)
        words = re.findall(r'\w+', soup.get_text().lower())
        word_count = Counter(words)
        total_words = sum(word_count.values())
        focus_keyword = 'example_keyword'
        keyword_density = word_count[focus_keyword] / total_words if focus_keyword in word_count and total_words > 0 else 0
        seo_analysis['keyword_density'] = keyword_density

        # Mobile Friendliness
        seo_analysis['mobile_friendly'] = 'yes' if 'viewport' in (meta_description["content"].lower() if meta_description else '') else 'no'

        # Link Analysis
        links = soup.find_all('a', href=True)
        seo_analysis['total_links'] = len(links)
        seo_analysis['nofollow_links'] = sum(1 for link in links if 'nofollow' in link.get('rel', []))
        seo_analysis['external_links'] = sum(1 for link in links if link['href'].startswith('http'))
        seo_analysis['internal_links'] = seo_analysis['total_links'] - seo_analysis['external_links']

        # Images Alt Text
        images = soup.find_all('img')
        images_with_alt = sum(1 for img in images if img.get('alt'))
        seo_analysis['images_with_alt'] = images_with_alt
        seo_analysis['total_images'] = len(images)

        # Favicon
        favicon = soup.find('link', rel=lambda value: value and 'icon' in value.lower())
        seo_analysis['favicon'] = favicon['href'] if favicon else 'No favicon found'

        # Open Graph Tags
        og_tags = {tag['property']: tag['content'] for tag in soup.find_all('meta', attrs={'property': re.compile('^og:')})}
        seo_analysis['open_graph_tags'] = og_tags

        # Twitter Card Tags
        twitter_tags = {tag['name']: tag['content'] for tag in soup.find_all('meta', attrs={'name': re.compile('^twitter:')})}
        seo_analysis['twitter_card_tags'] = twitter_tags

        # Hreflang Tags
        hreflang_tags = [tag['href'] for tag in soup.find_all('link', rel='alternate', hreflang=True)]
        seo_analysis['hreflang_tags'] = hreflang_tags

        # Structured Data
        structured_data = soup.find_all('script', type='application/ld+json')
        seo_analysis['structured_data'] = [script.string for script in structured_data]

        # Page Loading Time
        seo_analysis['loading_time'] = loading_time

        return seo_analysis
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    url = input("Enter the URL to scan: ")
    result = main(url)
    print(json.dumps(result, indent=4, ensure_ascii=False))
