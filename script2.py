import requests
from bs4 import BeautifulSoup
import json

url = "https://www.dicionariopopular.com/girias-paraenses/"

# gaucha, paranaense, bahiana

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')

p_elements = [p for p in soup.find_all('p') if p.strong]

girias = []

print(p_elements)
for p in p_elements:
    giria_strong = p.strong
    if giria_strong:
        giria = giria_strong.text
        giria_strong.extract()
        descricao = p.text.strip()
        
        girias.append({
            "giria": giria.replace(":", ""),
            "descricao": descricao
        })

with open("girias.json", "w") as f:
    json.dump(girias, f, indent=4, ensure_ascii=False)
