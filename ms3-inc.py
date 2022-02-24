import requests
from bs4 import BeautifulSoup

URL = "https://www.ms3-inc.com/careers/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="site-inner")

job_elements = results.find_all("li", class_="career-oppt")
for job_element in job_elements:
    title_element = job_element.find("div", class_="skill-title")
    link_element = job_element.find("a")
    # if values[1] == title_element.text.strip():
    print(title_element.text.strip())
    link_url = link_element["href"]
    print(f"Apply Here: {link_url}\n")

