from bs4 import BeautifulSoup
import requests
import pandas as pd


columns = [
    'Title',
    'Url',
    'Price',
    'Area',
    'Address'
    ]

houseitems = pd.DataFrame(columns=columns)
rangeFrom = 0
rangeTO = 0
totalcount = '0'


def Read_Cover(webpage):
    print("Start Scrape...")
    try:
        page = requests.get(webpage)
    except:
        return;


    print(page.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify)
    
    print("-------------------------------------")
    global houseitems

    datum = soup.findAll('li', {'class': 'result-row'})

    houseitems.drop(houseitems.index, inplace=True) #clear the dataframe
    for data in datum:
        a = data.find('a',{'class': 'result-title'}).text
        print(a)

        b = data.find('a',{'class': 'result-title'}).get('href')
        print(b)
        
        c = data.find('span',{'class': 'result-price'}).text
        print(c)

        if hasattr(data.find('span',{'class': 'housing'}), 'text') == True:
            d = data.find('span',{'class': 'housing'}).text.splitlines()
            if len(d) > 1:
                dd = []
                for str in d:
                    str = str.strip()
                    dd.append(str.strip()[:-1].strip()) if str.strip()[-1:] == '-' else dd.append(str.strip())
                d=''
                for str in dd:
                    d += str + ' '
            d = d.strip()
            print(d)
        else:
            d = "-NA-"

        
        if hasattr(data.find('span',{'class': 'result-hood'}), 'text') == True:
            e = data.find('span',{'class': 'result-hood'}).text.strip()
            if e[-1:] == ')':
                e = e[:-1].strip() 
            if e[0] == '(':
                e = e[1:].strip() 
            print(e)
        else:
            e="-NA-"
            print(e)
        
        
        df = {'Title': a, 'Url': b, 'Price': c, 'Area': d, 'Address': e}
        houseitems = houseitems.append(df, ignore_index=True)

    global rangeFrom
    global rangeTO
    global totalcount

    rangeFrom = soup.find('span', {'class': 'rangeFrom'})
    rangeTO = soup.find('span', {'class': 'rangeTo'})
    totalcount = soup.find('span', {'class': 'totalcount'})
    
    houseitems
    print(houseitems)
    print(len(houseitems))
    

