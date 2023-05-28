Array_URLS = []
Objects_scraped = 0
while True:
    input_link = input("Enter link to scrape from Blocket.se:")
    if input_link == "":
        break
    input_title = input("""Enter corresponding name of search (i.e. "Fender Stratocaster":""")
    Array_URLS.append([input_link,input_title])
    Objects_scraped += 1

print(Array_URLS)