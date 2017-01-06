import argparse
import re
import dateparser
import datetime
from bs4 import BeautifulSoup


def name_old_repositories(file, days_old):
    html = open(file, 'r')
    soup = BeautifulSoup(html, 'html.parser')
    now = datetime.datetime.now()

    for repository_soup in soup.find('table', class_='repositories').find('tbody').find_all('tr'):
        age_text = repository_soup.find('span', class_=re.compile("age[0-9]+")).get_text()
        repository_name_text = repository_soup.find('a', class_='list').get_text()
        age_datetime = dateparser.parse(age_text)

        if age_datetime is None:
            print('{:<50} ! WARNING - failed to parse date last updated: {}'.format(repository_name_text, age_text))
            continue

        days_since_last_updated = (now - age_datetime).days

        if days_since_last_updated > days_old:
            print('{:<50} - last updated approximately {:.0f} days ago'.format(repository_name_text, days_since_last_updated))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', default='./git.html', help='target file to parse for old repos, default ./git.html')
    parser.add_argument('-d', '--days-old', default=30, help='how recently a repo needs to have been updated, default 30')
    args = parser.parse_args()
    name_old_repositories(file=args.file, days_old=args.days_old)
