import PySimpleGUI as sg
import requests
from bs4 import BeautifulSoup

sg.theme('SandyBeach')

layout = [
    [sg.Text('Choose Website')],
    [sg.Combo(['https://realpython.github.io/fake-jobs/', 'https://www.ms3-inc.com/careers/',
               'http://health.wvu.edu/healthaffairs/careers/'])],
    [sg.Text('Job Title', size=(8, 1)), sg.InputText()],
    [sg.Text('Location', size=(8, 1)), sg.InputText()],
    [sg.Button("Submit"), sg.Button("Cancel")]
]

window = sg.Window('Web Scraper', layout)


def tutorial():
    url = "https://realpython.github.io/fake-jobs/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    job_elements = results.find_all("div", class_="card-content")
    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        link_element = job_element.find_all("a")
        if values[1] == title_element.text.strip() or values[2] == location_element.text.strip():
            print(title_element.text.strip())
            print(company_element.text.strip())
            print(location_element.text.strip())
            link_url = link_element[1]["href"]
            print(f"Apply Here: {link_url}\n")
            print()


def ms3():
    url = "https://www.ms3-inc.com/careers/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="site-inner")
    job_elements = results.find_all("li", class_="career-oppt")
    for job_element in job_elements:
        title_element = job_element.find("div", class_="skill-title")
        link_element = job_element.find("a")
        if values[1] == title_element.text.strip():
            print(title_element.text.strip())
            link_url = link_element["href"]
            print(f"Apply Here: {link_url}\n")


def health():
    url = "http://health.wvu.edu/healthaffairs/careers/"
    page = requests.get(url)
    counter = 0
    soup = BeautifulSoup(page.content, "html.parser")
    pieces = []
    piece = []
    results = soup.find(id="content")
    target = results.find(class_="page-primary rich-text")
    for child in target.children:
        if child.name == "h4":
            piece.append(child.text.strip())
            while True:
                child = child.nextSibling
                if child.name == "h4" or child.name == "h3":
                    pieces += piece
                    counter += 1
                    piece.clear()
                    break
                elif child.name == "p":
                    piece.append(child.text.strip())
    for bit in pieces:
        print(bit)


while True:
    event, values = window.read()
    if event == "Submit":
        URL = values[0]
        Job_Title = values[1]
        Location = values[2]
        if values[0] == 'https://realpython.github.io/fake-jobs/':
            tutorial()
        if values[0] == 'https://www.ms3-inc.com/careers/':
            ms3()
        if values[0] == 'http://health.wvu.edu/healthaffairs/careers/':
            health()
        break
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break
window.close()
