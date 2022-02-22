import requests
from bs4 import BeautifulSoup

URL = "https://www.ms3-inc.com/careers/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
# print(page.text)
results = soup.find(id="site-inner")
# print(results.prettify())
job_elements = results.find_all("li", class_="career-oppt")
for job_element in job_elements:
    title_element = job_element.find("div", class_="skill-title")
    print(title_element.text.strip())
    # print(job_element, end="\n"*2)
