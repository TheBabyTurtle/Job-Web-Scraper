import PySimpleGUI as sg
import requests
from bs4 import BeautifulSoup


def inputGUI():
    layout = [
        [sg.Text('Choose Website')],
        [sg.Combo(['Fake Jobs', 'MS3', 'WVU Office of Health Affairs', 'Career Builder', 'Indeed', 'USAJobs'])],
        [sg.Text('Job Title', size=(8, 1)), sg.InputText()],
        [sg.Text('Location', size=(8, 1)), sg.InputText()],
        [sg.Button("Submit"), sg.Button("Cancel"), sg.Button("Clear Results")],
        [sg.Text('Job Results')],
        [sg.Output(key='Output', size=(100, 20))]
    ]
    window = sg.Window('Web Scraper', layout).finalize()
    window['Output'].TKOut.output.config(wrap='word')
    while True:
        event, values = window.read()
        if event == "Submit":
            if values[0] == 'Fake Jobs':
                print("Beautiful Soup Tutorial Results")
                for value in tutorial(values):
                    print(value)
            if values[0] == 'MS3':
                print("MS3 Results")
                for value in ms3(values):
                    print(value)
            if values[0] == 'WVU Office of Health Affairs':
                print("WVU Office of Health Affairs Results")
                for value in health(values):
                    print(value)
            if values[0] == 'Career Builder':
                print("Career Builder Results")
                for value in career_builders(values):
                    print(value)
            if values[0] == 'Indeed':
                print("Indeed Results")
                for value in indeed(values):
                    print(value)
            if values[0] == 'USAJobs':
                print("USAJobs Results")
                for value in usajobs(values):
                    print(value)
        if event == "Cancel" or event == sg.WIN_CLOSED:
            window.close()
            break
        if event == "Clear Results":
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
        if (values[1] == title_element.text.strip() or values[1] == "") and \
                (values[2] == location_element.text.strip() or values[2] == ""):
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
            elements.append("Position Summary: \n" + description.text.strip())
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


def career_builders(values):
    url = "https://www.careerbuilder.com/jobs?emp=" + "&keywords=" + values[1] + "&location=" + values[2]
    elements = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="site-content")
    job_elements = results.find_all("li", class_="data-results-content-parent relative")
    for job_element in job_elements:
        title_element = job_element.find("div", class_="data-results-title dark-blue-text b")
        job_details = job_element.find("div", class_="data-details")
        job_details = job_details.findAll("span")
        job_description = job_element.findAll("div", class_="block")
        job_link = job_element.find("a")
        elements.append("\n" + "Job Title: " + title_element.text.strip())
        if len(job_details) == 3:
            elements.append("Company Name: " + job_details[0].text.strip())
            elements.append("Location: " + job_details[1].text.strip())
            elements.append("Part/Full-time: " + job_details[2].text.strip())
        elif len(job_details) == 2:
            elements.append("Location: " + job_details[0].text.strip())
            elements.append("Part/Full-time: " + job_details[1].text.strip())
        elements.append("Description: " + job_description[0].text.strip())
        if job_description[1].text.strip() != "":
            elements.append("Salary/Pay: " + job_description[1].text.strip())
        else:
            elements.append("No salary/pay given.")
        elements.append("Apply Here: https://www.careerbuilder.com/" + job_link["href"])
    return elements


def indeed(values):
    elements = []
    url = "https://www.indeed.com/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="jobsearch-HomePage")
    job_elements = results.find_all("div", class_="serpLinking-Column-Entry")
    # Only shows trending searches
    for job_element in job_elements:
        title_element = job_element.find("a")
        if values[1] == title_element.text.strip() or values[1] == "":
            elements.append(title_element.text.strip())
    return elements


def usajobs(values):
    elements = []
    url = "https://www.usajobs.gov/Search/Results?j=1550#"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="main-content")
    # Only shows Computer Science government positions in high demand
    job_elements = results.find_all("li", class_="usajobs-search-no-params-highlight__list-item")
    for job_element in job_elements:
        title_element = job_element.find("a")
        if values[1] == title_element.text.strip() or values[1] == "":
            elements.append(title_element.text.strip())
    return elements


sg.theme('SandyBeach')
inputGUI()
