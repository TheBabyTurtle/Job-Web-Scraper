import requests
from bs4 import BeautifulSoup

URL = "https://www.usajobs.gov/Search/ExploreOpportunities?Series=1550"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="main-content")
# Only shows Computer Science government positions

job_elements = results.find_all("div", class_="usajobs-search-result--card")
for job_element in job_elements:
    title_element = job_element.find("h3", class_="usajobs-search-result__title")
    department_element = job_element.find("h4", class_="usajobs-search-result__department")
    agency_element = job_element.find("h5", class_="usajobs-search-result__agency")
    location_element = job_element.find("h4", class_="usajobs-search-result__location")
    description_element = job_element.find("p", class_="usajobs-search-result__multi-line")
    link_element = job_element.find("a")
    print("Job title: " + title_element.text.strip())
    print("Department: " + department_element.text.strip())
    print("Agency: " + agency_element.text.strip())
    print("Location: " + location_element.text.strip())
    print("Description: " + description_element.text.strip())
    print("Apply here: " + link_element["href"] + "\n")
    # print(job_element.prettify(), end="\n"*2)
