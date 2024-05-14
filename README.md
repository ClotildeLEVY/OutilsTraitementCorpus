# Outils de Traitement de Corpus
>_dépôt des tp pour le cours Outils de Traitement de Corpus_


Le projet consiste en l'établissement d'un corpus exploitable selon la tâche que nous souhaitons réaliser.

&nbsp;

## DESCRIPTION DU CORPUS

Le corpus que j'ai choisi est **orange_sum** disponible via le lien suivant : [_lien vers le corpus_](https://huggingface.co/datasets/orange_sum).  
La langue traitée est le français, uniquement.

Sa tâche est la **summarization** _(résumé de données textuelles)_.  
Voici ses sous-tâches :

- _new-articles-headline-generation_ 
- _news-articles-summarization_

&nbsp;

Les informations que comporte le corpus sont constituées de deux champs : **text** et **summary**.  
Le champ **text** contient l'intégralité du texte et le champ **summary** le résumé du texte dont il est question.  
Extraction des descriptions et des titres des articles.

&nbsp;

Taille du corpus :

- 58 060 lignes d'informations
- taille : 50.4 MB et 84.2 MB _(au format Parquet)_

&nbsp;

Ce corpus peut servir pour diverses prédictions comme par exemple la classification de textes _(à quelle catégorie un texte appartiennent)_, en recherche d'information pour trouver des textes pertinents selon des requêtes spécifiques ou encore pour l'analyse de sentiment en fonction des différents sujets des articles.

Concernant les modèles entraînés avec ce corpus, nous distinguons :

- T5-Ponctuation
- BART-CNN-Orangesum
- bert2gpt2SUMM

&nbsp;

L'intégralité des données de ce corpus sont issues du site "Orange Actu" [_lien vers le site_](https://actu.orange.fr/france/). Les données récoltées s'étendent de février 2011 à septembre 2020 et proviennet des cinq grandes catégories du site : _France_, _Monde_, _Politique_, _Automobile_ et _Société_ _(qui regroupe quant à elle un total de huit sous-catégories)_.
  
>la catégorie _Automobile_ semble avoir été remplacée par _Économie_ et nous distinguons également une nouvelle catégorie : _Vie Digitale_.

&nbsp;

Les données ont été divisées en train-validation-test :  
→ pour les résumés : 21 400 train, 1 500 validation et 1 500 test  
→ pour les titres : 30 658 train, 1 500 validation et 1 500 test

&nbsp; 

Le corpus **orange_sum** a été publié sur hugging face en 2020 par _Eddine Moussa Kamal_, _Tixier Antoine J-P_ et _Vazirgiannis Michalis_. 
