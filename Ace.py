import requests
from bs4 import BeautifulSoup

URL = "https://careers-aceinfosolutions.icims.com/jobs/search?ss=1"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="content")
job_elements = results.find_all("div", class_="content")
#for job_element in job_elements:
    #print(job_elements, end="\n" * 2)
    # title_element = job_element.find("var", jobImpressions="positionType")
    #company_element = job_element.find("h3", class_="company")
    #location_element = job_element.find("p", class_="location")
    #print(title_element.text.strip())
    #print(company_element.text.strip())
    #print(location_element.text.strip())
    #print()
print(results.prettify())
