"""
Ce script permet de pretraiter les données des articles récupérés.

Il utilise les bibliothèques :
- panda pour charger le fichier parquet initial et enregistrer le fichier une fois nettoyé 
- re pour nettoyer les données avec des expressions régulières
- nltk pour la tokenisation des données

Voici la commande a effectuer pour lancer le script : 
python3 pre_traitements.py
"""
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download("punkt")
nltk.download("stopwords")

stop_words_fr = set(stopwords.words("french"))

def preprocess_text(corpus):
    """
    Cette fonction est une fonction de prétraitement pour le nettoyage du texte pour par la suite pouvoir vectoriser les données.

    Args:
    - corpus (str) : corpus à prétraiter

    Returns:
    - corpus (str): corpus prétraité
    """
    #Suppression de la ponctuation
    corpus = re.sub(r'[^\w\s]', '', corpus)
    #Tokenisation
    tokens = word_tokenize(corpus, language='french')
    #Supprimer des stopwords et ignorer la casse (mise en minuscule)
    tokens = [word.lower() for word in tokens if word.lower() not in stop_words_fr]
    return ' '.join(tokens)


def main():
    '''
    Fonction principale du script de preprocessing.

    Permet de charger un fichier au format parquet qui contient les données, de nettoyer ces données et enfin, de les enregistrer dans un nouveau fichier au format parquet.
    '''
    #Chargement du fichier Parquet
    df = pd.read_parquet("articles_cleaned.parquet")

    #Application du prétraitement aux deux colonnes "text" et "summary"
    df["text"] = df["text"].apply(preprocess_text)
    df["summary"] = df["summary"].apply(preprocess_text)

    #Enregistrement du nouveau fichier Parquet nettoyé
    df.to_parquet("articles_preprocessed.parquet", index=False)

if __name__ == "__main__":
    main()