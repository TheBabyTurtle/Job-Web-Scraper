import requests
from bs4 import BeautifulSoup

URL = "https://www.careerbuilder.com/jobs-near-me"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="site-content")
job_elements = results.find_all("li", class_="data-results-content-parent relative")
for job_element in job_elements:
    title_element = job_element.find("div", class_="data-results-title dark-blue-text b")
    job_details = job_element.find("div", class_="data-details")
    job_details = job_details.findAll("span")
    job_description = job_element.findAll("div", class_="block")
    job_link = job_element.find("a")
    print("\n" + "Job Title: " + title_element.text.strip())
    print("Company Name: " + job_details[0].text.strip())
    print("Location: " + job_details[1].text.strip())
    print("Part/Full-time: " + job_details[2].text.strip())
    print("Description: " + job_description[0].text.strip())
    if job_description[1].text.strip() != "":
        print("Salary/Pay: " + job_description[1].text.strip())
    else:
        print("No salary/pay given.")
    print("Apply Here: https://www.careerbuilder.com/" + job_link["href"])
    
