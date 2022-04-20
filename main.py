import PySimpleGUI as sg
import requests
from requests_html import AsyncHTMLSession
import asyncio
from bs4 import BeautifulSoup


result_counter = 0


def inputGUI():
    layout = [
        [sg.Text('Choose Website')],
        [sg.Checkbox('Fake Jobs', default=False, key='FakeJobs'), sg.Checkbox('MS3', default=False, key='MS3'), sg.Checkbox('WVU Office of Health Affairs', default=False, key='WVU')],
        [sg.Checkbox('Career Builder', default=False, key='CB'), sg.Checkbox('Indeed', default=False, key='Indeed'), sg.Checkbox('USAJobs', default=False, key='USA')],
        [sg.Checkbox('IRS', default=False, key='IRS')],
        [sg.Text('Job Title', size=(15, 1)), sg.InputText()],
        [sg.Text('Company Name', size=(15, 1)), sg.InputText()],
        [sg.Text('Location', size=(15, 1)), sg.InputText()],
        [sg.Button("Submit"), sg.Button("Cancel"), sg.Button("Clear Results")],
        [sg.Text('Job Results')],
        [sg.Output(key='Output', size=(100, 20))]
    ]
    window = sg.Window('Web Scraper', layout).finalize()
    window['Output'].TKOut.output.config(wrap='word')
    while True:
        event, values = window.read()
        global result_counter
        if event == "Submit":
            if values['FakeJobs']:
                print("Beautiful Soup Tutorial Results")
                scraped = tutorial(values)
                for value in scraped:
                    print(value)
                print("The number of results found is: " + str(result_counter))
            if values['MS3']:
                print("MS3 Results")
                scraped = ms3(values)
                for value in scraped:
                    print(value)
                print("The number of results found is: " + str(result_counter))
            if values['WVU']:
                print("WVU Office of Health Affairs Results")
                scraped = health(values)
                for value in scraped:
                    print(value)
                print("The number of results found is: " + str(result_counter))
            if values['CB']:
                print("Career Builder Results")
                scraped = career_builders(values)
                for value in scraped:
                    print(value)
                print("The number of results found is: " + str(result_counter))
            if values['Indeed']:
                print("Indeed Results")
                results = asyncio.run(indeed_builder(values))
                if len(results) == 0:
                    print("No Results")
                print("The number of results found is: " + str(result_counter))
            if values['USA']:
                print("USAJobs Results")
                scraped = usajobs(values)
                for value in scraped:
                    print(value)
                print("The number of results found is: " + str(result_counter))
            if values['IRS']:
                print("IRS Results")
                scraped = irs(values)
                for value in scraped:
                    print(value)
                print("The number of results found is: " + str(result_counter))
        if event == "Cancel" or event == sg.WIN_CLOSED:
            window.close()
            break
        if event == "Clear Results":
            window.FindElement('Output').Update('')


def tutorial(values):
    global result_counter
    result_counter = 0
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
        if (values[0] == title_element.text.strip() or values[0] == "") and \
                (values[1] == company_element.text.strip() or values[1] == "") and \
                (values[2] == location_element.text.strip() or values[2] == ""):
            elements.append("Job Title:" + title_element.text.strip())
            elements.append("Company Name: " + company_element.text.strip())
            elements.append("Location: " + location_element.text.strip())
            link_url = link_element[1]["href"]
            elements.append(f"Apply Here: {link_url}\n")
            result_counter += 1
    if len(elements) == 0:
        elements.append("No results")
    return elements


def ms3(values):
    global result_counter
    result_counter = 0
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
        if values[0] == title_element.text.strip() or values[0] == '':
            elements.append("Job Title: " + title_element.text.strip())
            elements.append("Position Summary: \n" + description.text.strip())
            elements.append(f"Apply Here: {link_url}\n")
            result_counter += 1
    if len(elements) == 0:
        elements.append("No results")
    return elements


def health(values):
    global result_counter
    result_counter = 0
    url = "http://health.wvu.edu/healthaffairs/careers/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    elements = []
    results = soup.find(id="content")
    target = results.find(class_="page-primary rich-text")
    for child in target.children:
        if child.name == "h4":
            if values[0] == child.text.strip() or values[0] == "":
                elements.append("Job Title: " + child.text.strip())
                result_counter += 1
                while True:
                    child = child.nextSibling
                    if child.name == "h4" or child.name == "h3":
                        break
                    elif child.name == "p":
                        elements.append(child.text.strip())
    if len(elements) == 0:
        print("No results")
    return elements


def career_builders(values):
    global result_counter
    result_counter = 0
    url = "https://www.careerbuilder.com/jobs?emp=" + "&keywords=" + values[0] + "&location=" + values[2]
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
        result_counter += 1
    if len(elements) == 0:
        elements.append("No Results")
    return elements


async def indeed_scraper(session, link):
    new_page = await session.get(link)
    new_soup = BeautifulSoup(new_page.content, 'html.parser')
    position_name = new_soup.find('h1', class_='icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title')
    company_name = new_soup.find('div', class_='jobsearch-CompanyReview--heading')
    description = new_soup.find('div', id='jobDescriptionText')
    if company_name is None:
        company_name = new_soup.find('div',
                                     class_="jobsearch-InlineCompanyRating icl-u-xs-mt--xs jobsearch-DesktopStickyContainer-companyrating")
        for child in company_name.children:
            if child.text.strip() != '':
                company_name = child
                break
    print("Position Name: " + position_name.text.strip())
    print("Company Name: " + company_name.text.strip())
    print(description.text.strip() + "\n")


async def indeed_builder(values):
    global result_counter
    result_counter = 0
    session = AsyncHTMLSession()
    if values[0] != '':
        values[0] = values[0].replace(' ', '%20')
    if values[1] != '':
        values[1] = values[1].replace(' ', '%20')
    if values[2] != '':
        values[2] = values[2].replace(' ', '%20')
    links = []
    url = "https://www.indeed.com/jobs?q=" + values[0] + values[1] + "&l" + values[2]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    targets = soup.findAll('a', class_='tapItem')
    for target in targets:
        link_piece = (target['href'])
        links.append('https://www.indeed.com' + link_piece)
        result_counter += 1
    elements = (indeed_scraper(session, link) for link in links)
    return await asyncio.gather(*elements)


def usajobs(values):
    global result_counter
    result_counter = 0
    elements = []
    url = "https://www.usajobs.gov/Search/ExploreOpportunities?Series=1550"
    page = requests.get(url)
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
        if (values[0] == title_element.text.strip() or values[0] == "") and \
                (values[1] == agency_element.text.strip() or values[1] == "") and \
                (values[2] == location_element.text.strip() or values[2] == ""):
            elements.append("Job title: " + title_element.text.strip())
            elements.append("Department: " + department_element.text.strip())
            elements.append("Agency: " + agency_element.text.strip())
            elements.append("Location: " + location_element.text.strip())
            elements.append("Description: " + description_element.text.strip())
            elements.append("Apply here: " + link_element["href"] + "\n")
            result_counter += 1
    if len(elements) == 0:
        elements.append("No results")
    return elements


def irs(values):
    global result_counter
    result_counter = 0
    elements = []
    url = "https://www.jobs.irs.gov/careers"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("tbody")
    job_elements = []
    for child in results.children:
        if child != "\n":
            job_elements.append(child)
    for job_element in job_elements:
        title_element = job_element.find("td", class_="views-field views-field-title position")
        grade_element = job_element.find("td", class_="views-field views-field-nothing-1")
        location_element = job_element.find("td", class_="views-field views-field-field-usajobs-locations")
        link_element = job_element.find("a")
        if (values[0] == title_element.text.strip() or values[0] == "") and \
                (values[1] == location_element.text.strip() or values[1] == ""):
            elements.append("Position: " + title_element.text.strip())
            elements.append("Grade and Pay Range: " + grade_element.text.strip())
            elements.append("Locations: " + location_element.text.strip())
            elements.append("Apply here: " + link_element["href"] + "\n")
            result_counter += 1
    if len(elements) == 0:
        elements.append("No results")
    return elements


sg.theme('SandyBeach')
inputGUI()
