import requests
from bs4 import BeautifulSoup

URL = "https://www.usajobs.gov/Search/Results?j=1550#"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="main-content")
# print(results.prettify())
# Only shows government positions in high demand

job_elements = results.find_all("li", class_="usajobs-search-no-params-highlight__list-item")
for job_element in job_elements:
    title_element = job_element.find("a")
    print(title_element.text.strip())
    # print(job_element.prettify(), end="\n"*2)