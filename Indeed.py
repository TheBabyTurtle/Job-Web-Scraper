import requests
import asyncio
from bs4 import BeautifulSoup


async def indeed():
    links = []
    URL = "https://www.indeed.com/jobs?q=Network%20Administrator"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    targets = soup.findAll('a', class_='tapItem')
    for target in targets:
        links.append(target['href'])
    for link in links:
        print(link)
        new_page = requests.get('https://www.indeed.com' + link)
        new_soup = BeautifulSoup(new_page.content, 'html.parser')
        position_name = new_soup.find('h1', class_='icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title')
        company_name = new_soup.find('div', class_='jobsearch-CompanyReview--heading')
        if company_name is None:
            company_name = new_soup.find('div', class_="jobsearch-InlineCompanyRating icl-u-xs-mt--xs jobsearch-DesktopStickyContainer-companyrating")
            for child in company_name.children:
                if child.text.strip() != '':
                    company_name = child
                    break
        description = new_soup.find('div', id='jobDescriptionText')
        print(position_name.text.strip())
        print(company_name.text.strip())
        print(description.text.strip())
asyncio.run(indeed())
