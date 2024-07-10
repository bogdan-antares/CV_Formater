# CV_Formater

Application permettant de formater des CV pour l'entreprise Antares. Cette version est conçue uniquement pour une utilisation sur Windows.

## Mode d'emploi de l'installation de l'application :

### Étape 1 :

Faire un clic droit sur l'icône Windows, puis cliquer sur "Windows PowerShell (admin)".

### Étape 2 :

Entrer la commande suivante :

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

### Étape 3 :

Fermer la page PowerShell et la rouvrir de la même manière que précédemment puis entrer la commande suivante :

```powershell
choco install python -y
```

Une fois l'installation terminée, fermez et rouvrez PowerShell, puis entrez la commande suivante pour vérifier la bonne installation de Python :

```powershell
python --version
```

### Étape 4 :

Entrer les commandes suivantes :

```powershell
winget install Python.Python3 -y
pip install numpy
choco install git -y
pip install kivy
pip install openai
pip install python-docx
pip install python-dateutil
pip install python-dotenv
```

### Étape 5 :

Aller maintenant dans l'équipe Teams où se trouve le dossier CV_Formater, puis téléchargez-le. Ouvrez votre téléchargement, faites "Extraire" et choisissez le répertoire où vous voulez placer le dossier.

### Étape 6 :

Dans le dossier, faites un clic droit sur le fichier _'cv_formater.bat'_ et sélectionnez _'Envoyer vers Bureau'_. Un raccourci sera alors créé et l'application sera utilisable en cliquant sur le raccourci.

## Guide d'utilisation de l'application

Pour utiliser l'application, il suffit d'entrer un texte dans la zone de texte et de cliquer sur "Formater le CV". Choisissez ensuite le dossier où vous allez enregistrer le fichier ainsi que son nom (il n'est pas nécessaire de préciser l'extension, le fichier sera automatiquement un fichier .docx). Attendez quelques secondes le temps de la génération du fichier, puis un message indiquera que le fichier a bien été généré et où il se trouve dans le répertoire de l'appareil. L'opération est répétable.

## Comment cette application a été mise en œuvre

Pour créer cette application de formatage de CV au format de l'entreprise Antares, nous avons pris avantage de l'IA pour rendre le processus rapide et simple. Dans un premier temps, le texte que l'utilisateur va entrer est celui qui se trouve dans le CV à formater. Ensuite, trois requêtes sont envoyées à ChatGPT via son API : une pour les formations du candidat, une pour les compétences, et une dernière pour ses expériences professionnelles. L'objectif est qu'à l'issue de ces requêtes, l'IA retourne des tableaux Python où les informations du candidat sont spécifiquement organisées pour pouvoir être utilisées dans le script qui crée le fichier .docx. Ce script crée le template de l'entreprise, puis prend les tableaux et place les informations dans le fichier grâce à des boucles `for`. Pour que l'IA puisse bien créer ces tableaux, il a fallu lui donner des exemples de tableaux Python dans les prompts. Enfin, nous utilisons Kivy pour créer l'interface utilisateur.
