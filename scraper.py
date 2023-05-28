import requests
from bs4 import BeautifulSoup
import time
import random
import yagmail

URL = "https://www.blocket.se/annonser/hela_sverige"


def parse_site(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

def send_email(header, info):
    receiver = "thisisnotanemail@gmail.com"

    yag = yagmail.SMTP("thisisnotanemail1@gmail.com")
    yag.send(
        to=receiver,
        subject=header,
        contents=info,

    )


def get_latest_add():
    soup = parse_site(URL)
    ad_elems = soup.find_all("article", class_="hidZFy")
    latest_add = ad_elems[0]

    ad_name = latest_add.find("span", class_="jzzuDW").text
    ad_price = latest_add.find("div", class_="jkvRCw").text
    ad_link = latest_add.find("a", class_="enigRj")["href"]


    return (ad_name, ad_price, ad_link)

get_latest_add()
prev_ad_name, prev_ad_price, prev_ad_link = get_latest_add()
print("The latest ad is: ", prev_ad_name, "\nPrice: ", prev_ad_price, "\nLink: ", prev_ad_link, sep='') 

found_ad_counter = 0
while True:
    duration_sleep = random.randint(50,60)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S",t)
    time.sleep(duration_sleep)
    ad_name, ad_price, ad_link = get_latest_add()
    if ad_name == prev_ad_name:
        #No new ads
        print("No new ads..." + current_time)
        pass
    else:
        #Match found

        ad_link = "https://www.blocket.se" + ad_link
        ad_link = ad_link.strip()
        email_contant = "The latest ad is: " + ad_name, "\nPrice: " + ad_price + "\nLink: ", ad_link,

        print("Ny annons: " + ad_name + current_time)
        print("sending email...")
        send_email(ad_name, email_content)
        prev_ad_name = ad_name
        found_ad_counter += 1