import requests
from bs4 import BeautifulSoup

URL = "https://www.indeed.com/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="jobsearch-HomePage")
job_elements = results.find_all("div", class_="serpLinking-Column-Entry")
for job_element in job_elements:
    # title_element = job_element.find("div", div="aria-label")
    # print(title_element.text.strip())
    print(job_element, end="\n"*2)
# print(results.prettify())
