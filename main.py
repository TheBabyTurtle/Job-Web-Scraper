import PySimpleGUI as sg
import requests
from bs4 import BeautifulSoup


def inputGUI():
    layout = [
        [sg.Text('Job Results')],
        [sg.Output(key='Output', size=(100, 30))],
        [sg.Text('Choose Website')],
        [sg.Combo(['https://realpython.github.io/fake-jobs/', 'https://www.ms3-inc.com/careers/',
                   'http://health.wvu.edu/healthaffairs/careers/'])],
        [sg.Text('Job Title', size=(8, 1)), sg.InputText()],
        [sg.Text('Location', size=(8, 1)), sg.InputText()],
        [sg.Button("Submit"), sg.Button("Cancel"), sg.Button("Clear")]
    ]
    window = sg.Window('Web Scraper', layout).finalize()
    window['Output'].TKOut.output.config(wrap='word')
    while True:
        event, values = window.read()
        if event == "Submit":
            if values[0] == 'https://realpython.github.io/fake-jobs/':
                print("Beautiful Soup Tutorial Results")
                for value in tutorial(values):
                    print(value)
            if values[0] == 'https://www.ms3-inc.com/careers/':
                print("MS3 Results")
                for value in ms3(values):
                    print(value)
            if values[0] == 'http://health.wvu.edu/healthaffairs/careers/':
                print("WVU Office of Health Affairs Results")
                for value in health(values):
                    print(value)
        if event == "Cancel" or event == sg.WIN_CLOSED:
            window.close()
            break
        if event == "Clear":
            window.FindElement('Output').Update('')


def tutorial(values):
    elements = []
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
        if values[1] == title_element.text.strip() or values[2] == location_element.text.strip() or values[1] == "" or values[2] == "":
            elements.append("Job Title:" + title_element.text.strip())
            elements.append("Company Name: " + company_element.text.strip())
            elements.append("Location: " + location_element.text.strip())
            link_url = link_element[1]["href"]
            elements.append(f"Apply Here: {link_url}\n")
    return elements


def ms3(values):
    elements = []
    url = "https://www.ms3-inc.com/careers/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="site-inner")
    job_elements = results.find_all("li", class_="career-oppt")
    for job_element in job_elements:
        title_element = job_element.find("div", class_="skill-title")
        link_element = job_element.find("a")
        link_url = link_element["href"]
        element_page = requests.get(link_url)
        element_soup = BeautifulSoup(element_page.content, "html.parser")
        element_results = element_soup.find(id="site-inner")
        description = element_results.find("div", class_="career-highlight")
        if values[1] == title_element.text.strip() or values[1] == "":
            elements.append("Job Title: " + title_element.text.strip())
            elements.append("Position Summary: " + description.text.strip())
            elements.append(f"Apply Here: {link_url}\n")
    return elements


def health(values):
    url = "http://health.wvu.edu/healthaffairs/careers/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    elements = []
    results = soup.find(id="content")
    target = results.find(class_="page-primary rich-text")
    for child in target.children:
        if child.name == "h4":
            if values[1] == child.text.strip() or values[1] == "":
                elements.append("Job Title: " + child.text.strip())
                while True:
                    child = child.nextSibling
                    if child.name == "h4" or child.name == "h3":
                        break
                    elif child.name == "p":
                        elements.append(child.text.strip())
    return elements


sg.theme('SandyBeach')
inputGUI()
