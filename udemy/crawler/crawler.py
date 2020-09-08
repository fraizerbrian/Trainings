#!usr/bin/env python
import requests
import re

def request(url):
    try:
        return requests.get("http://"+url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "http://zsecurity.org"

def extract_links_from(url):
    response = requests.get(target_url)
    return re.findall('(?:href=")(.*?)"', response.content)

href_links = extract_links_from(target_url)
print(href_links)

# with open("/home/fraize/Desktop/Trainings/udemy/crawler/files-and-dirs-wordlist","r") as wordlist_file:
#     for line in wordlist_file:
#         word = line.strip()
#         test_url = target_url + "/" + word
#         response = request(test_url)
#         if response:
#             # print("[+] Discovered subdomain --> " + test_url)
#             print("[+] Discovered url --> " + test_url)
