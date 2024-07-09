# CV_Formater

Application permettant de formater des CV pour l'entreprise Antares. Cette version est seulement conçu pour une utilisaton sur Windows.

# Mode d'emploie de l'installation de l'application : 

## Etape 1 :

Faire clique droit sur l'icône Windows, puis cliquer sur "Windows PowerShell (admin)".

## Etape 2 :

Entrer la commande suivante : 

```Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient.DownloadString('https://community.chocolatey.org/install.ps1'))```

## Etape 3 :

Fermer la page PowerShell et réouvrer-la de la même manière que précedemment puis entrer la commande suivante :

```choco install python -y```

Puis lorsque l'installation est terminé, fermer et réouvrer la page PowerShell et entrer la commande suivante pour vérifier la bonne installation de Python : 

```python --version```

## Etape 4 : 

Entrer les commandes suivante : 

```winget install Python.Python3 -y```
```pip install numpy```
```choco install git -y```
```pip install kivy```
```pip install openai```
```pip install python-docx```
```pip install pyhon-dateuil```

## Etape 6 :

Toujours dans le termianal, veuillez rentrer la commande suivante :



## Etape 5 :

Dans le dossier, faire clique droit sur la fichier _'cv_formater.bat'_ et faire _'envoyer vers Bureau'_. Un raccourci sera alors crée et l'application sera utilisable. en cliquant sur le raccourci.
