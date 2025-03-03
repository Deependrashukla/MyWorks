import csv
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
api_key = "AIzaSyCFrGrVxKzgPkduvc2kqC-n07MzfzIXPYI"
cx_id = "77462b8ececf14052"
query = "Nutritional benefits of avocados"

with open('searc.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Rank", "URL"])
    for page in range(0, 11):
        url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx_id}&q={query}&start={page*10}"
        response = requests.get(url)
        results = response.json().get('items', [])
        for i, result in enumerate(results, start=1):
            writer.writerow([(page)*10 + i, result['link']])
            
def calculate_title_importance(title, query):
    title = title.lower()
    query = query.lower()
    query_words = query.split()
    count = sum(word in title for word in query_words)
    importance = count / len(query_words)
    return importance

def calculate_headers_importance(headers, query):
    query = query.lower()
    query_words = query.split()
    total_importance = 0
    for header in headers:
        header = header.lower()
        count = sum(word in header for word in query_words)
        importance = count / len(query_words)
        total_importance += importance
    return total_importance

def calculate_body_text_importance(body_text, query):
    body_text = body_text.lower()
    query = query.lower()
    query_words = query.split()
    body_text_words = body_text.split()
    count = sum(word in body_text_words for word in query_words)
    importance = count / len(query_words)
    return importance

def calculate_alt_text_for_images_importance(alt_text_for_images, query):
    alt_text_for_images = alt_text_for_images.lower()
    query = query.lower()
    query_words = query.split()
    count = sum(word in alt_text_for_images for word in query_words)
    importance = count / len(query_words)
    return importance

def calculate_backlinks_importance(backlinks):
    importance = len(backlinks)
    return importance

def calculate_meta_tags_importance(meta_tags, query):
    meta_tags = meta_tags.lower()
    query = query.lower()
    query_words = query.split()
    count = sum(word in meta_tags for word in query_words)
    importance = count / len(query_words)
    return importance

with open('searc.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    urls = [(row[0], row[1]) for row in reader]
    urls = urls[0:]
with open('seo_.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Rank", "URL", "Title Importance", "Headers Importance", "Body Text Importance", "Meta Tags Importance", "Alt Text for Images Importance", "Loading Speed Score", "Backlinks Importance"])
    
    with requests.Session() as session:
        def fetch(url):
            try:
                response = session.get(url, verify=False)
                return response if response.status_code == 200 else None
            except requests.exceptions.RequestException:
                return None

        with ThreadPoolExecutor(max_workers=5) as executor:
            responses = executor.map(fetch, [url for i, url in urls])

        for response, (i, url) in zip(responses, urls):
            if response is not None:
                try:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    title = soup.find('title').text if soup.find('title') else 'N/A'
                    headers = [h.text for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])] if soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']) else 'N/A'
                    body_text = soup.find('body').text if soup.find('body') else 'N/A'
                    meta_tags = ', '.join([meta['content'] for meta in soup.find_all('meta') if 'content' in meta.attrs]) if soup.find_all('meta') else 'N/A'
                    alt_text_for_images = ', '.join([img['alt'] for img in soup.find_all('img') if 'alt' in img.attrs]) if soup.find_all('img') else 'N/A'
                    backlinks = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('http')] if soup.find_all('a', href=True) else 'N/A'
                    pagespeed_response = requests.get(f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}")
                    loading_speed_score = pagespeed_response.json()['lighthouseResult']['audits']['speed-index']['displayValue'] if 'lighthouseResult' in pagespeed_response.json() and 'audits' in pagespeed_response.json()['lighthouseResult'] and 'speed-index' in pagespeed_response.json()['lighthouseResult']['audits'] else 'N/A'
                    title_importance = calculate_title_importance(title, query)
                    headers_importance = calculate_headers_importance(headers, query)
                    body_text_importance = calculate_body_text_importance(body_text, query)
                    meta_tags_importance = calculate_meta_tags_importance(meta_tags, query)
                    alt_text_for_images_importance = calculate_alt_text_for_images_importance(alt_text_for_images, query)
                    backlinks_importance = calculate_backlinks_importance(backlinks)
                    writer.writerow([i, url, title_importance, headers_importance, body_text_importance, meta_tags_importance, alt_text_for_images_importance, loading_speed_score, backlinks_importance])
                except Exception as e:
                    print(f"Error parsing URL {url}: {str(e)}")
                    continue