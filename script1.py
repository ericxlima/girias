import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json


url = "https://www.dicionariopopular.com/girias-mineiras/"

## Paulista, nordeste, carioca, mineira

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')

h3_elements = soup.find_all('h2')

girias = []

for h3 in h3_elements:
    giria_dict = {}
    giria_dict["giria"] = h3.text
    if h3.find_next('p'):
        giria_dict["significado"] = h3.find_next('p').text
    else:
        break
    exemplos = []
    for blockquote in h3.find_all_next('blockquote'):
        if blockquote.find_previous('h2') == h3: 
            exemplos.extend([p.text for p in blockquote.find_all('p')])
        else:
            break

    giria_dict["exemplos"] = exemplos

    girias.append(giria_dict)

with open("girias.json", "w") as f:
    json.dump(girias, f, indent=4, ensure_ascii=False)