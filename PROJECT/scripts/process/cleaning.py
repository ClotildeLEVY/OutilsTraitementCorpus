"""
Ce script permet de nettoyer le contenu (text) des articles récupérés.

Il utilise les bibliothèques :
- panda pour charger le fichier parquet initial et enregistrer le fichier une fois nettoyé 
- re pour nettoyer les données avec des expressions régulières

Voici la commande a effectuer pour lancer le script : 
python3 cleaning.py
"""
import pandas as pd
import re

def clean_text(text):
    """
    Nettoyage du "text" (contenu des articles) en supprimant : 
    - emojis
    - photos (liens)
    - les sections "à lire aussi[...]"
    - mentions twitter
    - hashtags

    Args: 
    text (str): le texte à nettoyer.

    Returns:
    text (str): le texte nettoyé.
    """
    #Suppression des emojis
    text = re.sub(r"[\U00010000-\U0010ffff]", "", text)
    #Suppression des photos
    text = re.sub(r"pic.twitter.com/\w+", "", text)
    #Suppression des mentions twitter
    text = re.sub(r"@\w+", "", text)
    #Suppression des rubriques "à lire aussi"
    text = re.sub(r"(?i)\nà lire aussi\n.*?\n", "", text)
    #Suppression des hashtags
    text = re.sub(r"#\w+", "", text)

    return text

def main():
    '''
    Fonction principale du script de nettoyage.

    Permet de charger un fichier au format parquet qui contient les données brutes, de nettoyer ces données et enfin, de les enregistrer dans un nouveau fichier au format parquet.
    '''
    #Chargement du fichier Parquet
    df = pd.read_parquet("articles.parquet")

    #Application de la fonction de nettoyage sur la partie "text" du fichier
    df["text"] = df["text"].apply(clean_text)

    #Enregistrement du nouveau fichier Parquet nettoyé
    df.to_parquet("articles_cleaned.parquet", index=False)

if __name__ == "__main__":
    main()