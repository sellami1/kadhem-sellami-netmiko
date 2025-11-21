# Mon Projet Netmiko
## I. Initialiser un dépôt Git local
### 1. mkdir kadhem-sellami-netmiko
### 2. cd kadhem-sellami-netmiko && git init

## II. Ajouter et commiter des fichiers
### 1. nano README.md
### 2. git add README.md && git commit -m "Ajout du fichier README."
### 3. nano main.py
### 4. git add main.py && git commit -m "Ajout du script Python principal".
### 5. git log

## III. Créer et fusionner des branches
### 1. git checkout -b feature/netmiko
### 2. nano main.py
### 3. git add . && git commit -m "Ajout de la fonction acces_netmiko."
### 4. git checkout main
### 5. git merge feature/netmiko

## IV. Travailler avec un dépôt distant sur GitHub
### 1. IU Web
### 2. git remote add origin <repo_url>
### 3. git push origin main
### 4. IU Web
### 5. IU Web
### 6. git fetch origin && git checkout -b feature/salut origin/feature/salut
### 7. nano main.py
### 8. git add . && git commit -m "Ajout de la fonction dire_salut."
### 9. git push origin feature/salut
### 10. IU Web
### 11. IU Web
### 12. git pull
 