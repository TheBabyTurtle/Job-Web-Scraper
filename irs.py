import requests
from bs4 import BeautifulSoup

URL = "https://www.jobs.irs.gov/careers"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="main")
# print(results.prettify())

# job_elements = results.find_all("tr", class_="odd views-row-first")
job_elements = results.find_all("tr", class_="even")
# job_elements = results.find_all("tr", class_="odd")
# job_elements = results.find_all("tr, class_="odd views-row-last')
for job_element in job_elements:
    title_element = job_element.find("td", class_="views-field views-field-title position")
    grade_element = job_element.find("td", class_="views-field views-field-nothing-1")
    location_element = job_element.find("td", class_="views-field views-field-field-usajobs-locations")
    link_element = job_element.find("a")
    print("Position: " + title_element.text.strip())
    print("Grade and Pay Range: " + grade_element.text.strip())
    print("Locations: " + location_element.text.strip())
    print("Apply here: " + link_element["href"] + "\n")
