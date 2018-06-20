from bs4 import BeautifulSoup
import pandas as pd
import glob
import pprint

def DOI_extract(identifiers):
    '''Extract DOI reference from metadata'''
    if identifiers==[]:
        return

    for link in identifiers:

        if link.text[:4] == 'doi:':
#             return link.text[4:]
            return link.text

    return float('nan')


def journal_extract(identifiers):
    '''Extract Journal reference from metadata'''
    if identifiers==[]:
        return float('nan')

    for link in identifiers:
        if link.text[:4] != 'doi:' and link.text[:5] != 'http:':
                return link.text


    return float('nan')


def fields_of_interest(soup):
    '''Gathers xml tags of interest from arxiv'''
    fields = []
    ident = soup.find_all('dc:identifier')
    fields.append(DOI_extract(ident))
    fields.append(journal_extract(ident))

    try:
        fields.append(soup.find_all('dc:title')[0].text)
    except:
         fields.append(float('nan'))


    try:
        fields.append(soup.find_all('dc:description')[0].text)
    except:
         fields.append(float('nan'))

    try:
        fields.append(soup.find_all('dc:subject')[0].text)
    except:
         fields.append(float('nan'))

    return fields





if __name__ == '__main__':
    info = []
    for name in glob.glob('data\*'):

        soup = bs.BeautifulSoup(open(name), "lxml-xml")

    #     pprint.pprint(fields_of_interest(soup))
        info.append(fields_of_interest(soup))

    df = pd.DataFrame(info,columns=['DOI', 'Journal', 'title','Abstract','Categories'])
    df.to_csv('test.csv',index=False)
