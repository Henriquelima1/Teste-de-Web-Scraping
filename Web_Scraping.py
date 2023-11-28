import requests
from bs4 import BeautifulSoup

def scrape_details(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar todos os elementos que contêm informações 
        elements = soup.find_all('div', class_='span4')

        # Lista para armazenar os detalhes
        details = []

        # Iterar sobre os elementos e extrair informações
        for element in elements:
            
            image_tag = element.find('a', class_='img-rounded')
            if image_tag:
                image = image_tag.get('href')
            else:
                image = 'N/A'

            
            decicao_tag = element.find('p', class_='description')
            if decicao_tag:
                decicao = decicao_tag.text.strip()
            else:
                decicao = 'N/A'

            
            info = {
                'image': image,
                'decicao': decicao
            }

            # Adicionar o dicionário à lista de detalhes
            details.append(info)

        # Imprimir os detalhes 
        print("Detalhes do site:")
        for info in details:
            print(f"Imagem: {info['image']}")
            print(f"Decisão: {info['decicao']}")
            print("\n")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar a página {url}: {e}")

# Exemplo de uso
url = 'http://passofundo.ifsul.edu.br'
scrape_details(url)
