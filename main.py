import requests
import random
from bs4 import BeautifulSoup

# with open("proxy_server/valid_proxies.txt", "r") as f:
#     proxies = [proxy.strip() for proxy in f.readlines() if proxy.strip()]

# def fetch_and_save_to_file(url, path):
#     selected_proxy = random.choice(proxies)
#     print(f"Selected proxy: {selected_proxy}")

#     proxy_dict = {
#         'http': selected_proxy,
#         'https': selected_proxy
#     }

#     try:
#         r = requests.get(url, proxies=proxy_dict, timeout=10)
#         r.raise_for_status()  

#         with open(path, 'w', encoding="utf-8") as f:
#             f.write(r.text)
#         print(f"Content saved to {path}")

#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching URL using proxy {selected_proxy}: {e}")

# url = "https://learn.microsoft.com/en-us/office/developer-program/terms-and-conditions"

# fetch_and_save_to_file(url, "data/test.html")

scraped_html_path = "data/test.html"

with open(scraped_html_path, "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")
page_text = soup.get_text(separator="\n")
page_text = ' '.join(page_text.split())
print(page_text)
