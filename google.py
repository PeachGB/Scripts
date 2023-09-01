#! /usr/bin/python3
import webbrowser, sys, requests, bs4

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    #get the links
    res = requests.get('https://www.google.com/search?q=' + address)
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    links = soup.find_all("h3")
    parents = list()
    for i, link in enumerate(links):
        if link.find_parent('a') != None:
            print(i, link.get_text())
        
        parents.append(link.find_parent('a'))
    x = int(input("Select link: "))
    if parents[x] != None:
        href = parents[x].get('href')
        webbrowser.open('http://google.com' + href)
    else:
        print('not a valid url')
else:
    print("provide search")
    
