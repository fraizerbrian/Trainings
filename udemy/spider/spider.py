#!usr/bin/env python
import requests
import re
#import urlparse #for python2
import urllib.parse as urlparse #for python3


def request(url):
    try:
        return requests.get("http://"+url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "https://zsecurity.org" #use link of website
target_links = []

def extract_links_from(url):
    response = requests.get(target_url)
    return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))

def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = urlparse.urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)

crawl(target_url)
