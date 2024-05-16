"""
Ce script permet de récupérer les contenus, les descriptions ainsi que les titres d'articles issus du site francetvinfo.fr/sciences, puis de les stocker dans un fichier au format Parquet.
Le fichier obtenu au format Parquet comporte deux colonnes : "text" (qui contient le contenu de chaque article) et "summary" (qui contient leur description).

Il utilise selenium qui permet d'automatiser les interaction du navigateur web, ici Firefox, dans le but d'extraire les données souhaitées.

Pour utiliser ce script, il est nécessaire d'avoir installé en amont :
- geckodriver (qui est le web driver utilisé pour selenium avec Firefox)
- selenium
- pandas

Voici la commande a effectuer pour lancer le script : 
python3 web_scrap.py
"""
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


service = Service(executable_path='/home/clotilde/Downloads/geckodriver')
service.start()
options = Options()
options.headless = True
profile_path = "/home/clotilde/snap/firefox/common/.mozilla/firefox/v4mzyour.default"
options.add_argument(f"-profile {profile_path}")
driver = webdriver.Firefox(service=service, options=options)


url = "https://www.francetvinfo.fr/sciences/"
driver.get(url)
time.sleep(3)

#Récupération de tous les liens des articles de la page
articles = driver.find_elements(By.CLASS_NAME, "card-article-list-l__link")
#print(articles)

contents = []
descriptions = []

#Récupération des attributs : title, description et content de chaque article par son lien 
for article in articles:

    lien = article.get_attribute("href")
    #print(lien)
    
    driver.get(lien)
    time.sleep(2)

    page_title = driver.title
    #print("Titre de la page:", page_title)
        
    article_description_element = driver.find_element(By.CLASS_NAME, "c-chapo")
    description = article_description_element.text
    #print("Description:", description)
    descriptions.append(description)

    article_content_element = driver.find_element(By.CLASS_NAME, "c-body")
    article_content = article_content_element.text
    #print("Contenu de l'article:", article_content)
    contents.append(article_content)

    time.sleep(5)
    driver.back()
    
driver.quit()

#Création du fichier avec l'extension parquet avec deux colonnes : text et summary comme le corpus de référence orange_sum
df = pd.DataFrame({"text": contents, "summary": descriptions})
df.to_parquet("articles.parquet", index=False)