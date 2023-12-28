from bs4 import BeautifulSoup
import requests

current_page = 21
# Iterate through the site pages
for _ in range(1, current_page):
    # Request to the main site
    response = requests.get(url=f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={_}")
    web_page = response.text

    # Find laptop names and detailed description
    soup = BeautifulSoup(web_page, "html.parser")
    laptop_names = soup.find_all(name="a", class_="title")
    laptop_information = soup.find_all(name="p", class_="description")

    # Create a list with laptops text
    laptops = []
    for i in range(len(laptop_names)):
        laptop_model = []
        laptop_model.append(laptop_names[i].text)
        laptop_model.append(laptop_information[i].text)
        laptops.append(laptop_model)

    print(laptops)
