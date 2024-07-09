import os
import openai
import re
import subprocess
import sys

# Définir la clé API OpenAI
api_key = 'sk-proj-RcYuvwOdivawba3brVatT3BlbkFJs5nSIgV3vl1YjxectVCp'  # Remplacez par votre clé API réelle

exemple1 = """
# Ajouter des entrées de formation, le tableau fromations doit s'appeler "formations". Ne change pas le nom je te rappelle que ce que tu retourne sera directement inclut dans un code python et donc il faut que respecter la structure :
formations = [
    ("2023", "Certificat de compétence Analyste en Cybersécurité, CNAM / Cours à Distance"),
    ("2012", "BTS Informatique de Gestion (niveau), Lycée Saint Paul Bourdon Blanc, Orléans"),
    ("2010", "BAC Pro, Micro-Informatique, Installation et maintenance, Lycée Saint Paul Bourdon Blanc, Orléans"),
    ("2008", "BAC Technologique STI Génie Electronique, Lycée Maurice Genevoix, Ingé, France")
]
"""

exemple2 = """
# Ajouter des compétences et sous-compétences, le tableau competences doit s'appeler 'competences'. Ne change pas le nom je te rappelle que ce que tu retourne sera directement inclut dans un code python et donc il faut que respecter la structure :
competences = {
    "Logiciels & Compétences": [
        "Support utilisateurs",
        "Active directory (classique)",
        "Déploiement",
        "Pack Office 2013, 19, 365",
        "Gestion de parc SI",
        "Sécurité informatique"
    ],
    "Langues": [
        "Français : Bilingue",
        "Espagnol : Compétences professionnelles"
    ]
}
"""

exemple3 = """
# Ajouter des expériences professionnelles, le tableau experience doit s'appeler "experiences". Ne change pas le nom je te rappelle que ce que tu retourne sera directement inclut dans un code python et donc il faut que respecter la structure et evite d'avoir cette erreur : 

entreprise, periode, poste, description, technologies = experience
ValueError: not enough values to unpack (expected 5, got 4) :

experiences = [
    ("ORCOM", "Depuis 2020 – Orléans", "Technicien de support Informatique",
     [
         "Commande, déploiement, gestion de stock, attributions des matériels informatique et au besoin retour garantie (DELL).",
         "Mise à jour des applications métiers serveur et utilisateurs.",
         "Création utilisateurs (Active directory, exchange, office 365, ouverture accès application métier, gestion de droits).",
         "Gestion des demandes et des incidents utilisateurs (modification droits, accès aux applications après validation).",
         "Déplacements sur site distant si besoin.",
         "Gestion de la plateforme de filtrage de mail.",
         "Gestion des incidents de niveau 1, 2 et 3 en support des administrateurs réseau si besoin."
     ], ["Active Directory", "Exchange", "Office 365"]),
    ("SERVIER", "Mai 2020 - Août 2020 – Orléans", "Technicien de déploiement",
     [
         "Déploiement de poste neuf sous Windows 10, installation application métier et livraison à l’utilisateur final après prise de rendez-vous.",
         "Gestion des incidents et des problématiques après livraison du poste à l’utilisateur final."
     ], ["Windows 10"]),
    ("Conseil Régional Du Centre", "Mai 2019 - Août 2019 et Décembre 2019 – Orléans", "Technicien support de Niveau 2",
     [
         "Installation et paramétrage de nouveaux matériels.",
         "Gestion des incidents de niveau 2, prise en main à distance ou déplacement auprès des collaborateurs."
     ], []),
    ("Siemens, Banques CIC, Valloire Habitat", "Septembre 2019 - Novembre 2019 – Région Centre", "Technicien de déploiement",
     [
         "Paramétrage smartphone, déploiement applications et livraison utilisateur final.",
         "Déploiement image et paramétrage applications."
     ], ["Smartphone Configuration", "Application Deployment"]),
    ("Adecco, Proman, Smathpeople, etc.", "2012 - 2019 – Région Centre", "Technicien IT",
     [
         "Différentes missions intérim dans des domaines variés."
     ], [])
]
"""

# Fonction pour envoyer une requête à l'API GPT
def send_to_gpt(prompt, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=4000  # Augmenté pour s'assurer que toutes les informations sont couvertes
    )
    return response['choices'][0]['message']['content'].strip()

def main(cv_test_file, save_path):
    # Lire le texte du CV depuis le fichier
    with open(cv_test_file, 'r', encoding='utf-8') as file:
        cv_text = file.read()
        
    tab_py = [exemple1, exemple2, exemple3]
    tab_titres = ["formation", "compétences", "expériences professionnels"]
    compt = 0
    final_text = ""

    while compt < 3 : 
        for i in tab_titres :
            # Préparer la requête pour GPT
            prompt = f"""
            Voici le contenu d'un CV :
            
            {cv_text}
        
            Veuillez trier les informations de {i} et les formater en structures de données Python comme ci-dessous, donc servez vous de l'exemple ci-dessous pour formater les données de {i} du texte ci-dessus issue d'un CV :
        
            {tab_py[compt]}
        
            Dans ta réponse, répond seulemnt avec du code python, si tu veut rajouter un texte tu met un '#' sinon tu ne répond uniquement qu'avec du code python car ta réponse sera directement enregistré dans un code python. Pense a bien respecté la structure des tableaux. Si par exemple il manque une année dans les formations, met des accolades vides à cet endroit. Pense aussi à respecter le nom du tableau de l'exemple et le même que celui ou tu vas stocker les données.
            """

            # Envoyer la requête à GPT
            sorted_info = send_to_gpt(prompt, api_key)
            print("Informations triées par GPT :\n", sorted_info)

            # Supprimer les lignes contenant ''' ou '''python
            lines = sorted_info.split('\n')
            cleaned_info = '\n'.join(line for line in lines if "```" not in line)

            # Ajouter les informations nettoyées au texte final
            final_text += cleaned_info + '\n'
            compt += 1
        
    # Enregistrer la réponse nettoyée dans un fichier data.py
    with open('data.py', 'w', encoding='utf-8') as f:
        f.write(final_text)
        
    # Run the example.py script
    try:
        result = subprocess.run(['python', 'exemple.py', save_path], check=True, capture_output=True, text=True)
        print(f"STDOUT: {result.stdout}")
        print(f"STDERR: {result.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        print(f"Output: {e.stdout}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python web.py <cv_text_file> <save_path>")
        sys.exit(1)
    
    cv_text_file = sys.argv[1]
    save_path = sys.argv[2]
    
    main(cv_text_file, save_path)

