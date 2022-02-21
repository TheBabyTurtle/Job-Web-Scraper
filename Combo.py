import PySimpleGUI as sg
import requests
from bs4 import BeautifulSoup

# Sample website: https://realpython.github.io/fake-jobs/

sg.theme('SandyBeach')

layout = [
    [sg.Text('Choose Website')],
    [sg.Combo(['https://realpython.github.io/fake-jobs/', 'https://www.ms3-inc.com/careers/'])],
    [sg.Text('Job Title', size=(8, 1)), sg.InputText()],
    [sg.Text('Location', size=(8, 1)), sg.InputText()],
    [sg.Button("Submit"), sg.Button("Cancel")]
]

window = sg.Window('Web Scraper', layout)
while True:
    event, values = window.read()
    if event == "Submit":
        URL = values[0]
        Job_Title = values[1]
        Location = values[2]
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find(id="ResultsContainer")
        job_elements = results.find_all("div", class_="card-content")
        for job_element in job_elements:
            title_element = job_element.find("h2", class_="title")
            company_element = job_element.find("h3", class_="company")
            location_element = job_element.find("p", class_="location")
            link_element = job_element.find_all("a")
            if values[1] == title_element.text.strip() and values[2] == location_element.text.strip():
                print(title_element.text.strip())
                print(company_element.text.strip())
                print(location_element.text.strip())
                link_url = link_element[1]["href"]
                print(f"Apply Here: {link_url}\n")
                print()
            
        break
    if event == "Cancel":
        break
window.close()
