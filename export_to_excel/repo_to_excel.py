# A script to extract the table from the ladies of landsat repo and create excel file from it
# Author: Andrew Cutts 22/01/2022
# Version: 1.0

import pandas as pd
import requests
from bs4 import BeautifulSoup


def main():
    # use pandas to convert url to list
    url = 'https://github.com/ladiesoflandsat/LOLManuscriptMonday/blob/main/README.md'
    url_info = pd.read_html(url)
    # convert to dataframe
    df = url_info[0]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')

    links = []
    for tr in table.findAll("tr"):
        trs = tr.findAll("td")
        for each in trs:
            try:
                link = each.find('a')['href']
                links.append(link)
            # TODO make a better exception
            except:
                pass
    
    # your getting a dump of 3 times the links so I want to split it into a nested list. 
    # TODO remove magic numbers
    length_links = len(links)//3
    result = [links[i::3] for i in range(length_links)]

    # convert to dataframe
    columns_url = ['link_article', 'link_handle', 'link_tweet']
    df_links = pd.DataFrame(columns=columns_url)
    for i in range(length_links):
        df_links.loc[i] = result[0][i], result[1][i], result[2][i]

    # join df_links to df
    df = pd.concat([df, df_links], axis=1)
    for link_col in columns_url:
        df[link_col] = df[link_col].map(lambda short_link: '=HYPERLINK("{}","{}")'.format(short_link,short_link))
    # save to excel drop index
    # TODO write date to filename
    df.to_excel('LadiesofLandsat_README.xlsx', index=False)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


