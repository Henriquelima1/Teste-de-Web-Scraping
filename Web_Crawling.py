import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import re

def crawl_and_index(url):
    try:
        # Faz o download da página HTML
        response = requests.get(url)
        response.raise_for_status()

      
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extrai o texto da página e remove caracteres não alfanuméricos
        page_text = re.sub(r'\W+', ' ', soup.get_text()).lower()

        # Tokeniza o texto em palavras
        words = page_text.split()

        
        index = defaultdict(list)
        for position, word in enumerate(words):
            index[word].append(position)

        return index

    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar a página {url}: {e}")
        return None


url = 'http://passofundo.ifsul.edu.br'
index = crawl_and_index(url)

if index:
    
    print("Índice Invertido:")
    for word, positions in index.items():
        print(f"{word}: {positions}")
