import requests
from bs4 import BeautifulSoup

URL = "https://www.careerbuilder.com/jobs-near-me"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="site-content")
job_elements = results.find_all("li", class_="data-results-content-parent relative")
for job_element in job_elements:
    print(job_element.prettify(), end="\n" * 2)
    # title_element = job_element.find("div", class_="data-results-title dark-blue-text b")
    # print(title_element.text.strip())
    # job_details = job_element.find("div", class_= "data-details")
    # print(job_details.text.strip())
